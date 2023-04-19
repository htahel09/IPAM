import numpy as np
import matplotlib.pyplot as plt

def crop_image(image, top, bottom, left, right):
    """Crop an image using NumPy."""
    cropped_image = image[top:-bottom, left:-right, :]
    return cropped_image

def flip_upside_down(image):
    """Flip an image upside down using NumPy."""
    flipped_image = np.flipud(image)
    return flipped_image

def find_mirror_image(image):
    """Find the mirror image of an image using NumPy."""
    mirror_image = np.fliplr(image)
    return mirror_image

def grayscale(image):
    """Convert an image to grayscale using NumPy."""
    grayscale_image = np.dot(image, [0.2989, 0.5870, 0.1140])
    return grayscale_image

def blur_image(image, sigma=1):
    """Blur an image using Gaussian blur without using scipy."""
    k_size = int(3 * sigma) * 2 + 1
    k = np.exp(-np.arange(k_size)**2 / (2*sigma**2))
    k = k / np.sum(k)
    blurred_image = np.apply_along_axis(lambda x: np.convolve(x, k, mode='same'), axis=0, arr=np.apply_along_axis(lambda x: np.convolve(x, k, mode='same'), axis=1, arr=image))
    blurred_image = np.clip(blurred_image, 0, 255).astype(np.uint8) # Add normalization step
    return blurred_image



