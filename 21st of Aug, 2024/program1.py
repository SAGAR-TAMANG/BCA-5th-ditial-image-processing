import numpy as np
import matplotlib.pyplot as plt
import cv2

image_path = "C:/Users/TAMANG/Downloads/WhatsApp Image 2024-07-23 at 13.58.18_8a37fc20 (1).png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(image.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')

plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Histogram of Equalized Image')

plt.tight_layout()
plt.show()


