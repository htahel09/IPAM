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



# Load the image
image = plt.imread('picture.jpg')

# Convert the image to pixel data
pixel_data = np.array(image)

# Increase brightness by adding a constant value
#brightness_increase = 1
#pixel_data = np.clip(pixel_data + brightness_increase, 0, 255).astype(np.uint8)

# Crop the image
top = 10
bottom = 100
left = 20
right = 30
#pixel_data = crop_image(pixel_data, top, bottom, left, right)

# Flip the image upside down
#pixel_data = flip_upside_down(pixel_data)

# Find the mirror image
#mirror_image = find_mirror_image(pixel_data)

# Convert the image to grayscale
#gray_image = grayscale(mirror_image)
pixel_data1 = image.copy()
# Blur the image
sigma = 5
blurred_image = blur_image(pixel_data1, sigma=sigma)


# Save the result as a new file
output_file_name = 'blur1111111222.jpg'
plt.imsave(output_file_name, blurred_image, cmap='gray')

print(f"Image saved as '{output_file_name}' with increased brightness, cropped, flipped upside down, mirrored, converted to grayscale, and blurred.")

