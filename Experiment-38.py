import cv2

def count_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("❌ Error: Could not load image. Check the path:", image_path)
        return 0

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar cascade face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Count faces
    face_count = len(faces)
    print(f"✅ Number of faces detected: {face_count}")

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show image
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return face_count


# Example usage
image_path = r"D:\smile.jpg"  # ✅ fixed path
count_faces(image_path)
