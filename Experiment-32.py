import numpy as np
import cv2

def create_colored_corners(image_size):
    height, width = image_size  # Extract height and width

    # Create a white image (3D array of ones scaled to 255 for RGB)
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate the size of the colored boxes (1/10th of image size)
    box_h, box_w = height // 10, width // 10

    # Define corner regions and their colors
    image[:box_h, :box_w] = [0, 0, 0]       # Top-left (Black)
    image[:box_h, -box_w:] = [255, 0, 0]    # Top-right (Blue)
    image[-box_h:, :box_w] = [0, 255, 0]    # Bottom-left (Green)
    image[-box_h:, -box_w:] = [0, 0, 255]   # Bottom-right (Red)

    # Display the image
    cv2.imshow("Colored Corners Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))
create_colored_corners((user_height, user_width))
