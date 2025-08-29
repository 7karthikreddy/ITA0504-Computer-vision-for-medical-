import cv2

# Try loading a Haar cascade (replace with watch_cascade.xml if you train one)
watch_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Check if cascade loaded properly
if watch_cascade.empty():
    print("Error: Cascade XML not loaded!")
    exit()

# Read the image
image = cv2.imread(r"D:\practice.jpg")

# Check if image loaded properly
if image is None:
    print("Error: Could not read image")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect objects
watches = watch_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.1, 
    minNeighbors=5, 
    minSize=(30, 30)
)

# Draw bounding boxes
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display result
cv2.imshow("Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
