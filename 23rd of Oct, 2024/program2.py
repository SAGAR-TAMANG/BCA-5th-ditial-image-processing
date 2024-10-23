
import cv2
import numpy as np

# Load the Lenna image 
image_path = "C:/Users/TAMANG/Downloads/WhatsApp Image 2024-10-03 at 15.30.47_fa89c18e (1).jpg"
image = cv2.imread(image_path)

# Zooming effect (crop and resize) 
height, width image.shape[:2] 
zoom_factor = 1.5

# Calculate the center of the image 
center_x, center_y = int(width / 2), int(height / 2)
new_width, new_height = int(width / zoom_factor), int(height / zoom_factor)
# Crop the center region of the image x1,y1 = center_x - new_width // 2, center_y- new_height // 2
x2, y2 = center_x + new_width // 2, center_y + new_height // 2
=
zoomed_image image[y1:y2, x1:x2]
# Resize back to original size
zoomed_image = cv2.resize(zoomed_image,
(width, height))
# Blurring effect (Gaussian Blur)
blurred_image = cv2.GaussianBlur(image, (15.15) 0)


# Calculate the center of the image
center_x, center_y= int(width / 2), int(height/ 2)
new_width, new_height = int(width / zoom_factor), int(height / zoom_factor)
# Crop the center region of the image
x1,y1 = center_x - new_width // 2, center_y - new_height // 2
x2, y2 = center_x + new_width // 2, center_y+ new_height // 2
zoomed_image = image[y1:y2, x1:x2]
# Resize back to original size
zoomed_image = cv2.resize(zoomed_image,
(width, height))
# Blurring effect (Gaussian Blur) blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Zoomed Image', zoomed_image) cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()