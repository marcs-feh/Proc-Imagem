import numpy as np
import matplotlib.pyplot as plt

def img_8bit_val_count(img: np.ndarray):
  counts = np.zeros(256, np.uint64)

  h, w = img.shape
  for row in range(0, h):
    for col in range(0, w):
      idx = img[row, col]
      counts[idx] += 1

  return counts

def img_8bit_val_count_percent(img: np.ndarray):
  counts = np.zeros(256, np.uint64)

  h, w = img.shape
  for row in range(0, h):
    for col in range(0, w):
      idx = img[row, col]
      counts[idx] += 1

  total = img.shape[0] * img.shape[1]
  counts = counts / total

  return counts


def save_img_histogram(img : np.ndarray, outfile: str, title: str = ''):
  try:
    plt.title(title)
    plt.xlabel('Pixel Value [0, 255]')
    plt.ylabel('% of Pixels')
    vals = img_8bit_val_count_percent(img)
    plt.bar(list(range(0,256)), vals)
    if vals.max() >= 0.5:
      plt.ylim(top=1.0)
    elif vals.max() >= 0.25:
      plt.ylim(top=0.5)
    elif vals.max() >= 0.125:
      plt.ylim(top=0.25)
    else:
      plt.ylim(top=0.125)

    plt.savefig(f'{outfile}.png', dpi=300)
  finally:
    plt.clf()

