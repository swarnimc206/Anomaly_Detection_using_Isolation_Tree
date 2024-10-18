import numpy as np
import random
import time
import matplotlib.pyplot as plt

# Node structure for Isolation Trees
class TreeNode:
    def __init__(self, left=None, right=None, split_feature=None, split_value=None, size=1):
        self.left = left
        self.right = right
        self.split_feature = split_feature
        self.split_value = split_value
        self.size = size

# Isolation Tree
def iTree(data, current_height, height_limit):
    if current_height >= height_limit or len(data) <= 1:
        return TreeNode(size=len(data))
    
    # Randomly select a feature and a split value
    q = random.randint(0, data.shape[1] - 1)
    p = np.random.uniform(min(data[:, q]), max(data[:, q]))
    
    left_indices = data[:, q] < p
    right_indices = data[:, q] >= p
    
    left_tree = iTree(data[left_indices], current_height + 1, height_limit)
    right_tree = iTree(data[right_indices], current_height + 1, height_limit)
    
    return TreeNode(left=left_tree, right=right_tree, split_feature=q, split_value=p)

# Path length calculation for a given point
def pathLength(point, tree, current_height):
    if tree.left is None and tree.right is None:
        return current_height + c(tree.size)
    
    if point[tree.split_feature] < tree.split_value:
        return pathLength(point, tree.left, current_height + 1)
    else:
        return pathLength(point, tree.right, current_height + 1)

# Average path length of unsupervised trees
def avgPathLength(point, forest):
    return np.mean([pathLength(point, tree, 0) for tree in forest])

# Expected path length of an unsuccessful search in a Binary Search Tree
def c(n):
    if n <= 1:
        return 0
    return 2 * (np.log(n - 1) + np.euler_gamma) - (2 * (n - 1) / n)

# Isolation Forest
def fitIsolationForest(data, num_trees=100):
    forest = []
    height_limit = np.ceil(np.log2(len(data)))
    for _ in range(num_trees):
        sample = data[np.random.choice(len(data), size=len(data), replace=False)]
        forest.append(iTree(sample, 0, height_limit))
    return forest

# Identify anomalies
def identify_anomalies(data_points):
    forest = fitIsolationForest(np.array(data_points).reshape(-1, 1))
    avg_lengths = [avgPathLength(point, forest) for point in np.array(data_points).reshape(-1, 1)]
    
    # Calculate threshold
    threshold = np.percentile(avg_lengths, 90)
    return [1 if length >= threshold else -1 for length in avg_lengths]

# Simulates a continuous data stream with seasonal patterns and noise
def create_data_stream(total_points=100):
    stream_data = []
    for i in range(total_points):
        seasonal_variation = 50 * np.sin(i / 10)
        random_noise = random.uniform(-10, 10)
        value = 100 + seasonal_variation + random_noise

        # Introduce anomalies occasionally
        if random.random() < 0.1:
            value += random.choice([30, 50, 100])
            
        stream_data.append(value)
    return stream_data

# Visualizes the data stream with detected anomalies
def plot_data(data_points, anomaly_flags):
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

# Main function to simulate and observe data stream for anomalies
def observe_data_stream():
    collected_data = []
    data_stream = create_data_stream(100)
    for point in data_stream:
        collected_data.append(point)
        anomaly_flags = identify_anomalies(collected_data)
        if anomaly_flags[-1] == -1:
            print(f"Anomaly detected: {point}")
        time.sleep(0.5)
    plot_data(collected_data, anomaly_flags)

if __name__ == "__main__":
    observe_data_stream()
