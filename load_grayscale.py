# Load TIFF File as a normalized grayscale matrix

import cv2 as cv
import numpy as np

def load_normalized_grayscale(path: str, depth: int = 8) -> np.ndarray:
  img = cv.imread(path, cv.IMREAD_GRAYSCALE)
  N = np.float32((2 ** depth) - 1)

  def normalize(n: np.float32):
    return n / N

  normalizev = np.vectorize(normalize)

  norm = img.astype(np.float32)
  norm = normalizev(norm)

  return norm

def write_normalized_grayscale(img: np.ndarray, outfile: str, depth: int = 8):
  N = np.float32((2 ** depth) - 1)

  def denormalize(n: np.float32):
    return np.floor(n * N)

  denormalizev = np.vectorize(denormalize)
  denorm = denormalizev(img).astype(np.uint8) # TODO: This ignores depth, add an if-else or something

  cv.imwrite(outfile, denorm)

