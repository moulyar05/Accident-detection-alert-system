import cv2
from ultralytics import YOLO
import smtplib
import datetime
from email_alert import send_alert
import threading
from incident_log import log_incident
import threading
import dashboard

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)
print("Fall Detection starting... Press Q to quit")

threading.Thread(target=dashboard.start, daemon= True).start()
while True:
    ret, frame = cap.read()

    if not ret:
        break

    results= model(frame, verbose=False)

    for result in results:
        boxes = result.boxes

        for box in boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]

            if label == "person":
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                width = x2 - x1
                height = y2 - y1
                
    
                if width > height:
                    status = "FALL DETECTED!"
                    color = (0, 0, 255)  
                    timestamp = datetime.datetime.now()
                    threading.Thread(target=send_alert, args=(timestamp,)).start()
                    log_incident(timestamp)
                       
                else:
                    status = "Normal"
                    color = (0, 255, 0) 

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, status, (x1, y1 - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    cv2.imshow("Fall Detection System", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()