class Normalizer:
    def __init__(self, raw_min: int = -1024, raw_max: int = 3072, norm_min: int = 0, norm_max: int = 256) -> None:
        self.raw_min = raw_min
        self.raw_max = raw_max
        self.norm_min = norm_min
        self.norm_max = norm_max

    def normalize(self, data: np.ndarray or Tensor) -> np.ndarray or Tensor:
        data = data - self.raw_min
        data = data / (self.raw_max - self.raw_min)
        data = data * (self.norm_max - self.norm_min)
        data = data + self.norm_min
        return data

    def denormalize(self, data: np.ndarray or Tensor) -> np.ndarray or Tensor:
        data = data - self.norm_min
        data = data / (self.norm_max - self.norm_min)
        data = data * (self.raw_max - self.raw_min)
        data = data + self.raw_min
        return data
