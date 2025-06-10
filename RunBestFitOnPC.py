from ultralytics import YOLO
import cv2

# Initialize the model
model = YOLO("runs/detect/train4/weights/best.pt")

try:
    # Predict
    results = model.predict(source="0",show = True)
except:
    pass
