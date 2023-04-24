import numpy as np 
import matplotlib.pyplot as plt
class IPAM:
    def image_format(self, image):
        """
        This method converts an image to an array.
        Input :- Image - .jpg
        Ouput :- Array
        """
        # imread() method for reading a image
        image_for = plt.imread(image)
        return image_for

    def mirror_image(self, image,output_file):
        """
        This method finds the mirror image of a given image using NumPy's fliplr() function.
        Input :- Image - .jpg
        Output_file - string

        """
        #fliplr() function is used to flip the image along the vertical axis.
        mirror_image = np.fliplr(self.image_format(image))
        plt.imsave(output_file, mirror_image)

    def crop_image(self, image,output_file, left=60, right= 60 , top= 60 , bottom = 60):
        """
        This method crops an input image by removing the desired pixels from all the directions along the edges .
        It takes the input as an image and the values top, bottom, left, and right as parameters which represent the number of pixels to be removed from the respective sides of the image.
        Input:-   Image - .jpg
                    Output_file - string
                    left- int
                    right - int
                    top - int
                    bottom - int
        
        """
        cropped_image = self.image_format(image)[left:-right, top:-bottom, :]
        plt.imsave(output_file, cropped_image)
                
    def texture_effect(self, image, output_file, extent=7 ):
        """
        This method applies a texture effect to an image using NumPy.
        The resulting array is clipped between 0 and 255 and returned as an unsigned 8-bit integer array representing the processed image.
        Input:-   Image - .jpg
                    Output_file- string
                    Extent - int
        """
        texture = extent * 50
        # where() method creates a new array where values greater than 128 in the input image are replaced with the calculated texture value, and all other values are left unchanged.
        textured_image = np.where(self.image_format(image) > 128, texture, self.image_format(image))
        textured_image = np.clip(textured_image, 0, 255).astype(np.uint8)
        plt.imsave(output_file, textured_image)
        
    def rotate_180(self, image, output_file):
        """
        This method rotates an input image by 180 degrees using the NumPy rot90 function.
        s.
        This function rotates the image twice by 90 degrees using rot90 function. which results in a 180 degree rotation.
        Input:-   Image - .jpg
                    Output_file- string
        """
        #rot90 function is used to rotate an array by 90 degrees in the plane specified by axe
        rotated_image = np.rot90(self.image_format(image), 2)
        plt.imsave(output_file, rotated_image)

    def invert_image(self, image, output_file):
        """
        This method inverts an input image by subtracting each pixel value from 255 (the maximum possible pixel value in an 8-bit grayscale image).
        Input:-   Image - .jpg
                    Output_file- string
       """
        inverted_image = 255 - self.image_format(image)
        plt.imsave(output_file,inverted_image)
            
    def upside_down(self, image, output_file):
        """
        This method takes an image as input and flips it upside down
        This function reverses the order of rows in the array, effectively flipping the image vertically
                Input:-   Image - .jpg
                            Output_file- string
        """
        #Function np.flipud() used to flip the rows of the input image along the vertical axis
        flipped_image = np.flipud(self.image_format(image))
        plt.imsave(output_file, flipped_image)
        
    def blurred_image(self, image, output_file, extent=7):
        """
        This function takes an image and a value extentnas input, and applies Gaussian blurring to the image. The extent parameter controls the extent of the blur effect.
        The larger value of extent, the greater the extent of blurring applied to the image.
        Input:-   Image - .jpg
                    Output_file- string
                    Extent - int
        """
        k_size = int(3 * extent) * 2 + 1
        # the exp function creates a 1D Gaussian kernel.
        k = np.exp(-np.arange(k_size)**2 / (2*extent**2))
        k = k / np.sum(k)
        #the convolve function applies the Gaussian kernel in two dimensions to the image.
        blurred_image = np.apply_along_axis(lambda x: np.convolve(x, k, mode='same'), axis=0, arr=np.apply_along_axis(lambda x: np.convolve(x, k, mode='same'), axis=1, arr=self.image_format(image)))
        #the blurred image is normalized and converted to an 8-bit unsigned integer format using clip and astype functions
        blurred_image = np.clip(blurred_image, 0, 255).astype(np.uint8) 
        plt.imsave(output_file,blurred_image)

    def clockwise_rotation(self, image, output_file):
        """
        This method takes an input image and rotates it by 90 degrees clockwise using NumPy.
        Input:-   Image - .jpg
                    Output_file- string
        """
        # rot90() function rotates an array by 90 degrees which is equal to rotating it counter clockwise by 270 degrees thats why k equals to -1
        rotated_image = np.rot90(self.image_format(image), k=-1)
        plt.imsave(output_file, rotated_image)

    def anticlockwise_rotation(self, image, output_file):
        """
        This method rotates an input image by 90 degrees anticlockwise using NumPy's rot90 function.
        Input:-   Image - .jpg
                    Output_file- string
        """
        # rot90() function rotates an array by 90 degrees 
        rotated_image = np.rot90(self.image_format(image),1)
        plt.imsave(output_file, rotated_image)
