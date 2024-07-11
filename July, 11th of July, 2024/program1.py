import cv2, numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/TAMANG/Documents/GitHub/Ditial-Image-Processing/July, 11th of July, 2024/brain_tumor.jpg")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)

plt.imshow(image_rgb)
plt.title("Original Image")
# plt.axis('off')
plt.show()

blue_channel, green_channel, red_channel = cv2.split(image)

fig, axes = plt.subplots(1, 3, figsize = (15, 5))
axes[0].imshow(blue_channel, cmap='gray')
axes[0].set_title('Blue Channel')
axes[0].axis('off')

axes[1].imshow(green_channel, cmap='gray')
axes[1].set_title('Green Channel')
axes[1].axis('off')

axes[2].imshow(red_channel, cmap='gray')
axes[2].set_title('Red Channel')
axes[2].axis('off')

plt.show()
# axes[0].imshow(blue_channel, cmap='gray')