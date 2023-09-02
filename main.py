from load_grayscale import *
from convolution import *
from edge_detection import *

def main():
  img = load_normalized_grayscale('touhou_weed.tiff')
  res = edge_detection(img)
  write_normalized_grayscale(res, 'conv.out.tiff')

if __name__ == '__main__': main()
