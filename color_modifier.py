import numpy as np
import matplotlib.pyplot as plt
class IPAM:

    def grayscale(self, image,output_file):
        """
        The grayscale function takes an input image as a NumPy array and returns a grayscale version of that image. The function uses the dot product of the input image with a set of weights [0.2989, 0.5870, 0.1140] to convert the RGB image to grayscale. These weights are used to determine how much weight to assign to each of the red, green, and blue channels when converting to grayscale.
        The dot product of the input image and the weight matrix gives a new image where each pixel value is a weighted average of the R, G, and B values of the corresponding pixel in the original image.
        The resulting grayscale image has only one channel instead of three channels for red, green, and blue.
        """
        red_coeff = 0.2989
        green_coeff = 0.5870
        blue_coeff = 0.1140

        red_chan = image[:,:,0]
        green_chan = image[:,:,1]
        blue_chan = image[:,:,2]
        
        gray_red = red_chan * red_coeff
        gray_green = green_chan * green_coeff
        gray_blue = blue_chan * blue_coeff
        grays_image = gray_red+ gray_green + gray_blue
        plt.imsave(output_file, grays_image)
           
    def sepia(self,image, output_file):
        """
        The function first defines a 3x3 sepia filter matrix, which consists of floating-point values ranging from 0 to 1. Each row of the filter matrix represents a different color channel (red, green, and blue) and the columns correspond to the intensity of that channel.
        Next, the function applies the filter matrix to the image by matrix multiplication, using the numpy library's 'dot' function. Specifically, it multiplies the image matrix by the transpose of the sepia filter matrix. This is done to ensure that each pixel in the image is multiplied by the correct coefficients in the filter matrix.
        The resulting sepia image is then normalized using the numpy library's 'clip' function to ensure that all values are between 0 and 255, the range for an 8-bit unsigned integer. Any values below 0 are set to 0 and any values above 255 are set to 255.
        Finally, the image is converted to an 8-bit unsigned integer format using the numpy library's 'astype' function and returned as the output of the function.
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
        sepia_image = np.dot(image,transposed_matrix)
        sepia_image = np.clip(sepia_image, 0,255).astype(np.uint8)
        plt.imsave(output_file, sepia_image)

    
    def solarization(self, image, threshold, output_file):
        """
        The solarization method applies a solarization effect to an image using the NumPy library. Solarization is a technique in photography where the image tones are inverted, creating a dramatic effect.
        The method takes two parameters - image and threshold. The image parameter is the input image that needs to be solarized. The threshold parameter is the cutoff point that determines which pixel values in the image should be inverted.
        Inside the method, the O_threshold variable is calculated by multiplying the threshold parameter with 30. Then, using NumPy's where function, the method checks if each pixel in the input image is less than the O_threshold value. If the pixel value is less than O_threshold, then that pixel value is kept as is in the output solarized_image. Otherwise, the pixel value is inverted by subtracting it from 255. Finally, the output solarized_image is clipped to the range of 0 to 255 and returned as a NumPy array of unsigned integers.
        """
        #extent_index = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        #extent = [1,2,3,4,5,6,7,8,9]
        O_threshold = threshold * 30
        #if threshold in extent:
            #output_index = extend.index(threshold)
        #threshold
        solarized_image = np.where(image < O_threshold, image, 255 - image)
        solarized_image = np.clip(solarized_image, 0, 255).astype(np.uint8)
        plt.imsave(output_file, solarized_image)
   
    def color_filter(self, image, color, output_file):
        """
        The color_filter method applies a custom color filter to an input image based on the specified color. The method takes in two parameters - the input image and the color to be filtered.
        First, the method initializes an empty list called color_list. Then, based on the specified color, the method appends the appropriate RGB color values to color_list. For example, if the color is "RED", the method appends [1.0, 0.0, 0.0] to color_list (which represents full red, no green, and no blue).
        Next, the method creates a new array called filtered_image, which is the same shape as the input image. The method then applies the custom color filter to filtered_image by multiplying each color channel of the input image by the corresponding value in color_list. For example, if the color is "RED", the method multiplies the red channel of the input image by 1.0 and sets the green and blue channels to 0.0.
        `Finally, the resulting filtered_image is clipped between 0 and 255 (to ensure that all values are within the valid range for an image), and returned as an unsigned 8-bit integer array representing the processed image.Apply a custom color filter to an image using NumPy."""
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
            
        filtered_image = np.zeros_like(image)
        filtered_image[:,:,0] = image[:,:,0] * color_list[0] # Red channel
        filtered_image[:,:,1] = image[:,:,1] * color_list[1] # Green channel
        filtered_image[:,:,2] = image[:,:,2] * color_list[2] # Blue channel
        filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
        plt.imsave(output_file, filtered_image)
        
    def apply_vignette_effect(self,image, extent, output_file):
        """
        The apply_vignette_effect method applies a vignette effect to an input image.
        The extent parameter controls the strength of the effect, with a larger value resulting in a more pronounced vignette.
        The method first computes the distance of each pixel from the center of the image, and computes a vignette mask based on a power function of the distance.
        The mask is then clipped between 0 and 1. The method then applies a variable size filter to the input image using the extent parameter, and multiplies the filtered image with the vignette mask. The resulting image is then clipped between 0 and 255, and converted to a uint8 data type before being returned. The vignette effect darkens the image at the edges, creating a circular or oval shaped fade-out effect that draws the viewer's attention towards the center of the image.
        """
        if extent < 1:
            extent = 1
        elif extent > 10:
            extent = 10
        power = extent / 2
        y, x = np.indices(image.shape[:2])
        center_y, center_x = image.shape[0] // 2, image.shape[1] // 2
        distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        max_distance = np.sqrt(center_x ** 2 + center_y ** 2)
        vignette = 1 - (distance / max_distance) ** power
        vignette = np.clip(vignette, 0, 1)
        size = int(np.round(2 + extent / 10 * (image.shape[0] - 2)))
        kernel = np.ones((size, size), np.uint8)
        filtered_image = np.zeros_like(image)
        for c in range(image.shape[2]):
            filtered_image[:,:,c] = np.minimum(image[:,:,c], np.abs(np.fft.ifft2(np.fft.fft2(image[:,:,c]) * np.fft.fft2(kernel, s=image.shape[:2]))))
        vignette_image = filtered_image * vignette[..., np.newaxis]
        vignette_image = np.clip(vignette_image, 0, 255).astype(np.uint8)
        plt.imsave(output_file, vignette_image)

    
    def bright_image(self, image,output_file,extent=1):
        """
        This method takes an image array and an extent parameter as input. The extent parameter specifies the brightness level of the output image.
        The method then computes a bright_image by adding the extent multiplied by 2/5 to the input image array.
        This value is clipped between 0 and 255 to ensure that the output image has pixel values within the valid range of 0 to 255. Finally, the method returns the bright_image array with dtype np.uint8.
        Overall, this method increases the brightness level of an image by adding a constant value to all pixel values.
        """
        brightness = extent * 2/5
        bright_image = np.clip(image + brightness, 0, 255).astype(np.uint8)
        plt.imsave(output_file, bright_image)


