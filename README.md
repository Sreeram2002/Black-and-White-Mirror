# Black-and-White-Mirror

This Python script captures live video from a webcam, converts it to grayscale, applies a pixelation effect, and then converts it to a black and white image. The resulting pixelated image is displayed in real-time.

Dependencies: OpenCV (cv2), NumPy (np)

Usage:

1. Install the required dependencies using pip install opencv-python numpy.
2. Save the code as a Python file (e.g., pixelate_webcam.py).
3. Run the script from your terminal: python pixelate_webcam.py.
4. A window will appear showing the pixelated webcam feed. Press 'q' to quit.
5. Customization:

Pixelation level: Adjust the scale_percent parameter in the pixelate_image function to control the level of pixelation.

Black and white threshold: Modify the threshold value in the cv2.threshold function to adjust the black and white balance.

Note: This script requires a webcam connected to your system.
