import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Read the synthetic data from CSV file
    df = pd.read_csv("synthetic_data.csv")
    time = df["Time (s)"].values
    amplitude = df["Amplitude (pA)"].values

    # Print basic information
    print("Synthetic data loaded")
    print(f"Number of samples: {len(time)}")
    print(f"Sampling rate: {1/(time[1] - time[0])} Hz")

    # Plot the synthetic data
    plt.plot(time, amplitude)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (pA)")
    plt.title("Synthetic Data")
    plt.show()

    # Calculate the average amplitude (just a simple example)
    average_amplitude = np.mean(amplitude)
    print(f"Average Amplitude: {average_amplitude} pA")

    # Save the average amplitude to a CSV file
    df_avg = pd.DataFrame({"Time (s)": time, "Average Amplitude (pA)": [average_amplitude]*len(time)})
    df_avg.to_csv("average_synthetic_data.csv", index=False)
    print("Average synthetic data saved to average_synthetic_data.csv")

if __name__ == "__main__":
    main()
