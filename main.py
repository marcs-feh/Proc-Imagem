from image_properties import img_mse, img_psnr
from load_grayscale import img_denormalize, write_img_grayscale, load_img_grayscale
from convolution import convolution
from edge_detection import edge_detection
from histogram import save_img_histogram
from blur import img_blur
from noise import img_gaussian_noise

from sys import argv
from typing import Any

def demo():
  def format_filename(name:str, infix:str):
    l = name.split('.')
    l.insert(1, infix)
    return '.'.join(l)

  images = {
    'lena.tiff': load_img_grayscale('lena.tiff'),
    'clock.tiff': load_img_grayscale('clock.tiff'),
    'barb.tiff': load_img_grayscale('barb.tiff')
  }

  noisy_images:Any = {}

  print('===== NOISE =====')
  for name, img in images.items():
    mean, std_dev = 0, 0.3
    print(f'Applying gaussian noise (mean: {mean}, std_dev:{std_dev}) to "{name}"...  ', end='')
    out = img_gaussian_noise(img, mean, std_dev)


    path = format_filename(name, 'noise')
    noisy_images[path] = out
    write_img_grayscale(out, path)
    print(f'Wrote {path}')

    d_og = img_denormalize(img)
    d_noise = img_denormalize(out)

    mse = img_mse(d_og, d_noise)
    psnr = img_psnr(d_og, d_noise)
    print( f'Stats of {path}:\n'
          +f'  MSE: {mse}\n'
          +f'  PSNR: {psnr}\n')

  print('===== BLUR =====')
  for name, img in noisy_images.items():
    print(f'Applying 3x3 blur to "{name}"...   ', end='')
    out = img_blur(img)
    path = format_filename(name, 'blur')
    write_img_grayscale(out, path)
    print(f'Wrote {path}')

    d_og = img_denormalize(img)
    d_noise = img_denormalize(out)

    mse = img_mse(d_og, d_noise)
    psnr = img_psnr(d_og, d_noise)
    print( f'Stats of {path}:\n'
          +f'  MSE: {mse}\n'
          +f'  PSNR: {psnr}\n')


def main():
  demo()


if __name__ == '__main__': main()

# path = 'touhou_weed.tiff'
# img = load_normalized_grayscale(path)
# # res = img_gaussian_noise(img, 0.2, 0);
# # res = edge_detection(res)
# # write_normalized_grayscale(res, 'conv.out.tiff')
#
# a, b = int(argv[1]), int(argv[2])
#
# start = a
# img_count = b
#
# for i in range(start, img_count):
#   n = i * (8.0/240)
#   p = f'{i:08}'
#   write_normalized_grayscale(img, f'out/img/{p}.tiff', n)
#   print(f'image {p}')
#   save_img_histogram(img_denormalize(img, n), f'out/hist/{p}')
#   print(f'histogram {p}')
