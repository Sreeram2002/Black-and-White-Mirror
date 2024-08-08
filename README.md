# Black-and-White-Mirror

This Python script captures live video from a webcam, converts it to grayscale, applies a pixelation effect, and then converts it to a black and white image. The resulting pixelated image is displayed in real-time.

Dependencies:

OpenCV (cv2)
NumPy (np)
Usage:

Install the required dependencies using pip install opencv-python numpy.
Save the code as a Python file (e.g., pixelate_webcam.py).
Run the script from your terminal: python pixelate_webcam.py.
A window will appear showing the pixelated webcam feed. Press 'q' to quit.
Customization:

Pixelation level: Adjust the scale_percent parameter in the pixelate_image function to control the level of pixelation.
Black and white threshold: Modify the threshold value in the cv2.threshold function to adjust the black and white balance.
Note: This script requires a webcam connected to your system.
