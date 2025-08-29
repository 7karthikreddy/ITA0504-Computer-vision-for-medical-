import cv2

def detect_smile(image_path):
    # Load pre-trained Haar cascades for face and smile detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("❌ Error: Could not read image:", image_path)
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]  # Extract face region

        # Detect smiles inside face
        smiles = smile_cascade.detectMultiScale(
            face_roi,
            scaleFactor=1.8,
            minNeighbors=20,
            minSize=(25, 25)
        )

        # Draw bounding boxes around smiles
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(image, (x + sx, y + sy + int(h/2)), (x + sx + sw, y + sy + sh + int(h/2)), (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Smile Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
detect_smile(r"D:\smile.jpg")   # use raw string for Windows path
