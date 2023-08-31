import numpy as np

def valid_mask_shape(mask: np.ndarray) -> bool:
  is_odd = lambda x: (x % 2) != 0
  return ((mask.shape[0] == mask.shape[1]) and
           is_odd(mask.shape[0]) and is_odd(mask.shape[1]))

def convolution(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
  ok = (mask.shape[0] < img.shape[0]) and (mask.shape[1] < img.shape[1]) and valid_mask_shape(mask)
  assert ok

  

  res = img.copy()

  return res
