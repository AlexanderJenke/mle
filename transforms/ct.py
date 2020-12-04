from torch import Tensor
from numpy import ndarray

class Window:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __call__(self, data: Tensor or ndarray) -> Tensor or ndarray:
        if isinstance(data, Tensor):
            return data.clamp(self.low, self.high)
        elif isinstance(data, ndarray):
            return data.clip(self.low, self.high)
        else:
            raise TypeError(f"{data.__class__} is not supported by the transforms.Window!")