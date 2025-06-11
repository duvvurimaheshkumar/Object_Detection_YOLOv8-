# Object_Detection_YOLOv8-
---
# YOLO Model Training Script

This project provides an interactive Python script to train multiple YOLO (You Only Look Once) object detection models using the [Ultralytics YOLO](https://docs.ultralytics.com/) library. The script allows you to select different YOLO model variants, specify training epochs and image sizes, and iteratively train models on your custom dataset.

## Features

- **Interactive Model Selection:** Choose which YOLO model variants to train (`yolov8x`, `yolov8l`, `yolov8m`, `yolov8s`, `yolov8n`).
- **Parameter Tuning:** Specify multiple values for training epochs and image sizes to experiment with different configurations.
- **Step-by-Step Training:** The script guides you through each training combination, allowing you to continue or stop at any point.
- **Easy Customization:** Modify the script to suit your dataset or export needs.

## Prerequisites

- **Python 3.8+**
- **Ultralytics YOLO library**  
  Install via pip:
  ```bash
  pip install ultralytics
  ```
## Dataset Preparation

- Prepare your dataset in YOLO format.
- Create a `data_custom.yaml` file describing your dataset.  

## Usage

1. **Run the script:**
   ```bash
   python your_script_name.py
   ```

2. **Follow the prompts:**
   - **1. Select YOLO models**  
   - **2. Enter epochs**  
   - **3. Enter image sizes**  
   - **4. Continue or stop:**  
     After each training run, you can choose to continue with the next parameter combination or stop.

3. **Training Output:**  
   - Training progress and results will be displayed in the terminal.
   - Trained models and logs will be saved in the default Ultralytics output directory (`runs/detect/`).

## Script Overview

- **Model Selection:**  
  Choose from five YOLOv8 model variants.
- **Parameter Input:**  
  Specify multiple values for epochs and image sizes.
- **Training Loop:**  
  For each selected model and parameter combination, the script trains the model and prompts you to continue or stop.
- **Export (Placeholder):**  
  The script includes a placeholder for exporting trained models to TFLite format. You can implement this using Ultralytics' export functionality if needed.

## References

- [Ultralytics YOLO Documentation](https://docs.ultralytics.com/)
- [YOLOv8 Model Zoo](https://docs.ultralytics.com/models/)
