from load_grayscale import *
from blending_ops import *

def main():
  img = load_normalized_grayscale('camera.tiff')
  noise = np.random.normal(0, 0.5, img.shape)
  res = add_img(img, noise)
  write_normalized_grayscale(res, 'out.tiff')

if __name__ == '__main__': main()
