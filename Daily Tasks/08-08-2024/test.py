import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image with the particular library which we have imported
image = cv2.imread('test.png')

if image is None:
    print("Could not read the image")
    exit()

# Convert to greyscale
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(grey_image, (5, 5), 0)

# Apply Canny Edge Detection
edges = cv2.Canny(blurred_image, 100, 200)

# Apply Thresholding
_, thresholded_image = cv2.threshold(grey_image, 127, 255, cv2.THRESH_BINARY)

# Apply Dilation
kernel = np.ones((5,5), np.uint8)
dilated_image = cv2.dilate(thresholded_image, kernel, iterations=1)

# Apply Erosion
eroded_image = cv2.erode(thresholded_image, kernel, iterations=1)

# Display all images
plt.figure(figsize=(12, 10))

plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('Greyscale Image')
plt.imshow(grey_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('Blurred Image')
plt.imshow(blurred_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title('Edges')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title('Thresholded Image')
plt.imshow(thresholded_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title('Dilated Image')
plt.imshow(dilated_image, cmap='gray')
plt.axis('off')

plt.show()
