# 🧠 Stroke Detection from Brain MRI Images

A deep learning-based medical imaging application that detects stroke in brain MRI scans using a Convolutional Neural Network (CNN), with an interactive web interface built using Streamlit.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)

---

## 🔍 Overview

Stroke is one of the leading causes of death and long-term disability worldwide. Early detection is critical for effective treatment. This project leverages deep learning to automatically classify brain MRI images as either **Normal** or **Stroke**, enabling faster and more accessible diagnosis support.

The system consists of two components:
1. **Training Notebook** (`Stroke_image_detact.ipynb`) — builds and trains the CNN model.
2. **Web App** (`ImageDetact.py`) — a Streamlit app that loads the trained model and accepts MRI images for real-time prediction.

---

## ✨ Features

- ✅ Binary classification: **Normal** vs. **Stroke**
- ✅ Accepts JPG/JPEG image uploads via a clean web UI
- ✅ Real-time prediction with confidence-based thresholding (≥ 50%)
- ✅ Image preprocessing pipeline (resize, normalize, RGB conversion)
- ✅ Training and validation loss/accuracy visualization
- ✅ Model evaluation using classification report and confusion matrix

---

## 📂 Dataset

The model was trained on an organized brain MRI dataset with two classes:

| Class   | Description                        |
|---------|------------------------------------|
| Normal  | MRI scans of healthy brains        |
| Stroke  | MRI scans showing stroke evidence  |

Images are resized to **224×224 pixels** and normalized to the `[0, 1]` range before training.

**Dataset split:** 80% training / 20% testing (with shuffle)

---

## 🏗️ Model Architecture

The CNN model is built using Keras Sequential API:

```
Input: (224, 224, 3)
│
├── Conv2D(100 filters, 3×3, ReLU) → MaxPooling2D(2×2)
├── Conv2D(80 filters,  3×3, ReLU) → MaxPooling2D(2×2)
├── Conv2D(64 filters,  3×3, ReLU) → MaxPooling2D(2×2)
│
├── Flatten
├── Dense(500, ReLU) → Dropout(0.2)
├── Dense(500, ReLU) → Dropout(0.2)
└── Dense(1, Sigmoid)  ← Binary output
```

**Training configuration:**
- Optimizer: `Adam`
- Loss: `Binary Crossentropy`
- Metric: `Accuracy`
- Epochs: `5`
- Batch Size: `32`

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stroke-detection.git
cd stroke-detection
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**
```
streamlit
tensorflow
keras
numpy
Pillow
scikit-learn
matplotlib
pandas
```

---

## 🚀 Usage

### Running the Web Application

Make sure the trained model file `graduation project.h5` is in the same directory as `ImageDetact.py`, then run:

```bash
streamlit run ImageDetact.py
```

Open your browser and navigate to `http://localhost:8501`.

### How to Use the App

1. Click **"Browse files"** or drag and drop a brain MRI image (`.jpg` or `.jpeg`).
2. The uploaded image will be displayed.
3. The model will process the image and output the prediction:
   - 🟢 **Normal** — No stroke detected
   - 🔴 **Stroke** — Stroke detected

### Training the Model

Open and run the Jupyter notebook:

```bash
jupyter notebook Stroke_image_detact.ipynb
```

Update the dataset paths in the notebook to match your local directory structure before running.

---

## 📁 Project Structure

```
stroke-detection/
│
├── Stroke_image_detact.ipynb   # Model training & evaluation notebook
├── ImageDetact.py              # Streamlit web application
├── graduation project.h5       # Trained model weights (generated after training)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 📊 Results

Training performance is visualized using loss and accuracy curves across epochs:

- **Training vs. Validation Loss** — monitors overfitting
- **Training vs. Validation Accuracy** — tracks learning progress
- **Classification Report** — includes Precision, Recall, and F1-Score per class

---

## 🛠️ Technologies Used

| Technology     | Purpose                          |
|----------------|----------------------------------|
| Python 3.x     | Core programming language        |
| TensorFlow / Keras | Model building & training    |
| NumPy          | Numerical array operations       |
| Pillow (PIL)   | Image loading and preprocessing  |
| Streamlit      | Web application interface        |
| Matplotlib     | Training performance plots       |
| Scikit-learn   | Evaluation metrics               |

---

## 🔮 Future Improvements

- [ ] Upgrade to a pretrained architecture (e.g., VGG16, ResNet50, EfficientNet) via transfer learning
- [ ] Expand training epochs and apply data augmentation for improved generalization
- [ ] Add Grad-CAM visualizations to highlight stroke regions in the MRI
- [ ] Deploy the app on a cloud platform (e.g., Streamlit Cloud, Hugging Face Spaces)
- [ ] Support DICOM format (`.dcm`) for real-world clinical use
- [ ] Add confidence score display alongside the prediction label

---

## 👨‍💻 Author

Developed as a **Graduation Project** for medical image analysis using deep learning.

---

## 📄 License

This project is intended for academic and educational purposes only. It is **not a certified medical diagnostic tool** and should not be used as a substitute for professional medical advice.
