import numpy as np
import matplotlib.pyplot as plt
class IPAM1:
    def image_format(self, image):
        """
        This method converts an image to an array usinf matplotlib library.
        Input :- Image - .jpg
        Ouput :- Array
        """
        image_for = plt.imread(image)
        return image_for
    
    def grayscale(self, image,output_file):
        """
        This function finds the grayscale version of the input image.
        It uses the dot product of the input image with a set of weights [0.2989, 0.5870, 0.1140] to convert the RGB image to grayscale.
        This method converts an image to an array.
        Input :- Image - .jpg
        Ouput :- Array
        """
        red_coeff = 0.2989
        green_coeff = 0.5870
        blue_coeff = 0.1140

        red_chan = self.image_format(image)[:,:,0]
        green_chan = self.image_format(image)[:,:,1]
        blue_chan = self.image_format(image)[:,:,2]
        
        gray_red = red_chan * red_coeff
        gray_green = green_chan * green_coeff
        gray_blue = blue_chan * blue_coeff
        grays_image = gray_red+ gray_green + gray_blue
        # this imsave function is used to save the processed image
        plt.imsave(output_file, grays_image)
           
    def sepia_effect(self,image, output_file):
        """
        This function adds the sepia filter to the input image.
        Every row of the filter matrix represents a different color (red, green, and blue) 
        Input:-   Image - .jpg
                  Output_file- string
        
        """
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                                     [0.349, 0.686, 0.168],
                                     [0.272, 0.534, 0.131]])
        #creating an array with all zeros
        transposed_matrix = np.zeros_like(sepia_filter)
        print(transposed_matrix)
        for i in range(len(sepia_filter)):
            for j in range(len(sepia_filter[0])):
                transposed_matrix[j][i] = sepia_filter[i][j]
        print(transposed_matrix)
        sepia_image = np.dot(self.image_format(image),transposed_matrix)
        #clip function is used to normalize the image whereas astype for 8 bit 
        sepia_image = np.clip(sepia_image, 0,255).astype(np.uint8)
        #imsave function to save the processed file
        plt.imsave(output_file, sepia_image)
        
    def solarization(self, image, output_file,threshold=7):
        """
        The solarization method applies a solarization effect to an image.
        Input:-   Image - .jpg
                  Output_file- string
                  threshold - int ranging from(1 to 10)
        
        """
        #extent_index = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        #extent = [1,2,3,4,5,6,7,8,9]
        O_threshold = threshold * 30
        #if threshold in extent:
            #output_index = extend.index(threshold)
        #threshold
        solarized_image = np.where(image < O_threshold, image, 255 - image)
        solarized_image = np.clip(solarized_image, 0, 255).astype(np.uint8)
        #imsave function to save the processed file
        plt.imsave(output_file, solarized_image)
   
    def color_filter(self, image,output_file, color = "red"):
        """
        The color_filter method applies a custom color filter to an input image based on the specified color. 
        Input:-   Image - .jpg
                  Output_file- string
                  Extent - string out of ("red", "green", "blue")
        """
        #creating an empty list
        color_list =[]
        if color.upper() == "RED":
            color_list.append(1.0)
            color_list.append(0.0)
            color_list.append(0.0)

        elif color.upper() == "GREEN":
            color_list.append(0.0)
            color_list.append(1.0)
            color_list.append(0.0)
        elif color.upper() == "BLUE":
            color_list.append(0.0)
            color_list.append(0.0)
            color_list.append(1.0)
        else:
            return("Invalid Color")
        #zeros_likes creates a new array of zeros with the desired shape
        filtered_image = np.zeros_like(self.image_format(image))
        filtered_image[:,:,0] = self.image_format(image)[:,:,0] * color_list[0] # Red channel
        filtered_image[:,:,1] = self.image_format(image)[:,:,1] * color_list[1] # Green channel
        filtered_image[:,:,2] = self.image_format(image)[:,:,2] * color_list[2] # Blue channel
        #clip function is used to limit values in an array between a minimum and maximum value
        #astype function is used to cast an array to a new data type
        filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
        #imsave function to save the processed file
        plt.imsave(output_file, filtered_image)
        
    def vignette_effect(self,image,output_file,extent=5 ):
        """
        This method applies a vignette effect to an input image.
        The extent parameter controls the strength of the effect, with a larger value resulting in a more pronounced vignette
        Input:-   Image - .jpg
                  Output_file- string
                  Extent - int ranging from(1 to 10)
        """
        if extent < 1:
            extent = 1
        elif extent > 10:
            extent = 10
        power = extent / 2
        #indices function to create an array of indices that can be used to index into multi-dimensional arrays
        y, x = np.indices(self.image_format(image).shape[:2])
        center_y, center_x = self.image_format(image).shape[0] // 2, self.image_format(image).shape[1] // 2
        # the square root of the input array(sqrt)
        distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        max_distance = np.sqrt(center_x ** 2 + center_y ** 2)
        vignette = 1 - (distance / max_distance) ** power
        #clip function is used to limit values in an array between a minimum and maximum value
        vignette = np.clip(vignette, 0, 1)
        size = int(np.round(2 + extent / 10 * (self.image_format(image).shape[0] - 2)))
        kernel = np.ones((size, size), np.uint8)
        filtered_image = np.zeros_like(self.image_format(image))
        for c in range(self.image_format(image).shape[2]):
            filtered_image[:,:,c] = np.minimum(self.image_format(image)[:,:,c], np.abs(np.fft.ifft2(np.fft.fft2(self.image_format(image)[:,:,c]) * np.fft.fft2(kernel, s=self.image_format(image).shape[:2]))))
        vignette_image = filtered_image * vignette[..., np.newaxis]
        #clip function is used to limit values in an array between a minimum and maximum value
        #astype function is used to cast an array to a new data type
        vignette_image = np.clip(vignette_image, 0, 255).astype(np.uint8)
        #imsave function to save the processed file
        plt.imsave(output_file, vignette_image)
        
    def brightness_adjustment(self, image,output_file,extent=10):
        """
        This method takes an image array and an extent parameter as input. The extent parameter specifies the brightness level of the output image.
        The method then computes a bright_image by adding the extent multiplied by 2/5 to the input image array.
        Input:-   Image - .jpg
                  Output_file- string
                  Extent - int
        """
        brightness = extent * 2/5
        bright_image = np.clip(self.image_format(image) + brightness, 0, 255).astype(np.uint8)
        #imsave function to save the processed file
        plt.imsave(output_file, bright_image)

