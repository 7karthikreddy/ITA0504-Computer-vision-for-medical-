import cv2
import numpy as np
def subtract_foreground(image_path, lower_color, upper_color):
    # Read the image
    image = cv2.imread(image_path)
    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Define lower and upper range for foreground color (adjust as needed)
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)
    # Create mask to remove foreground
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    # Extract the background
    background = cv2.bitwise_and(image, image, mask=mask)
    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Subtracted Image (Only Background)", background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Example usage (adjust color range as needed)
image_path = "D:\practice.jpg"  # Replace with the actual image path
lower_color = [0, 50, 50]   # Example lower bound for foreground color (adjust as needed)
upper_color = [120, 255, 255]  # Example upper bound for foreground color (adjust as needed)
subtract_foreground(image_path, lower_color, upper_color)
