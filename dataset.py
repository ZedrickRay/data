from ultralytics import YOLO

# Load a pre-trained pose model (you can use n, s, m, l depending on your PC)
model = YOLO("yolov8n-pose.pt")

# Train the model
model.train(
    data="data.yaml",   # path to your dataset.yaml
    epochs=20,            # number of training epochs
    imgsz=640,             # image size
    batch=20,              # number of images per batch (adjust if GPU memory is low)
)
model.export(format="tflite", nms=True)  # export the model to TensorFlow Lite format with NMS