# IPAM
#Image processing and manipulation
Our package aims to make tools for image processing and manipulation by providing a user-friendly interface. It includes two modules, color_modifier and image_processing, which offer several methods for applying filters, increasing the brightness, cropping, mirroring, grascaling, etc.
The package consists modules, classes and methods for better code organization, encapsulation of data and behavior, reusability, modularity, and abstraction, which contribute to cleaner, more efficient, and easier-to-maintain. 
Two external libraries is been used in making IPAM. Numpy for manipulation of the arrays whereas Matplotlib for importing and saving the images.
There are certain libraries available for image processing with the similar functionality, including OpenCV, scikit-image, etc. However, our library is distinct in the way, we have performed the operations in addition to its simple layout that can easily be understood and used by beginners.
Examples:
# cropping an image and then increasing its brightness
import numpy as np
import matplotlib.pyplot as plt
from color_modifier import IPAM
from image_processing import IPAM
ipam = IPAM()
ipam.crop_image("rose.jpg","output_file" left=100, right=100, top=200, bottom=200)
ipam.brightness_adjustment("rose.jpg","output_image")

#color_filter
import numpy as np
import matplotlib.pyplot as plt
from color_modifier import IPAM
from image_processing import IPAM
image 


