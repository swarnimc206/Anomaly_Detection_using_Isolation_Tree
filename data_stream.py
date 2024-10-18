import numpy as np
import random

def create_data_stream(total_points=100):
    """
    Simulates a continuous data stream with seasonal patterns and noise.
    :param total_points: Number of data points to generate
    :return: List of generated data points
    """
    stream_data = []
    for i in range(total_points):
        seasonal_variation = 50 * np.sin(i / 10)  # Seasonal variation
        random_noise = random.uniform(-10, 10)  # Random noise
        value = 100 + seasonal_variation + random_noise  # Base value with patterns and noise
        
        # Introduce anomalies occasionally
        if random.random() < 0.1:  # 10% chance of anomaly
            value += random.choice([30, 50, 100])  # Add a spike
            
        stream_data.append(value)
    return stream_data
