import os
import numpy as np
from image_processing import IPAM
from PIL import Image

def test_mirror_image():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "mirror_image.jpg"
    # Mirror the image
    ipam.mirror_image(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Check that the output image is mirrored correctly
    mirrored_image = np.fliplr(image)
    output_image = np.array(Image.open(output_file))
    assert np.allclose(mirrored_image, output_image)
    
def test_crop_image():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "crop_image.jpg"
    # Crop the image
    ipam.crop_image(image, output_file, left=50, right=50, top=50, bottom=50)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Check that the output image is cropped correctly
    cropped_image = image[50:-50, 50:-50, :]
    output_image = np.array(Image.open(output_file))
    assert np.allclose(cropped_image, output_image)

def test_resize_image():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("input_image.jpg"))
    output_file = "resize_image.png"
    # Resize the image
    new_shape = (image.shape[0]//2, image.shape[1]//2, image.shape[2])
    ipam.resize_image(image, new_shape, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Check that the output image is resized correctly
    expected_image = np.array(Image.fromarray(image).resize((new_shape[1], new_shape[0])))
    output_image = np.array(Image.open(output_file))
    assert np.allclose(expected_image, output_image)
    
def test_texture_effect():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "texture.png"
    # Apply texture effect
    ipam.texture_effect(image, 0.5, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Load input and output images as arrays
    input_array = np.array(Image.open("rose.jpg"))
    output_array = np.array(Image.open(output_file))
    # Check that the output image is textured correctly
    diff = np.abs(output_array - input_array)
    assert np.sum(diff) > 0

def test_rotate_180():
    ipam = IPAM()
    # Read in the input image
    input_image = np.array(Image.open("rose.jpg"))
    # Get the dimensions of the input image
    height, width, channels = input_image.shape
    # Rotate the input image by 180 degrees
    expected_output_image = np.rot90(np.rot90(input_image))
    # Save the expected output image as a PNG file
    expected_output_file = "expected_rotated.png"
    Image.fromarray(expected_output_image).save(expected_output_file)
    # Rotate the input image using the rotate_180 method
    output_file = "rotated.png"
    ipam.rotate_180(input_image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Read in the output image
    output_image = np.array(Image.open(output_file))
    # Check if the output image is rotated correctly
    assert np.array_equal(output_image, expected_output_image)
    # Remove the output files
    os.remove(output_file)
    os.remove(expected_output_file)

def test_invert_image():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg").convert("L"))
    output_file = "inverted.png"
    # Invert the image
    ipam.invert_image(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Check that the output image has inverted colors
    inverted_image = np.array(Image.open(output_file).convert("L"))
    assert np.array_equal(255 - image, inverted_image)

def test_upside_down():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "upside_down.png"
    # Flip the image upside down
    ipam.upside_down(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Check that the output image is correctly upside down
    flipped_image = np.flipud(image)
    output_image = np.array(Image.open(output_file))
    assert np.array_equal(output_image, flipped_image)
    
def test_blurred_image():
    ipam = IPAM()
    # Load image
    image = np.array(Image.open("rose.jpg"))
    output_file = "blurred_image.jpg"
    # Blur the image
    ipam.blur_image(image, output_file, sigma=1)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Load input and output images as arrays
    input_array = np.array(Image.open("rose.jpg"))
    output_array = np.array(Image.open(output_file))
    # Check that the output image is blurred correctly
    diff = np.abs(output_array - input_array)
    assert np.sum(diff) > 0


def test_clockwise_rotation():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "clockwise_rotated.png"
    # Apply clockwise rotation using NumPy
    ipam.clockwise_rotation(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Load the output image and check that it is rotated clockwise by 90 degrees
    output_image = np.array(Image.open(output_file))
    assert output_image.shape == (image.shape[1], image.shape[0], image.shape[2])
    assert np.array_equal(output_image, np.rot90(image, k=-1))

def test_anticlockwise_rotation():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "anticlockwise_rotated.png"
    # Apply anticlockwise rotation using NumPy
    ipam.anticlockwise_rotation(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Load the output image and check that it is rotated anticlockwise by 90 degrees
    output_image = np.array(Image.open(output_file))
    assert output_image.shape == (image.shape[1], image.shape[0], image.shape[2])
    assert np.array_equal(output_image, np.rot90(image, k=1))

def test_rotate_image_by_angle():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "rotated.png"
    # Apply rotation using NumPy
    ipam.rotate_image_by_angle(image, 45, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
    # Load the output image and check that it is rotated by the specified angle
    output_image = np.array(Image.open(output_file))
    assert output_image.shape == image.shape
    assert not np.array_equal(output_image, image)



