# Sobel Edges

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load image
image_path = "C:/Users/TAMANG/Downloads/WhatsApp Image 2024-10-03 at 15.30.47_fa89c18e (1).jpg"
image = cv2.imread(image_path)

# Sobel Edge Detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow('Sobel Edges', sobel_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()