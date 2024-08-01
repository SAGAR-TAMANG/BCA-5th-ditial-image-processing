import cv2
import numpy as np

def rgb_hsi(image):
  # normalize the rgb value to the range [0, 1]
  image=  image / 255.0
  r, g, b = image[:, :, 0], image[:, :, 2], image[:, :, 2]

  # calculate intensity
  i = (r + g + b) / 3.0

  min_rgb = np.min(image, axis=2)

  # calculate saturation
  s = 1 - (3 / (r + g + b + 1e-10)) * min_rgb

  num = 0.5 * ((r - g) + (r - b))
  den = np.sqrt((r - g) ** 2 + (r - b) * (g - b))
  theta = np.arccos(num / (den + 1e-10))

  h = np.copy(b)
  h[b <= g] = theta[b <= g]
  h[b > g] = (2 * np.pi - theta)[b > g]

  h = h / (2 * np.pi)

  # combine the H, S, & I channels
  hsi_image = np.stack((h, s, i), axis=2)
  return hsi_image

image = cv2.imread('C:/Users/TAMANG/Documents/GitHub/Ditial-Image-Processing/July, 11th of July, 2024/brain_tumor.jpg')

hsi_image = rgb_hsi(image)

cv2.imshow('Image', hsi_image)
cv2.waitKey(0)
