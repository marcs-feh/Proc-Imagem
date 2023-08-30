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
  for li, _ in enumerate(res):
    for co, _ in enumerate(res[li]):
      pxA, pxB = res[li][co], imgB[li][co]
      res[li][co] = clamp(0.0, pxA + pxB, 1.0)

  return res

def mul_img(imgA: np.ndarray, imgB: np.ndarray) -> np.ndarray:
  assert imgA.shape == imgB.shape
  res = imgA.copy()
  for li, _ in enumerate(res):
    for co, _ in enumerate(res[li]):
      pxA, pxB = res[li][co], imgB[li][co]
      res[li][co] = clamp(0.0, pxA * pxB, 1.0)

  return res

