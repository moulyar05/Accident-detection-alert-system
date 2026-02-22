# Test file - used to verify camera and YOLOv8 are working

import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap=cv2.VideoCapture(0)
print("AI detection starting... Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not found")
        break

    results = model(frame, verbose = False)
    annotated_frame =  results[0].plot()
    cv2.imshow("Accident Detection System", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Detection stopped")