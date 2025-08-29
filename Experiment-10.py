import cv2
# Load the image
img = cv2.imread("D:\practice.jpg")
# Rotate 90 degrees clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# Display the rotated image
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
