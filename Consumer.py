from kafka import KafkaConsumer
from tensorflow.keras.models import load_model, save_model
import numpy as np
from sklearn.metrics import accuracy_score

consumer = KafkaConsumer(
    'ml-raw-dns',
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',
    enable_auto_commit=False
)


def preprocess(data):
    return
# for m in consumer:
#     print(m.value)



static_model_performance = []
dynamic_model_performance = []

static_model = load_model('static_model.h5')

dynamic_model = static_model
window_size = 1000  # Define the window size

window_data = []  # Initialize an empty list to hold the window data

for m in consumer:

    window_data.append(m.value)


    break
    # Check if the window has reached the desired size
    if len(window_data) == window_size:
        # Process the window data
        # You can add your processing logic here
        print("Processing window...")
        processed_data = preprocess(window_data)
        static_predictions = static_model.predict(processed_data)
        static_accuracy = accuracy_score(true_labels, static_predictions)  # Define true_labels
        static_model_performance.append(static_accuracy)

        dynamic_model.fit(processed_data, labels)  # Define labels


        dynamic_predictions = dynamic_model.predict(processed_data)
        dynamic_accuracy = accuracy_score(labels, dynamic_predictions)  # Define labels
        dynamic_model_performance.append(dynamic_accuracy)

        # 4. Evaluate the performance of each model on each window
        print(f"Static Model Accuracy: {static_accuracy}")
        print(f"Dynamic Model Accuracy: {dynamic_accuracy}")

        # Reset the window data
        window_data = []