import cv2
import numpy as np

def pixelate_image(img, scale_percent):
  # Resize image
  width = int(img.shape[1] * scale_percent / 100)
  height = int(img.shape[0] * scale_percent / 100)
  dim = (width, height)
  resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

  # Resize back to original dimensions
  width = int(resized.shape[1] * 100 / scale_percent)
  height = int(resized.shape[0] * 100 / scale_percent)
  dim = (width, height)
  resized = cv2.resize(resized, dim, interpolation = cv2.INTER_NEAREST)

  # Convert to black and white
  _, thresh = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

  return thresh

# Capture video from camera
cap = cv2.VideoCapture(0)

while True:
  # Read a frame from the camera
  ret, frame = cap.read()

  # Convert to grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Pixelate the image
  pixelated_image = pixelate_image(gray, 10)  # Adjust scale_percent for desired pixelation level

  # Display the resulting frame
  cv2.imshow('frame', pixelated_image)

  # Exit if 'q' is pressed
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
