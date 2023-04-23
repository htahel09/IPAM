import os
import numpy as np
from color_modifier import IPAM
from PIL import Image

def test_grayscale():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "grayscale.png"
    # Convert to grayscale
    ipam.grayscale(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0


def test_sepia():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    output_file = "sepia.png"
    # Apply sepia filter
    ipam.sepia(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0


def test_solarization():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    threshold = 0.5
    output_file = "solarization.png"
    # Apply solarization filter
    ipam.solarization(image, threshold, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0


def test_color_filter():
    ipam = IPAM()
    # Read in the image
    image = np.array(Image.open("rose.jpg"))
    color = "RED"
    output_file = "color_filter.png"
    # Apply color filter
    ipam.color_filter(image, color, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
