import numpy as np 
import matplotlib.pyplot as plt
class IPAM:

    def mirror_image(self, image,output_file):
        """
        The find_mirror_image() method finds the mirror image of a given image using NumPy's fliplr() function.
        NumPy's fliplr() function is used to flip the image along the vertical axis i.e., the columns of the image are reversed from left to right, effectively creating a mirror image of the original image.
        In other words, the method takes an image as input and returns the mirror image of the input image as output.
        """
        mirror_image = np.fliplr(image)
        plt.imsave(output_file, mirror_file)

    def crop_image(self, image,output_file, left=60, right= 60 , top= 60 , bottom = 60):
        """
        The crop_image method crops an input image by removing the specified number of pixels from the top, bottom, left, and right sides of the image.
        It takes the input image as a NumPy array and the values top, bottom, left, and right as parameters which represent the number of pixels to be removed from the respective sides of the image.
        It then creates a new NumPy array cropped_image by removing the specified number of pixels from each side of the input image using NumPy array slicing. Finally, it returns the cropped image as the output.
        """
        cropped_image = image[left:-right, top:-bottom, :]
        plt.imsave(output_file, crop_image)
        
    def resize_image(self, image, new_shape,output_file):
        """
        This method resizes an image to a new shape using NumPy. It creates a new image with the new shape and fills it with zeros.
        Then, for each pixel in the new image, it calculates the corresponding pixel in the original image using a simple scaling operation based on the ratios of the new and original image dimensions.
        Finally, it copies the color of the corresponding pixel from the original image to the new image. This process is repeated for all the pixels in the new image, resulting in the resized image.
        The resulting image may not be of exact size specified, but a close approximation based on the scaling operation.Resize an image to a new shape using NumPy.
        """
        resized_image = np.zeros(new_shape, dtype=image.dtype)
        height, width = new_shape[:2]
        original_height, original_width = image.shape[:2]
        for y in range(height):
            for x in range(width):
                orig_x = int(x * original_width / width)
                orig_y = int(y * original_height / height)
                resized_image[y, x] = image[orig_y, orig_x]
        plt.imsave(output_file, resized_image)
        
    def texture_effect(self, image, extent, output_file):
        """
        This method applies a texture effect to an image using NumPy. It takes in two parameters - the image to be processed and an extent value.
        First, the method calculates the texture value based on the extent parameter by multiplying it with 50.
        Then, using NumPy's where() method, the method creates a new array where values greater than 128 in the input image are replaced with the calculated texture value, and all other values are left unchanged.
        Finally, the resulting array is clipped between 0 and 255 (to ensure that all values are within the valid range for an image), and returned as an unsigned 8-bit integer array representing the processed image.Apply a texture effect to an image using NumPy.
        """
        texture = extent * 50 
        textured_image = np.where(image > 128, texture, image)
        textured_image = np.clip(textured_image, 0, 255).astype(np.uint8)
        plt.imsave(output_file, textured_image)
        
    def rotate_180(self, image, output_file):
        """
        The rotate_180 method rotates an input image by 180 degrees using the NumPy rot90 function.
        rot90 function is used to rotate an array by 90 degrees in the plane specified by axes. The first parameter specifies the input array that needs to be rotated.
        The second parameter k specifies the number of times the array needs to be rotated by 90 degrees, and it can be a negative or positive integer.
        In the rotate_180 method, the input image is rotated by 180 degrees, which is equivalent to rotating it two times by 90 degrees using rot90 function.
        The resulting rotated image is then returned by the method.Rotate an image by 180 degrees using NumPy."""
        rotated_image = np.rot90(image, 2)
        plt.imsave(output_file, rotated_image)

    def invert_image(self, image, output_file):
        """
        The invert_image() method takes an input image as a NumPy array and returns a new NumPy array with inverted colors.
        To invert the colors, the method subtracts each pixel value from 255 (the maximum possible pixel value in an 8-bit grayscale image).
        For example, if a pixel in the input image has a value of 100, the corresponding pixel in the inverted image will have a value of 155 (255-100=155).
        This process is repeated for each pixel in the image, resulting in an inverted image.Invert the colors of an image using NumPy."""
        inverted_image = 255 - image
        plt.imsave(output_file,inverted_image)
            
    def upside_down(self, image, output_file):
        """
        The flip_upside_down method takes an image as input and returns the same image flipped upside down. It uses the NumPy function np.flipud() to flip the rows of the input image along the vertical axis.
        This function reverses the order of rows in the array, effectively flipping the image vertically. The flipped image is then returned by the method.
        """
        flipped_image = np.flipud(image)
        plt.imsave(output_file, flipped_image)
        
    def blurred_image(self, image, extent, output_file):
        """
        This function takes an image and a value 'extent' as input, and applies Gaussian blurring to the image. The 'extent' parameter controls the extent of the blur effect. The larger the value of extent, the greater the extent of blurring applied to the image.
        The function first calculates the size of the kernel required for blurring based on the value of 'extent'. This is done by multiplying 3 times the extent value and then taking the next odd integer greater than that. This is because Gaussian kernels are usually odd-sized to ensure that they have a center pixel.
        Next, the function creates a 1D Gaussian kernel using the numpy library's 'exp' function. The kernel is generated by taking the exponential of the squared distance between each pixel in the kernel and the center pixel, divided by twice the square of the extent value.
        The kernel is then normalized by dividing each value by the sum of all values in the kernel.
        Then, the function applies the Gaussian kernel in two dimensions to the image using the numpy library's 'convolve' function. It applies the kernel to each row of the image, then applies it to each column of the resulting array. This is done using the numpy library's 'apply_along_axis' function.
        Finally, the blurred image is normalized and converted to an 8-bit unsigned integer format using the numpy library's 'clip' and 'astype' functions, respectively. The normalized image is then returned as the output of the function.
        """
        k_size = int(3 * extent) * 2 + 1
        k = np.exp(-np.arange(k_size)**2 / (2*extent**2))
        k = k / np.sum(k)
        blurred_image = np.apply_along_axis(lambda x: np.convolve(x, k, mode='same'), axis=0, arr=np.apply_along_axis(lambda x: np.convolve(x, k, mode='same'), axis=1, arr=image))
        blurred_image = np.clip(blurred_image, 0, 255).astype(np.uint8) # Add normalization step
        plt.imsave(output_file,blurred_image)

    def clockwise_rotatation(self, image, output_file):
        """
        The clock_rotate_image method takes an input image and rotates it by 90 degrees clockwise using NumPy.
        This is done using the rot90() function in NumPy, which rotates an array by 90 degrees in the plane specified by the two axes.
        The k argument in the rot90() function is used to specify the number of times the array is rotated by 90 degrees in the clockwise direction. In this case, k=-1 rotates the array by 90 degrees clockwise.
        """
        rotated_image = np.rot90(image, k=-1)
        plt.imsave(output_file, rotated_image)

    def anticlockwise_rotatation(self, image, output_file):
        """
        The anticlock_rotate_image method in the given code rotates an input image by 90 degrees anticlockwise using NumPy's rot90 function.
        The rot90 function is a NumPy method that rotates an array by 90 degrees in the counter-clockwise direction or k times (if k is provided as an argument).
        In this case, the input image is rotated by 90 degrees in the clockwise direction, which is equivalent to rotating it by 270 degrees in the counter-clockwise direction (i.e., k=-1).
        Here, the image argument is the input image that needs to be rotated, and the rotated_image variable is used to store the rotated image.
        The rotated image is then returned by the function.Rotate an image by 90 degrees clockwise using NumPy.
        """
        rotated_image = np.rot90(image,1)
        plt.imsave(output_file, rotated_image)
        
    def rotate_image_by_angle(self, image, angle, output_file):
        """
        This function rotate_image rotates an input image by a given angle in degrees using NumPy. It first converts the input angle to radians using the np.deg2rad() function. It then creates an output rotated_image array with the same shape as the input image using np.zeros_like().
        Next, it loops through each pixel in the input image and calculates its new position in the rotated image based on the rotation matrix formula
        where angle is the input angle in radians, x and y are the current pixel coordinates, mid_w and mid_h are the midpoints of the width and height of the input image, respectively.
        If the new pixel position is within the bounds of the input image, the corresponding pixel value is copied to the new position in the output image using rotated_image[y, x] = image[new_y, new_x].
        Finally, the function returns the rotated image.
        """
        angle_rad = np.deg2rad(angle)
        rotated_image = np.zeros_like(image)
        height, width= image.shape[:2]
        height_midpoint = height//2
        width_midpoint = width// 2
        for y in range(height):
            for x in range(width):
                new_x = int(np.cos(angle_rad) * (x - width_midpoint) + np.sin(angle_rad) * (y - height_midpoint) + width_midpoint)
                new_y = int(-np.sin(angle_rad) * (x - width_midpoint) + np.cos(angle_rad) * (y - height_midpoint) + width_midpoint)
                if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
                    rotated_image[y, x] = image[new_y, new_x]
        plt.imsave(output_file,rotated_image)
