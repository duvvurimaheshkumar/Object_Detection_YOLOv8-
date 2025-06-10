import os
# os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from ultralytics import YOLO

# Define a function to train a YOLO model with specified parameters
def train_yolo_model(model_name, data_path, epochs, img_size):
    print(f"Training YOLO model: {model_name} with data_path: {data_path}, epochs: {epochs}, img_size: {img_size}")
    model = YOLO(model_name)
    results = model.train(data=data_path, epochs=epochs, imgsz=img_size)
    print("Training completed.")
    return model


# List of YOLO models
yolo_models = [ 'yolov8x.pt', 'yolov8l.pt', 'yolov8m.pt', 'yolov8s.pt', 'yolov8n.pt']

# Ask the user which YOLO models they want to train on
print("Choose YOLO models to train on:")
for i, model in enumerate(yolo_models):
    print(f"{i+1}. {model}")
selected_models = input("Enter the numbers separated by commas (e.g., 1, 3, 5): ")
selected_model_indices = [int(idx.strip()) - 1 for idx in selected_models.split(',')]

# Define parameters to tune
epochs_input = input("Enter epochs separated by commas (e.g., 1, 2, 3): ")
epochs_list = [int(epoch.strip()) for epoch in epochs_input.split(',')]

img_sizes_input = input("Enter image sizes separated by commas (e.g., 416, 512, 608): ")
img_sizes = [int(size.strip()) for size in img_sizes_input.split(',')]

# Iterate through the selected YOLO models
for idx in selected_model_indices:
    model_name = yolo_models[idx]
    print(f"\nTrying YOLO model: {model_name}")
    
    # Iterate through different combinations of parameters
    for epochs in epochs_list:
        for img_size in img_sizes:
            # Train the YOLO model
            trained_model = train_yolo_model(model_name, 'data_custom.yaml', epochs, img_size)
            
            # Export the trained model to TFLite format
            
            # Ask the user if they want to continue with the next parameter combination
            user_input = input("Do you want to try the next combination? (yes/no): ")
            if user_input.lower() != 'yes':
                break
        else:
            continue  # Continue to the next epoch size
        break  # Break out of the loop if the user doesn't want to continue with the next model

    # Ask the user if they want to continue with the next YOLO model
    user_input = input("Do you want to try the next YOLO model? (yes/no): ")
    if user_input.lower() != 'yes':
        break