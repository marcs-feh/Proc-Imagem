from load_grayscale import *
from blending_ops import *
from convolution import *

def main():
  img = load_normalized_grayscale('touhou_weed.tiff')
  # noise = np.random.normal(0, 0.25, img.shape)

  # res = add_img(img, noise)
  # write_normalized_grayscale(res, 'add.out.tiff')
  #
  # res = mul_img(img, noise)
  # write_normalized_grayscale(res, 'mul.out.tiff')

  horizontal = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]]) * 0.25

  vertical = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]]) * 0.25

  res_h = convolution(img, horizontal)
  res_v = convolution(img, vertical)
  res = add_img(res_h, res_v)
  write_normalized_grayscale(res, 'conv.out.tiff')

if __name__ == '__main__': main()
