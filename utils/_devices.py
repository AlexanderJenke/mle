"""
devices
"""

from torch import device
from torch.cuda import is_available

device_gpu = device('cuda:0')  # gpu
device_cpu = device('cpu')  # cpu


def getDevice():
    """
    returns device_gpu if cuda is available else device_cpu
    :return: torch.device
    """

    device_available = device_gpu if is_available() else device_cpu
    print(f"device: {device_available}")
    return device_available
