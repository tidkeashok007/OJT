import cv2
import matplotlib.pyplot as plt

# Load the pre-trained classifier for frontal face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Upload an image for testing
image = cv2.imread('img.jpg')

# Convert the image to grayscale for the face detection model
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale(grey_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Print the number of faces detected
print(f"No of faces detected: {len(faces)}")

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Convert the image from BGR to RGB for displaying in Matplotlib
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image with detected faces
plt.imshow(img_rgb)
plt.axis("off")  # Turn off axis labels
plt.show()
