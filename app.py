import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Function to create data stream
def create_data_stream(total_points=100):
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

# Function to identify anomalies
def identify_anomalies(data_points):
    model = IsolationForest(contamination=0.1)  # 10% expected anomalies
    reshaped_data = np.array(data_points).reshape(-1, 1)  # Reshape for model input
    model.fit(reshaped_data)
    return model.predict(reshaped_data)

# Streamlit application
st.set_page_config(page_title="Anomaly Detection Dashboard", layout="wide")
st.title("Real-Time Data Stream Anomaly Detection")

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f5;
        padding: 20px;
    }
    h1 {
        color: #1a1a1a;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar for user input
st.sidebar.header("User Input")
num_points = st.sidebar.slider("Number of Data Points", min_value=50, max_value=200, value=100)

# Start button
if st.button("Start Monitoring"):
    with st.spinner("Generating data and identifying anomalies..."):
        collected_data = create_data_stream(num_points)  # Generate initial data stream
        anomaly_flags = identify_anomalies(collected_data)  # Identify anomalies

    # Display the data
    st.subheader("Generated Data Points:")
    st.write(collected_data)

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.plot(collected_data, label='Data Stream', color='blue')
    plt.scatter([i for i in range(len(collected_data)) if anomaly_flags[i] == -1], 
                [collected_data[i] for i in range(len(collected_data)) if anomaly_flags[i] == -1], 
                color='red', label='Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Real-Time Data Stream with Anomalies')
    plt.legend()
    
    # Show the plot in Streamlit
    st.pyplot(plt)

# Footer
st.markdown("""
    <style>
    .footer {
        text-align: center;
        font-size: 14px;
        color: #555;
        margin-top: 20px;
    }
    </style>
    <div class="footer">
    Made by Swarnim Mishra
    </div>
    """, unsafe_allow_html=True)
