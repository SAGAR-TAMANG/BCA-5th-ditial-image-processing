import numpy as np
import matplotlib.pyplot as plt
import cv2

def display_image(image, title='Image'):
  plt.figure(figsize=(5, 5))
  plt.imshow(image, cmap='gray')
  plt.title(title)
  plt.axis('off')
  plt.show()

image_path = "C:/Users/TAMANG/Downloads/img2.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.plot(hist)
plt.xlabel('Histogram')
plt.xlabel('Pizel Intesity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()