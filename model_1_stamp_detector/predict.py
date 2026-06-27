from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent

model = YOLO(str(ROOT / "models" / "best.pt"))

model.predict(
    source=str(ROOT / "data" / "raw_pages"),
    classes=[0],  # stamp only; ignore paper_label
    conf=0.36,
    iou=0.7,
    save=True,
    save_txt=True,
    save_conf=True,
    save_crop=True,
    project=str(ROOT / "runs"),
    name="stamp_predictions",
    exist_ok=True,
)