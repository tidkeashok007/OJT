import cv2
import matplotlib.pyplot as plt

# Load an image using OpenCV
image_path = "images.jpg"
image_cv2 = cv2.imread(image_path)

# Convert the image from BGR to RGB
image_cv2_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(image_cv2)
plt.title('Image loaded with OpenCV')
plt.show()

from PIL import Image
# Load an image using PIL
image_pil = Image.open(image_path)

# Display the image
plt.imshow(image_pil)
plt.title('Image loaded with PIL')
plt.show()

import imageio
# Load an image using imageio
image_imageio = imageio.imread(image_path)
# Display the image
plt.imshow(image_imageio)
plt.title('Image loaded with imageio')
plt.show()
# PNG image path
image_path_png = "images.jpg"
image_path_jpg = "images.jpg"


# OpenCV
image_cv2_png = cv2.imread(image_path_png)
image_cv2_png_rgb = cv2.cvtColor(image_cv2_png, cv2.COLOR_BGR2RGB)
plt.imshow(image_cv2_png_rgb)
plt.title('PNG loaded with OpenCV')
plt.show()

# PIL
image_pil_png = Image.open(image_path_png)
plt.imshow(image_cv2_png_rgb)
plt.title('PNG loaded with OpenCV')
plt.show()

# imageio
image_imageio_png = imageio.imread(image_path_png)
plt.imshow(image_cv2_png_rgb)
plt.title('PNG loaded with OpenCV')
plt.show()