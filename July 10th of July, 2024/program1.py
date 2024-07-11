# Brightness -> Luminance -> Brightness Channel

import cv2, numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:/Users/TAMANG/Documents/GitHub/Ditial-Image-Processing/July 10th of July, 2024/feynman.jpeg')

# Matrix
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50

# Image Vars
bright_image = cv2.add(image, brightness_matrix)
dark_image = cv2.subtract(image, brightness_matrix)

high_contrast_image = cv2.addWeighted(image, 2.2, brightness_matrix, 0, 0)
low_contrast_image = cv2.addWeighted(image, 0.5, brightness_matrix, 0, 0)

if image is None:
    print("Error: Could not read the image.")

# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.imshow('Image', bright_image)
# cv2.waitKey(0)
# cv2.imshow('Image', dark_image)
# cv2.waitKey(0)
cv2.imshow('Image', high_contrast_image)
cv2.waitKey(0)
cv2.imshow('Image', low_contrast_image)
cv2.waitKey(0)
# cv2.imshow('Image', image)

cv2.destroyAllWindows()