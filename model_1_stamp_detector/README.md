
# Stamp AI — Sri Lankan Stamp Detector

An offline computer-vision project for detecting postage stamps in Sri Lankan stamp album-page photographs.

This is the first model in a larger Stamp AI system. Its purpose is to automatically find individual stamps in an album page so they can later be cropped, stored, and compared against a collector’s personal collection.

## Current Model

* Model: YOLO11n object detector
* Task: Object detection
* Classes:

  * `0` — stamp
  * `1` — paper_label
* Input: Stamp album-page image
* Output: Bounding boxes around detected stamps and handwritten paper labels

## Dataset

The training dataset is maintained in a separate repository:

`https://github.com/Nethsith/sri-lanka-stamp-album-dataset`

Dataset version used for the initial model:

* Total annotated pages: 68
* Training pages: 51
* Validation pages: 7
* Test pages: 10
* Annotation format: YOLO bounding boxes

## Project Structure

```text
model_1_stamp_detector/
├── models/
│   └── best.pt
├── reports/
│   ├── BoxF1_curve.png
│   ├── BoxPR_curve.png
│   ├── confusion_matrix.png
│   └── results.png
├── sample_data/
│   ├── images/
│   └── labels/
├── train.py
├── predict.py
├── dataset.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

```bash
git clone https://github.com/Nethsith/Stamp-AI.git
cd Stamp-AI/model_1_stamp_detector
```

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Train the Model

First download or clone the dataset repository.

```powershell
git clone https://github.com/Nethsith/sri-lanka-stamp-album-dataset.git
```

Then train using the dataset YAML file:

```powershell
python train.py --data "PATH_TO_DATASET\dataset.yaml"
```

Example:

```powershell
python train.py --data "D:\projects\stamp\sri-lanka-stamp-album-dataset\dataset.yaml"
```

Training outputs will be saved inside:

```text
runs/
```

## Run Prediction

The trained model is stored at:

```text
models/best.pt
```

To detect only stamps from a folder of album-page images:

```powershell
yolo detect predict model="models/best.pt" source="PATH_TO_IMAGES" classes=0 conf=0.36 iou=0.7 save=True save_txt=True save_conf=True save_crop=True
```

* `classes=0` detects stamps only.
* `conf=0.36` is the selected confidence threshold from the F1-confidence analysis.
* `save_crop=True` saves individual detected stamp crops.

## Reports

The `reports/` folder contains training and validation results, including:

* F1-confidence curve
* Precision-recall curve
* Confusion matrix
* Training and validation loss curves

## Limitations

This is an initial detector trained on a limited custom dataset of Sri Lankan stamp album pages.

It may struggle with:

* Heavily overlapping stamps
* Very small stamps
* Stamps partly hidden by other stamps
* Strong glare or blur
* Unusual album layouts not represented in the dataset

The dataset and model will be expanded in future versions.

## Future Work

* Add more labelled album pages.
* Improve detection of overlapping and triangular stamps.
* Add automatic perspective correction and image preprocessing.
* Build a second model to match exact stamp variants.
* Integrate the trained models into an offline mobile application.

## Author

Nethsith Gunaweera

## License

This repository contains code and trained model files for research and educational purposes.

The dataset has its own separate license in the dataset repository.
