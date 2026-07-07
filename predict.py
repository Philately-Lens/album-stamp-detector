from pathlib import Path
import argparse
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent

parser = argparse.ArgumentParser(description="Run stamp detection.")
parser.add_argument(
    "--source",
    required=True,
    help="Path to an image or folder of album-page images."
)
parser.add_argument(
    "--model",
    default=str(ROOT / "models" / "best.pt"),
    help="Path to the trained YOLO model."
)
args = parser.parse_args()

model_path = Path(args.model).expanduser().resolve()

if not model_path.exists():
    raise FileNotFoundError(f"Model not found: {model_path}")

model = YOLO(str(model_path))

model.predict(
    source=args.source,
    classes=[0],
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