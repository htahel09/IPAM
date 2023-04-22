class IPAM:
    def bright_image(self, image,extent=1):
        """
        This method takes an image array and an extent parameter as input. The extent parameter specifies the brightness level of the output image.
        The method then computes a bright_image by adding the extent multiplied by 2/5 to the input image array.
        This value is clipped between 0 and 255 to ensure that the output image has pixel values within the valid range of 0 to 255. Finally, the method returns the bright_image array with dtype np.uint8.
        Overall, this method increases the brightness level of an image by adding a constant value to all pixel values.
        """
        brightness = extent * 2/5
        bright_image = np.clip(image + brightness, 0, 255).astype(np.uint8)
        return bright_image
    def mirror_image(self, image):
        """
        The find_mirror_image() method finds the mirror image of a given image using NumPy's fliplr() function.
        NumPy's fliplr() function is used to flip the image along the vertical axis i.e., the columns of the image are reversed from left to right, effectively creating a mirror image of the original image.
        In other words, the method takes an image as input and returns the mirror image of the input image as output.
        """
        mirror_image = np.fliplr(image)
        return mirror_image

    def crop_image(self, image, left=30, right= 30 , top= 30 , bottom = 30):
        """
        The crop_image method crops an input image by removing the specified number of pixels from the top, bottom, left, and right sides of the image.
        It takes the input image as a NumPy array and the values top, bottom, left, and right as parameters which represent the number of pixels to be removed from the respective sides of the image.
        It then creates a new NumPy array cropped_image by removing the specified number of pixels from each side of the input image using NumPy array slicing. Finally, it returns the cropped image as the output.
        """
        cropped_image = image[left:-right, top:-bottom, :]
        return cropped_image

   
    def resize_image(self, image, new_shape):
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
        return resized_image
    def texture_effect(self, image, extent):
        """
        This method applies a texture effect to an image using NumPy. It takes in two parameters - the image to be processed and an extent value.
        First, the method calculates the texture value based on the extent parameter by multiplying it with 50.
        Then, using NumPy's where() method, the method creates a new array where values greater than 128 in the input image are replaced with the calculated texture value, and all other values are left unchanged.
        Finally, the resulting array is clipped between 0 and 255 (to ensure that all values are within the valid range for an image), and returned as an unsigned 8-bit integer array representing the processed image.Apply a texture effect to an image using NumPy.
        """
        texture = extent * 50 
        textured_image = np.where(image > 128, texture, image)
        textured_image = np.clip(textured_image, 0, 255).astype(np.uint8)
        return textured_image
    def rotate_180(self, image):
        """
        The rotate_180 method rotates an input image by 180 degrees using the NumPy rot90 function.
        rot90 function is used to rotate an array by 90 degrees in the plane specified by axes. The first parameter specifies the input array that needs to be rotated.
        The second parameter k specifies the number of times the array needs to be rotated by 90 degrees, and it can be a negative or positive integer.
        In the rotate_180 method, the input image is rotated by 180 degrees, which is equivalent to rotating it two times by 90 degrees using rot90 function.
        The resulting rotated image is then returned by the method.Rotate an image by 180 degrees using NumPy."""
        rotated_image = np.rot90(image, 2)
        return rotated_image

    def invert_image(self, image):
        """
        The invert_image() method takes an input image as a NumPy array and returns a new NumPy array with inverted colors.
        To invert the colors, the method subtracts each pixel value from 255 (the maximum possible pixel value in an 8-bit grayscale image).
        For example, if a pixel in the input image has a value of 100, the corresponding pixel in the inverted image will have a value of 155 (255-100=155).
        This process is repeated for each pixel in the image, resulting in an inverted image.Invert the colors of an image using NumPy."""
        inverted_image = 255 - image
        return inverted_image
