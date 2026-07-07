# Album Stamp Detector

Model 1 of the **Philately Lens** project.

This repository contains a YOLO-based object detection model that identifies stamps and paper labels in stamp album images.

## Classes

| Class ID | Class Name  |
| -------: | ----------- |
|        0 | stamp       |
|        1 | paper_label |

## Project Structure

```text
album-stamp-detector/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── scripts/
│   ├── train.py
│   ├── predict.py
│   ├── upload_dataset_to_hf.py
│   └── download_dataset_from_hf.py
│
├── data/
│   ├── yolo_dataset/
│   │   ├── images/
│   │   │   ├── train/
│   │   │   ├── val/
│   │   │   └── test/
│   │   └── labels/
│   │       ├── train/
│   │       ├── val/
│   │       └── test/
│   │
│   └── [raw image folders]
│
├── dataset.yaml
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.11 recommended
* Git
* A Hugging Face account only when uploading or updating the dataset

## Installation

Clone the repository:

```powershell
git clone https://github.com/Philately-Lens/album-stamp-detector.git
cd album-stamp-detector
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Download the Dataset

The complete dataset, including raw images and YOLO-formatted images and labels, is stored on Hugging Face:

```text
nethsith/sri-lankan-album-stamp-detection
```

Download it into the local `data` folder:

```powershell
python scripts\download_dataset_from_hf.py --repo-id "nethsith/sri-lankan-album-stamp-detection" --output-dir "data"
```

The dataset is public, so downloading does not require a Hugging Face token.

After downloading, confirm that these folders exist:

```text
data/yolo_dataset/images/train
data/yolo_dataset/images/val
data/yolo_dataset/labels/train
data/yolo_dataset/labels/val
```

## Dataset Configuration

The project uses this `dataset.yaml` configuration:

```yaml
path: data/yolo_dataset

train: images/train
val: images/val
test: images/test

names:
  0: stamp
  1: paper_label
```

## Train the Model

Run training from the project root:

```powershell
python scripts\train.py
```

Training outputs, logs, metrics, and model weights are saved inside the `runs/` folder.

The best trained model is normally saved in a path similar to:

```text
runs/stamp_detector_v1/weights/best.pt
```

## Run Predictions

Use the prediction script after training:

```powershell
python scripts\predict.py
```

Ensure that the script is configured to use the correct trained weight file, usually `best.pt`, and the correct input image or folder.

## Upload Dataset Updates

Log in to Hugging Face before uploading:

```powershell
hf auth login
```

Upload the full local `data` folder:

```powershell
python scripts\upload_dataset_to_hf.py --repo-id "nethsith/sri-lankan-album-stamp-detection" --dataset-dir "data"
```

## GitHub Actions

This repository includes a GitHub Actions workflow located at:

```text
.github/workflows/python-ci.yml
```

The workflow runs when Python files, `dataset.yaml`, or the workflow file changes.

It validates:

* Python syntax in the `scripts` folder
* Required values inside `dataset.yaml`

The workflow does not download the dataset or train the model on GitHub Actions.

## Recommended `.gitignore` Entries

Keep large local files out of GitHub:

```gitignore
.venv/
__pycache__/
*.pyc

data/
runs/

.idea/
.vscode/
```
