import numpy as np
import pandas as pd

# Parameters for synthetic data
sampling_rate = 20000  # Hz
duration = 2  # seconds
num_samples = sampling_rate * duration
time = np.linspace(0, duration, num_samples)

# Generate synthetic data (e.g., a sine wave)
frequency = 5  # Hz
amplitude = 100  # pA
data = amplitude * np.sin(2 * np.pi * frequency * time)

# Save the synthetic data to a CSV file
df = pd.DataFrame({"Time (s)": time, "Amplitude (pA)": data})
df.to_csv("synthetic_data.csv", index=False)

print("Synthetic data saved to synthetic_data.csv")
