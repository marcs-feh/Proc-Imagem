from convolution import convolution
import numpy as np

def edge_detection(img: np.ndarray) -> np.ndarray:
  horizontal = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]]) * 0.25

  vertical = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]]) * 0.25

  res_h = convolution(img, horizontal) ** 2
  res_v = convolution(img, vertical) ** 2
  res = np.clip(0.0, np.sqrt(res_h + res_v), 1.0)
  return res

