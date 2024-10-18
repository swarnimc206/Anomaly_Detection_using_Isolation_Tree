# Efficient Data Stream Anomaly Detection

## Project Overview

The **Efficient Data Stream Anomaly Detection** project aims to develop a Python application that detects anomalies in a continuous data stream. This application simulates real-time sequences of floating-point numbers, representing various metrics such as financial transactions or system metrics. The focus is on identifying unusual patterns, such as exceptionally high values or deviations from the norm.

## Features

- Simulated data stream generation with seasonal patterns and random noise.
- Anomaly detection using the Isolation Forest algorithm.
- Real-time visualization of the data stream with highlighted anomalies.
- Interactive user interface built with Streamlit.

## Technologies Used

- **Python 3.x**
- **Streamlit** for web application interface
- **NumPy** for numerical operations
- **Matplotlib** for data visualization
- **scikit-learn** for machine learning anomaly detection

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. It's recommended to use a virtual environment to manage dependencies.

### Setup Instructions

1. **Create Directory:**


   mkdir Efficient-Data-Stream-Anomaly-Detection
   cd Efficient-Data-Stream-Anomaly-Detection


2. **Create and activate a virtual environment:**

   python -m venv venv_anomaly

   # On Windows
   venv_anomaly\Scripts\activate

   # On macOS/Linux
   source venv_anomaly/bin/activate


3. **Install required packages:**

   pip install -r requirements.txt
 

## Usage

1. **Run the Streamlit application:**


   streamlit run app.py
   

2. Access the application:

   Open your web browser and go to `http://localhost:8501`.

3. Interact with the application:

   - Use the slider in the sidebar to select the number of data points to generate.
   - Click the **"Start Monitoring"** button to begin the anomaly detection process.
   - View the generated data points and the corresponding visualization with detected anomalies.

## Error Handling
The application includes error handling mechanisms in both the data generation and anomaly detection functions. Users will receive clear error messages through the Streamlit interface in case of:

   - Invalid parameters for data generation.
   - Issues during the anomaly detection process.

## Key Changes Made

Conciseness: Streamlined sentences for better readability while retaining essential information.
Error Handling Section: Added a dedicated section to highlight the presence of error handling in the application.
Clear Structure: Organized sections with consistent formatting for easy navigation.



## Code Structure
 # Project documentation
  # Required packages  # Module for data visualization # Module for anomaly detection logic # Module for data stream generation # Main Streamlit application

Efficient-Data-Stream-Anomaly-Detection/




├── app.py                   
├── data_stream_generation.py 
├── anomaly_detection_process.py 
├── visualization_module.py  
├── requirements.txt         
└── README.md                




## Acknowledgements

- [Streamlit](https://streamlit.io/) for the framework used in building the application.
- [scikit-learn](https://scikit-learn.org/stable/) for the machine learning tools utilized in anomaly detection.



# Code Walkthrough for Efficient Data Stream Anomaly Detection





### Importing Libraries
The application imports essential libraries for functionality:
- **Streamlit** for web application development.
- **NumPy** for numerical operations.
- **Pandas** for data manipulation.
- **Matplotlib** for data visualization.
- **IsolationForest** from scikit-learn for anomaly detection.
- **Time** for simulating real-time data generation.

### Simulated Data Generation
A function `generate_data(n_points, noise_level)` generates synthetic data representing a continuous data stream. It combines:
- A linear trend.
- Seasonal variations using a sine function.
- Random noise to mimic real-world data variability.

### Anomaly Detection
The `detect_anomalies(data)` function implements the Isolation Forest algorithm. It fits the model to the generated data and identifies anomalies based on predictions:
- Anomalies are marked when the prediction result is -1.

### Streamlit User Interface
The application sets up a user-friendly interface with:
- A title and sidebar settings.
- Sliders for users to adjust the number of data points and noise levels.
- A button to initiate monitoring.

### Main Monitoring Loop
Upon clicking the "Start Monitoring" button, an infinite loop executes:
- New data is generated based on user inputs.
- Anomalies in the data are detected.
- The generated data and anomalies are visualized in a plot using Matplotlib, displayed in the Streamlit app.
- A delay simulates the real-time data stream, allowing for continuous monitoring.


