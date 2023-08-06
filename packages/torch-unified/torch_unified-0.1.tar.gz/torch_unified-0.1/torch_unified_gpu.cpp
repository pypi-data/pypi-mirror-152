#include <torch/extension.h>
#include <ATen/InitialTensorOptions.h>

#include <cuda.h>
#include <cuda_runtime.h>

#include <map>
#include <vector>


namespace {
    std::map<void*, int> ptr_to_refcount;

    void on_unified_dealloc(void* ptr) {
        if(--ptr_to_refcount[ptr] == 0) {
            cudaFree(ptr);
        }
    }
}



std::tuple<torch::Tensor,torch::Tensor> empty_unified(const std::vector<int64_t> &shape, py::object dtype) {
    auto dtype_cpp = torch::python::detail::py_object_to_dtype(dtype);
    auto elsize = at::elementSize(dtype_cpp);
    int64_t nbytes = elsize;
    for (auto&& sz: shape) {
        nbytes *= sz;
    }
    void* ptr;
    cudaMallocManaged(&ptr, nbytes, cudaMemAttachGlobal);
    ptr_to_refcount[ptr] = 2;
    auto options_cpu = at::TensorOptions().dtype(dtype_cpp).device(c10::kCPU);
    auto options_gpu = at::TensorOptions().dtype(dtype_cpp).device(c10::kCUDA);

    auto ret_cpu = torch::from_blob(ptr, shape, on_unified_dealloc, options_cpu);
    auto ret_gpu = torch::from_blob(ptr, shape, on_unified_dealloc, options_gpu);
    return std::make_tuple(ret_cpu, ret_gpu);
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("empty_unified", &empty_unified, "Alocated a pair of cpu/gpu tensors on unified memory");
}
