import cv2
import os
from datetime import datetime

# Create a directory to save detected faces if it doesn't exist
if not os.path.exists('detected_faces'):
    os.makedirs('detected_faces')

# Initialize the video capture
videoCapture = cv2.VideoCapture(0)
if not videoCapture.isOpened():
    print("Unable to open the camera")
    exit()

# Load the cascade classifier for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Video Writer for saving the video stream
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(videoCapture.get(3)), int(videoCapture.get(4))))

frame_count = 0

while True:
    ret, frame = videoCapture.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    frame = cv2.flip(frame, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Display the count of detected faces
    face_count_text = f"Faces Detected: {len(faces)}"
    cv2.putText(frame, face_count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Save each detected face
        face_img = frame[y:y+h, x:x+w]
        face_filename = os.path.join('detected_faces', f'face_{datetime.now().strftime("%Y%m%d_%H%M%S")}_{frame_count}.jpg')
        cv2.imwrite(face_filename, face_img)
    
    # Add timestamp to the frame
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cv2.putText(frame, timestamp, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Face Detection', frame)
    out.write(frame)  # Write the frame to the video file

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
out.release()  # Release the video writer
cv2.destroyAllWindows()

