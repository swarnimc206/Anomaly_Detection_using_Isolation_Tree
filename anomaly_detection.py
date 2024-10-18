import numpy as np
from sklearn.ensemble import IsolationForest
from data_stream import create_data_stream
import time
from visualization import plot_data

def identify_anomalies(data_points):
    """
    Detect anomalies in the given data using Isolation Forest.
    :param data_points: List of data points
    :return: List of anomaly flags (1 for normal, -1 for anomaly)
    """
    model = IsolationForest(contamination=0.1)  # 10% expected anomalies
    reshaped_data = np.array(data_points).reshape(-1, 1)  # Reshape for model input
    model.fit(reshaped_data)
    return model.predict(reshaped_data)

def observe_data_stream():
    collected_data = []  # Store all data points for visualization
    data_stream = create_data_stream(100)  # Generate initial data stream

    for point in data_stream:
        collected_data.append(point)
        anomaly_flags = identify_anomalies(collected_data)
        if anomaly_flags[-1] == -1:  # Check the most recent point
            print(f"Anomaly detected: {point}")
        time.sleep(0.5)  # Simulate delay for real-time processing

    plot_data(collected_data, anomaly_flags)  # Visualize after monitoring

if __name__ == "__main__":
    observe_data_stream()
