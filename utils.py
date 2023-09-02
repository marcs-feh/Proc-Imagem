import numpy as np
from load_grayscale import *

def clamp(min, x, max):
  if x < min:
    return min
  if x > max:
    return max
  return x

def clamp_img(img: np.ndarray):
  f = lambda x: clamp(0.0, x, 1.0)
  fv = np.vectorize(f)
  return fv(img)

