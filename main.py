from load_grayscale import *
from convolution import *
from edge_detection import *
from histogram import *
from noise import img_gaussian_noise

def main():
  path = 'touhou_weed.tiff'
  img = load_normalized_grayscale(path)
  res = img_gaussian_noise(img, 0.2, 0);
  res = edge_detection(res)
  write_normalized_grayscale(res, 'conv.out.tiff')

  # save_img_histogram(img, 'hist.out')
  # img_count = 240
  # for i in range(0, img_count):
  #   n = i * (8.0/img_count)
  #   p = f'out/{i:08}.tiff'
  #   write_normalized_grayscale(img, p, n)
  #   print(f'wrote {p}')

if __name__ == '__main__': main()
