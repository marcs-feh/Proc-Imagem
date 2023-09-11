import numpy as np
import matplotlib.pyplot as plt
# from utils import read_image, write_plot_image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

# def plot_mse(image_name, mse_value, image_without_noise, image_with_noise):
#   fig, ax = plt.subplots(figsize=(10, 5))
#
#   # Use seaborn color palette for better colors
#   colors = sns.color_palette("bright")
#
#   # Plot the histogram of image without noise (excluding 255 and 0)
#   ax.hist(image_without_noise.ravel(), bins=253, range=(1, 254), color=colors[0], alpha=0.7, label='Without Noise')
#   ax.hist(image_with_noise.ravel(), bins=253, range=(1, 254), color=colors[3], alpha=0.7, label='With Noise')
#   ax.axvline(x=mse_value, color=colors[8], linestyle='--', label=f'MSE = {mse_value:.2f}')  # Use the same color as 'With Noise'
#
#   # Set labels and legend
#   ax.set_xlabel('Pixel Value')
#   ax.set_ylabel('Frequency')
#   fig.legend(loc='upper right')
#
#   # Save the plot
#   plt.tight_layout()
#   write_plot_image(image_name, "mse", plt)



def img_mse(denorm_img_original: np.ndarray, demorn_img_noise: np.ndarray) -> np.float64:
  n, m = denorm_img_original.shape

  mse = np.sum((denorm_img_original - demorn_img_noise)**2) / (n * m)

  return mse.astype(np.float64)


def img_psnr(denorm_img_original: np.ndarray, denorm_img_noisy: np.ndarray):
  mse_value = img_mse(denorm_img_original, denorm_img_noisy)
  max_value = np.max(denorm_img_original)

  psnr = 10 * np.log10((max_value ** 2) / mse_value)
  return psnr

