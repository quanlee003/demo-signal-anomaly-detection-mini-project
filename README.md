# 📡 Signal Analysis & Anomaly Detection

This project explores basic signal processing concepts by simulating time-series data, applying noise filtering techniques, and detecting anomalies using simple statistical methods.

The goal is to build an intuitive understanding of how real-world signals behave and how irregular patterns can be identified using data-driven approaches.

---

## 🚀 Overview

In many real-world systems (e.g. sensing, telecommunications, infrastructure monitoring), signals are often noisy and difficult to interpret directly.

This project demonstrates a simple pipeline:

1. Generate a clean signal (sine wave)
2. Add noise to simulate real-world conditions
3. Introduce anomalies (disturbances)
4. Apply filtering techniques
5. Detect anomalies using statistical thresholds

---

## 🧠 Key Concepts

- Time-series data
- Signal noise and filtering
- Moving average smoothing
- Statistical anomaly detection
- Pattern recognition in dynamic systems

---

## 🛠️ Technologies Used

- Python
- NumPy
- Matplotlib

---

## 📊 Methodology

### 1. Signal Simulation
A sine wave is generated to represent a clean periodic signal.

### 2. Noise Injection
Random Gaussian noise is added to simulate real-world interference.

### 3. Anomaly Injection
Artificial disturbances are introduced into the signal to mimic irregular events (e.g. blockages or faults).

### 4. Signal Filtering
A moving average filter is applied to smooth the signal and reduce noise.

### 5. Anomaly Detection
A simple statistical threshold is used:
- Values significantly above the mean (mean + 2×std) are flagged as anomalies.

---

## 📈 Example Output

The visualization includes:
- Noisy signal
- Filtered signal
- Detected anomalies (highlighted points)

---

## 💡 Key Learnings

- Real-world signals are often noisy and require preprocessing
- Simple filtering techniques can significantly improve signal clarity
- Even basic statistical methods can be effective for anomaly detection
- Understanding signal behaviour is essential before applying advanced models

---

## 🔭 Future Improvements

- Apply Fourier Transform for frequency domain analysis
- Use advanced filters (e.g. Butterworth, Kalman)
- Implement machine learning models for anomaly detection
- Work with real sensor datasets instead of simulated data

---

## 🎯 Motivation

This project was developed as a self-initiated step to explore signal processing and its applications in real-world sensing systems.

---

## 👤 Author

Quan Le  
Master of Data Science – University of Technology Sydney  
GitHub: https://github.com/quanlee003