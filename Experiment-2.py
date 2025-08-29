import cv2

# Correct way - use full path or raw string
image = cv2.imread("D:\practice.jpg")
 # change path

if image is None:
    print("Image not loaded. Check the path!")
else:
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow("Blurred", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print(image)
