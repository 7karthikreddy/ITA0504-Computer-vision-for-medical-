import cv2
import pytesseract
def extract_text_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_frame)
        print(text)
    cap.release()
    cv2.destroyAllWindows()
extract_text_from_video("D:\sample.mp4")  # Replace 'video.mp4' with your video path
