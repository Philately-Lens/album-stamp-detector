from pathlib import Path
import argparse
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent

parser = argparse.ArgumentParser(description="Train the stamp detector.")
parser.add_argument(
    "--data",
    required=True,
    help="Path to the dataset.yaml file."
)
args = parser.parse_args()

dataset_yaml = Path(args.data).expanduser().resolve()

if not dataset_yaml.exists():
    raise FileNotFoundError(f"Dataset YAML not found: {dataset_yaml}")

model = YOLO("yolo11n.pt")

model.train(
    data=str(dataset_yaml),
    epochs=120,
    imgsz=960,
    batch=-1,
    patience=30,
    project=str(ROOT / "runs"),
    name="stamp_detector_v1",
)