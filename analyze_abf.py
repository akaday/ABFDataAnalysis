import pyabf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    # Load the ABF file
    abf = pyabf.ABF("your_file.abf")

    # Print basic information
    print(f"ABF file loaded: {abf.abfID}")
    print(f"Number of sweeps: {abf.sweepCount}")
    print(f"Sampling rate: {abf.dataRate} Hz")

    # Plot the first sweep
    abf.setSweep(0)
    plt.plot(abf.sweepX, abf.sweepY)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (pA)")
    plt.title("Sweep 0")
    plt.show()

    # Calculate the average sweep
    sweeps = []
    for sweep in abf.sweepList:
        abf.setSweep(sweep)
        sweeps.append(abf.sweepY)

    average_sweep = np.mean(sweeps, axis=0)

    # Plot the average sweep
    plt.plot(abf.sweepX, average_sweep, label="Average Sweep")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (pA)")
    plt.title("Average Sweep")
    plt.legend()
    plt.show()

    # Save the average sweep to a CSV file
    df = pd.DataFrame({
        "Time (s)": abf.sweepX,
        "Average Amplitude (pA)": average_sweep
    })

    df.to_csv("average_sweep.csv", index=False)
    print("Data saved to average_sweep.csv")

if __name__ == "__main__":
    main()
