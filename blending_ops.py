import numpy as np
from load_grayscale import *

def clamp(min, x, max):
  if x < min:
    return min
  if x > max:
    return max
  return x

def add_img(imgA: np.ndarray, imgB: np.ndarray) -> np.ndarray:
  assert imgA.shape == imgB.shape
  res = imgA.copy()
  for row, _ in enumerate(res):
    for col, _ in enumerate(res[row]):
      pxA, pxB = res[row][col], imgB[row][col]
      res[row][col] = clamp(0.0, pxA + pxB, 1.0)

  return res

def mul_img(imgA: np.ndarray, imgB: np.ndarray) -> np.ndarray:
  assert imgA.shape == imgB.shape
  res = imgA.copy()
  for row, _ in enumerate(res):
    for col, _ in enumerate(res[row]):
      pxA, pxB = res[row][col], imgB[row][col]
      res[row][col] = clamp(0.0, pxA * pxB, 1.0)

  return res

