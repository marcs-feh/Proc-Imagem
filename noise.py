import numpy as np

def img_gaussian_noise(img: np.ndarray, mean: float = 0, std_dev: float = 1.0) -> np.ndarray:
    noise = np.random.normal(mean, std_dev, img.shape)
    noisy_image = np.clip(0.0, img + noise, 1.0)
  
    return noisy_image
