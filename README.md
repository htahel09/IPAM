# IPAM
#Image processing and manipulation

Our package aims to make tools for image processing and manipulation by providing a user-friendly interface. It includes two modules, color_modifier and image_processing, which offer several methods for applying filters, increasing the brightness, cropping, mirroring, grascaling, etc.
The package consists modules, classes and methods for better code organization, encapsulation of data and behavior, reusability, modularity, and abstraction, which contribute to cleaner, more efficient, and easier-to-maintain. 

Two external libraries is been used in making IPAM. Numpy for manipulation of the arrays whereas Matplotlib for importing and saving the images.
There are certain libraries available for image processing with the similar functionality, including OpenCV, scikit-image, etc. However, our library is distinct in the way, we have performed the operations in addition to its simple layout that can easily be understood and used by beginners.

Examples:

# cropping an image and increasing the brightness

import numpy as np

import matplotlib.pyplot as plt

from IPAM.color_modifier import IPAM1

from  IPAM.image_processing import IPAM2

ipam2 = IPAM2()

ipam2.crop_image("rose.jpg","output_file1.jpg",left=100, right=100, top=200, bottom=200)

ipam1 = IPAM1()

ipam1.brightness_adjustment("rose.jpg","output_image2.jpg")

# applying vignette effect

import numpy as np

import matplotlib.pyplot as plt

from IPAM.color_modifier import IPAM1

ipam1 = IPAM1()

ipam1.vignette_effect("rose.jpg","output_image2.jpg")

# textured image

from  IPAM.image_processing import IPAM2

ipam2 = IPAM2()

ipam2.texture_effect("rose.jpg","textured_image.jpg")
