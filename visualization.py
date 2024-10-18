import matplotlib.pyplot as plt

def plot_data(data_points, anomaly_flags):
    """
    Visualizes the data stream with detected anomalies.
    :param data_points: List of data points
    :param anomaly_flags: List of anomaly flags
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data_points, label='Data Stream', color='blue')
    plt.scatter([i for i in range(len(data_points)) if anomaly_flags[i] == -1], 
                [data_points[i] for i in range(len(data_points)) if anomaly_flags[i] == -1], 
                color='red', label='Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Real-Time Data Stream with Anomalies')
    plt.legend()
    plt.show()
