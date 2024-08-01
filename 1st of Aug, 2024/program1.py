import numpy as np
import matplotlib.pyplot as plt
import cv2

def display_image(image, title='Image'):
  plt.figure(figsize=(5, 5))
  plt.imshow(image, cmap='gray')
  plt.title(title)
  plt.axis('off')
  plt.show()

image_path = "C:/Users/TAMANG/Downloads/WhatsApp Image 2024-07-23 at 13.58.18_8a37fc20 (1).png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

display_image(image, title='Original Image')

dct_image = cv2.dct(np.float32(image))

display_image(np.log(np.abs(dct_image)), title='DCT Transformer Image')

idct_image = cv2.idct(dct_image)

display_image(idct_image, title='Reconstructed Image from DCT')

cv2.imwrite('dct_transformed.jpg', dct_image)
cv2.imwrite('reconstructed_image.jpg', idct_image)