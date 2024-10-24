import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "C:/Users/TAMANG/Downloads/IMG_5062.JPG"
image = cv2.imread(image_path)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, thresh_binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Apply adaptive thresholding
thresh_adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Binary Thresholding')
plt.imshow(thresh_binary, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Adaptive Thresholding')
plt.imshow(thresh_adaptive, cmap='gray')
plt.axis('off')

plt.show()