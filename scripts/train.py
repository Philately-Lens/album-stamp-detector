from pathlib import Path
import argparse
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent.parent

parser = argparse.ArgumentParser(description="Train the stamp detector.")
parser.add_argument(
    "--data",
    default=str(ROOT / "dataset.yaml"),
    help="Path to the dataset.yaml file. Defaults to the repo-local dataset.yaml."
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