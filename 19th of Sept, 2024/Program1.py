import cv2
import numpy as np
import random

# Load a sample image
image_path = "C:/Users/TAMANG/Downloads/Architectural-detail-of-marble-Corinthian-order-columns-scaled (1).jpg"
image = cv2.imread(image_path, 0)  # Load as grayscale

# Function to add Gaussian noise
def add_gaussian_noise(image):
    mean = 0
    std = 25
    gaussian_noise = np.random.normal(mean, std, image.shape)
    noisy_image = image + gaussian_noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

# Function to add Salt-and-Pepper noise
def add_salt_and_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy_image = np.copy(image)
    num_salt = np.ceil(salt_prob * image.size)
    num_pepper = np.ceil(pepper_prob * image.size)

    # Add Salt noise
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255

    # Add Pepper noise
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0

    return noisy_image

# Function to add Poisson noise
def add_poisson_noise(image):
    noisy_image = np.random.poisson(image * 255.0) / 255.0
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

# Function to add Speckle noise
def add_speckle_noise(image):
    noise = np.random.randn(*image.shape)
    noisy_image = image + image * noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

# Apply each noise type to the image
gaussian_noise_image = add_gaussian_noise(image)
salt_and_pepper_noise_image = add_salt_and_pepper_noise(image)
poisson_noise_image = add_poisson_noise(image)
speckle_noise_image = add_speckle_noise(image)

# Display the images
cv2.imshow('Original', image)
cv2.imshow('Gaussian Noise', gaussian_noise_image)
cv2.imshow('Salt-and-Pepper Noise', salt_and_pepper_noise_image)
cv2.imshow('Poisson Noise', poisson_noise_image)
cv2.imshow('Speckle Noise', speckle_noise_image)

# Wait until a key is pressed, then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
