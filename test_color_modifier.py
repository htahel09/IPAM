import numpy as np
from color_modifier import IPAM

def test_grayscale():
    ipam = IPAM()
    output_file = "rose.jpg"
    # Convert to grayscale
    ipam.grayscale(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0

def test_sepia():
    ipam = IPAM()
    output_file = "rose.jpg"
    # Apply sepia filter
    ipam.sepia(image, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0

def test_solarization():
    ipam = IPAM()
    threshold = 0.5
    output_file = "rose.jpg"
    # Apply solarization filter
    ipam.solarization(image, threshold, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0

def test_color_filter():
    ipam = IPAM()
    color = "RED"
    output_file = "rose.jpg"
    # Apply color filter
    ipam.color_filter(image, color, output_file)
    # Check that the output file exists and is non-empty
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0
