# IOAI Portfolio — Milana

A collection of my projects from the International Olympiad in Artificial Intelligence (IOAI): one machine learning task and two computer vision tasks, all in Python.

## Repository structure

| Folder | Topic | What it does |
| --- | --- | --- |
| [`IOAI_Round3`](./IOAI_Round3) | Machine learning | Binary classification on tabular data (20 numeric features) |
| [`IOAI-50Fins`](./IOAI-50Fins) | Computer vision | Loads a photo and shows it in colour and grayscale |
| [`IOAI-Ryabokon2`](./IOAI-Ryabokon2) | Computer vision | Live webcam feed with a circle and a logo overlay in the centre |

## IOAI_Round3 — Tabular classification

- **Data:** `training_file.csv` (5,600 rows, imbalanced: 4,950 of class 0 vs 650 of class 1) and `test_file.csv` (2,400 rows).
- **`main.py`** — Random Forest (100 trees, `class_weight='balanced'`) → `my_prediction.csv`
- **`Advansed_main.py`** — Gradient Boosting (200 estimators, depth 5) → `ryabokon_prediction.csv`
- `advanced_prediction.csv` — an additional prediction file.
- **Libraries:** pandas, scikit-learn

Run:
```bash
cd IOAI_Round3
python main.py
python Advansed_main.py
```

## IOAI-50Fins — Image processing

`image_process.py` reads `photo.jpg` and opens two windows: the original and the grayscale version. Press **Q** to close.

```bash
cd IOAI-50Fins
python image_process.py
```

## IOAI-Ryabokon2 — Webcam overlay

`webcam_circle.py` opens the webcam, draws a green circle in the centre of the frame and places `logo.png` (resized to 40×40) inside it. Press **Q** to quit.

```bash
cd IOAI-Ryabokon2
python webcam_circle.py
```

## Setup

```bash
pip install pandas scikit-learn opencv-python
```

Python 3.9+ is recommended. The webcam project needs a connected camera.
