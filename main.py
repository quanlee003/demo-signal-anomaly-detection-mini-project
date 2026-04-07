import numpy as np
import matplotlib.pyplot as plt

# 1. Create a clean signal (sine wave)
t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * t)

# 2. Add noise
noise = np.random.normal(0, 0.3, t.shape)
noisy_signal = signal + noise

# 3. Add anomaly (simulate blockage / disturbance)
noisy_signal[200:220] += 2

# 4. Simple moving average filter
window_size = 10
filtered_signal = np.convolve(noisy_signal, np.ones(window_size)/window_size, mode='same')

# 5. Detect anomaly (simple threshold)
threshold = np.mean(filtered_signal) + 2 * np.std(filtered_signal)
anomalies = np.where(filtered_signal > threshold)

# 6. Plot
plt.figure(figsize=(10,5))
plt.plot(t, noisy_signal, label='Noisy Signal')
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.scatter(t[anomalies], filtered_signal[anomalies], color='red', label='Anomaly')
plt.legend()
plt.title("Signal Simulation & Anomaly Detection")
plt.show()