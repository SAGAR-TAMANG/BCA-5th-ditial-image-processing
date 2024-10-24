# And Wateshed Segmentation: 


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert to grayscale
image_path = "C:/Users/TAMANG/Downloads/IMG_5062.JPG"
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to smooth the image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform binary thresholding
_, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

# Finding sure background area
kernel = np.ones((3, 3), np.uint8)
sure_bg = cv2.dilate(thresh, kernel, iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Finding unknown region
unknown = cv2.subtract(sure_bg, np.uint8(sure_fg))

# Label markers
_, markers = cv2.connectedComponents(np.uint8(sure_fg))

# Add one to all the labels to distinguish unknown as 0
markers = markers + 1
markers[unknown == 255] = 0

# Apply the Watershed algorithm
image[markers == -1] = [255, 0, 0]  # Marking the boundaries in red
markers = cv2.watershed(image, markers)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Watershed Segmentation')
plt.imshow(markers, cmap='nipy_spectral')
plt.axis('off')

plt.show()