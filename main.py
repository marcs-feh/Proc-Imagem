from load_grayscale import *
from blending_ops import *
from convolution import *

def main():
  img = load_normalized_grayscale('camera.tiff')
  noise = np.random.normal(0, 0.25, img.shape)

  # res = add_img(img, noise)
  # write_normalized_grayscale(res, 'add.out.tiff')
  #
  # res = mul_img(img, noise)
  # write_normalized_grayscale(res, 'mul.out.tiff')

  conv_mask = np.array([
    [0.1, 0.1, 0.8],
    [0.2, 0.8, 0.1],
    [0.1, 0.1, 0.3],
  ])

  res = convolution(img, conv_mask)
  write_normalized_grayscale(res, 'conv.out.tiff')

if __name__ == '__main__': main()
