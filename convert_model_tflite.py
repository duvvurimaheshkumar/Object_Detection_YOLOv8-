from ultralytics import YOLO
path = input('Enter the path for the file example - runs/detect/train/weights/best.pt')
model = YOLO(path)
model.export(format='tflite')
