# Load TIFF File as a normalized grayscale matrix

import cv2 as cv
import numpy as np

def load_img_grayscale(path: str, depth: int = 8) -> np.ndarray:
  img = cv.imread(path, cv.IMREAD_GRAYSCALE)
  N = np.float32((2 ** depth) - 1)

  def normalize(n: np.float32):
    return n / N

  normalizev = np.vectorize(normalize)

  norm = img.astype(np.float32)
  norm = normalizev(norm)

  return norm

def img_denormalize(img: np.ndarray, depth: float|int = 8) -> np.ndarray:
  max_val = np.float32((2 ** depth) - 1)

  denormalizev = np.vectorize( lambda n: np.floor(n * max_val))

  denorm = denormalizev(img)

  if depth == 8:
    denorm = denorm.astype(np.uint8)
  elif depth == 16:
    denorm = denorm.astype(np.uint16)
  elif depth == 32:
    denorm = denorm.astype(np.uint32)
  elif depth <= 8:
    if depth == 0: max_val = np.float32(1)
    frac = 255 / max_val
    denorm = (denorm * frac).astype(np.uint8)
  else:
    assert False, "Unsupported depth"

  return denorm

def write_img_grayscale(img: np.ndarray, outfile: str, depth: float|int = 8):
  out = img_denormalize(img, depth)
  cv.imwrite(outfile, out)



