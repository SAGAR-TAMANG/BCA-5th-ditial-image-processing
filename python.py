import cv2
import requests
import numpy as np

# Image URL
url = "https://instagram.fgau1-5.fna.fbcdn.net/v/t51.2885-19/448879601_2210137209322158_930178855523273684_n.jpg?_nc_ht=instagram.fgau1-5.fna.fbcdn.net&_nc_cat=106&_nc_ohc=1nFtwQDwezYQ7kNvgEawoV6&edm=AEhyXUkBAAAA&ccb=7-5&oh=00_AYAJMWQ_BAmaXe4uyCaC-hAdmjgtRf0-vDf44yAuT6mvjQ&oe=668C3583&_nc_sid=8f1549"

# Download the image
response = requests.get(url)
image_array = np.frombuffer(response.content, np.uint8)
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# Show the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
