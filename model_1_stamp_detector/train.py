from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent

model = YOLO("yolo11n.pt")

model.train(
    data=str(ROOT / "dataset.yaml"),
    epochs=120,
    imgsz=960,
    batch=-1,
    patience=30,
    project=str(ROOT / "runs"),
    name="stamp_detector_v1",
)