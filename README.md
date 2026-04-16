# 🃏 Blackjack Object Detection (WIP)

An End-to-End Computer Vision and Machine Learning pipeline designed to detect and recognize Blackjack cards in real-time directly from the screen. This project is currently a Work In Progress (WIP).

## 🚀 Project Overview

The goal of this project is to build a real-time card recognition system. The pipeline is divided into three main phases:
1.  **Data Collection:** Custom high-frequency screen capture script to build a proprietary dataset.
2.  **Annotation & Training:** Manual annotation and model training using **YOLOv11** via Roboflow.
3.  **Real-Time Inference (WIP):** Live screen analysis to detect cards and calculate Blackjack values.

## 🛠️ Tech Stack & Tools

*   **Python:** Core programming language.
*   **OpenCV (`cv2`):** Image processing and rendering.
*   **mss:** Ultra-fast cross-platform module for taking screenshots.
*   **Roboflow & YOLOv11:** For dataset management, annotation, and training the Object Detection model.

## 📂 Current Progress

*   ✅ **`data_collector.py`:** A custom script that captures a specific region of the screen (the game window) and saves the frames as `.jpg` using UUIDs. It uses keyboard hooks (`s` to save, `q` to quit) for rapid data gathering.
*   ✅ **Model Training:** Initial model (`FORSECISIAMO 3`) trained on Roboflow using YOLOv11 architecture, achieving preliminary metrics (Precision: 78.8%).
*   ⏳ **Inference Engine:** *Currently in development.* Integration of the YOLO model to perform live detection and calculate the cards' sum.

## 💻 How to use the Data Collector

If you want to gather more training data:

1. Install the dependencies:
   ```bash
   pip install opencv-python mss keyboard numpy
   ```
2. Run the script:
   ```bash
   python data_collector.py
   ```
3. Place your game window in the top-left corner of the screen. Press `S` to save a frame, `Q` to quit. Images will be saved in the `dataset_raw` folder.

---
*Developed by [Federico Taiola](https://github.com/FedeTaiola)*
