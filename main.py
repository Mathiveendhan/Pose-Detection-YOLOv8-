from ultralytics import YOLO

model = YOLO('yolov8m.pt')
#model = YOLO('yolov8m-pose.pt')

results = model.track(source='pose.mp4', show=True, tracker=" bytetrack.yaml")
#results = model.track(source='0', show=True, conf=0.3, save=True)