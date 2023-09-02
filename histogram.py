import numpy as np
import matplotlib.pyplot as plt

def img_8bit_val_count(img: np.ndarray):
  counts = np.zeros(256, np.uint64)

  h, w = img.shape
  for row in range(0, h):
    for col in range(0, w):
      idx = int(img[row, col] * 0xff)
      counts[idx] += 1

  return counts


def save_img_histogram(img, outfile: str, title: str = ''):
  try:
    plt.title(title)
    plt.xlabel('Pixel Value [0, 255]')
    plt.ylabel('Count')
    plt.bar(list(range(0,256)), img_8bit_val_count(img))
    plt.savefig(f'{outfile}.png', dpi=300)
  finally:
    plt.clf()

