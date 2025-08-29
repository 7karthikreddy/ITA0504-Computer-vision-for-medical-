import cv2
import os
import urllib.request

def download_cascade(cascade_path):
    """Download cars.xml if it does not exist"""
    if not os.path.exists(cascade_path):
        print("⚠️ cars.xml not found. Downloading...")
        url = "https://github.com/andrewssobral/vehicle_detection_haarcascades/raw/master/cars.xml"
        urllib.request.urlretrieve(url, cascade_path)
        print("✅ cars.xml downloaded to", cascade_path)

def detect_vehicles(video_path, cascade_path):
    # Make sure cascade exists
    download_cascade(cascade_path)

    # Load cascade classifier
    vehicle_cascade = cv2.CascadeClassifier(cascade_path)
    if vehicle_cascade.empty():
        print("❌ Error: Could not load cascade file:", cascade_path)
        return

    # Open video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ Error: Could not open video:", video_path)
        return

    # Print video info
    print("✅ Video opened successfully!")
    print("Total Frames:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    print("FPS:", cap.get(cv2.CAP_PROP_FPS))
    print("Resolution:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), "x", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("✅ Video ended or cannot fetch frame.")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect vehicles
        vehicles = vehicle_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50)
        )

        # Draw bounding boxes
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show frame
        cv2.imshow("Vehicle Detection", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(30) & 0xFF == ord('q'):
            print("🛑 Stopped by user.")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


# -------- Example Usage --------
video_path = r"D:\sample.mp4"       # <-- change to your video
cascade_path = r"D:\cars.xml"    # <-- cascade will auto-download if missing

detect_vehicles(video_path, cascade_path)
