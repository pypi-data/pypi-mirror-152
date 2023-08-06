# Torch unified

Adds support for [unified memory](https://developer.nvidia.com/blog/unified-memory-cuda-beginners/) to torch. 

### Usage

```python
import torch
from torch_unified import empty_unified

tensor_cpu, tensor_gpu = empty_unified((10,), torch.float32)
```
