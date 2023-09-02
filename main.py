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

  save_img_histogram(img, 'hist.out')
  write_normalized_grayscale(res, 'conv.out.tiff')

if __name__ == '__main__': main()
