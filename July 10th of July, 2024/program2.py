# Contrast -> Difference between the objects -> or Difference in lumninance or coor that makes an object distinguishable from others within the same field of view.

import cv2, numpy as np

image = cv2.imread('C:/Users/TAMANG/Documents/GitHub/Ditial-Image-Processing/July 10th of July, 2024/feynman.jpeg')

# Matrix
brightness_matrix = np.ones(image.shape, dtype="uint8") * 100

# Image Vars
bright_image = cv2.add(image, brightness_matrix)
dark_image = cv2.subtract(image, brightness_matrix)

if image is None:
  print("Error: Could not read the image.")

cv2.imshow('Image', image)
cv2.waitKey(0)
