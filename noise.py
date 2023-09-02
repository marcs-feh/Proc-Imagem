import numpy as np

def img_gaussian_noise(img: np.ndarray, std_dev: float = 25, mean: float = 0) -> np.ndarray:
    noise = np.random.normal(mean, std_dev, img.shape)
    noisy_image = np.clip(0.0, img + noise, 1.0)
  
    return noisy_image
