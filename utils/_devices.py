from torch import device
from torch.cuda import is_available
"""
devices
"""
device_gpu = device('cuda:0')
device_cpu = device('cpu')
