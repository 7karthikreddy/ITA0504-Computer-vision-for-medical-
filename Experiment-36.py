import cv2
import numpy as np

def subtract_background(image_path, lower_color, upper_color):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("❌ Error: Could not read image:", image_path)
        return

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper range for background color
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask for background removal
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert mask to keep the foreground
    mask_inv = cv2.bitwise_not(mask)

    # Extract the foreground
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Subtracted Image", foreground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage (adjust color range as needed)
image_path = r"C:\Users\yogiy\OneDrive\Pictures\hq720.jpg"  # ✅ fixed path
lower_color = [30, 30, 30]   # Example lower bound (adjust as needed)
upper_color = [255, 255, 255]  # Example upper bound (adjust as needed)

subtract_background(image_path, lower_color, upper_color)
