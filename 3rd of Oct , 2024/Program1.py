import cv2
import numpy as np

image_path = "C:/Users/TAMANG/Downloads/WhatsApp Image 2024-10-03 at 15.30.47_fa89c18e (1).jpg"
img = cv2.imread(image_path)

# Linear Filters

# 1. Gaussian Blur (Smoothing)
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
# 2. Median Blur (Noise Reduction)
median_blur = cv2.medianBlur(img, 5)
# 3. Bilateral Filter (Edge-Preserving Smoothing)
bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)

# Non-Linear Filters

# 4. Unsharp Masking (Sharpening)
blurred = cv2.GaussianBlur(img, (0, 0), 3)
sharpened = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)
# 5. Non-Local Means Denoising
nl_means_denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# Display the results
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Filter", bilateral_filter)
cv2.imshow("Sharpened (Unsharp Masking)", sharpened)
cv2.imshow("Non-Local Means Denoised", nl_means_denoised)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
