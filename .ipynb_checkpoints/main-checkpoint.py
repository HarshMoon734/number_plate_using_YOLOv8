from ultralytics import YOLO

# Load YOLOv8 model (choose 'yolov8n.pt', 'yolov8s.pt', etc.)
model = YOLO("yolov8n.pt")

# Train the model
model.train(data="dataset/data.yaml", epochs=50, imgsz=640, batch=16)
