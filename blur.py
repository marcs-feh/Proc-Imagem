from convolution import convolution
import numpy as np

def img_blur(img: np.ndarray) -> np.ndarray:
  mask = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]]) * (1/9)

  res = convolution(img, mask).clip(0.0, 1.0)
  return res

