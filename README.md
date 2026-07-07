
# Album Stamp Detector

**Model 1 of the Philately Lens project**

A YOLO-based object detection model for scanned stamp album pages.
The model is trained to detect stamps and paper labels, while the prediction script returns stamp detections only.

## Detection Classes

| ID | Class           | Description                        |
| -: | --------------- | ---------------------------------- |
|  0 | `stamp`       | A postage stamp on an album page   |
|  1 | `paper_label` | A paper label or note near a stamp |

## Project Structure

```text
album-stamp-detector/
├── models/                         # Optional location for selected trained weights
├── reports/                        # Training notes or reports
├── sample_data/                    # Sample images for testing
│
├── scripts/
│   ├── download_dataset_from_hf.py # Download dataset from Hugging Face
│   ├── train.py                    # Train the detector
│   └── predict.py                  # Run stamp detection
│
├── dataset.yaml                    # YOLO dataset configuration
├── requirements.txt
├── .gitignore
└── README.md
```
