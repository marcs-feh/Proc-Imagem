from load_grayscale import *
from convolution import *
from edge_detection import *
from histogram import *

def main():
  path = 'touhou_weed.tiff'
  img = load_normalized_grayscale(path)
  res = edge_detection(img)
  save_img_histogram(img, 'hist.out')
  write_normalized_grayscale(res, 'conv.out.tiff')

if __name__ == '__main__': main()
