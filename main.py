from sys import argv
from load_grayscale import *
from convolution import *
from edge_detection import *
from histogram import *
from noise import img_gaussian_noise

def main():
  path = 'touhou_weed.tiff'
  img = load_normalized_grayscale(path)
  # res = img_gaussian_noise(img, 0.2, 0);
  # res = edge_detection(res)
  # write_normalized_grayscale(res, 'conv.out.tiff')

  a, b = int(argv[1]), int(argv[2])

  start = a
  img_count = b

  for i in range(start, img_count):
    n = i * (8.0/240)
    p = f'{i:08}'
    write_normalized_grayscale(img, f'out/img/{p}.tiff', n)
    print(f'image {p}')
    save_img_histogram(img_denormalize(img, n), f'out/hist/{p}')
    print(f'histogram {p}')

if __name__ == '__main__': main()
