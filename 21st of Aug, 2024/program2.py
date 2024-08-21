import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load a grayscale image

image_path = "C:/Users/TAMANG/Downloads/WhatsApp Image 2024-07-23 at 13.58.18_8a37fc20 (1).png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
hist, bins = np.histogram(image.flatten(), 256, [0, 256])

# Calculate the CDF
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# Apply histogram equalization
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())* 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

# Map the original image through the CDF
image_equalized = cdf[image]

# Display results
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(image_equalized, cmap='gray'), plt.title('Equalized Image')
plt.show()

