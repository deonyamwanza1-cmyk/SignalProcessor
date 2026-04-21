# C++ Digital Signal Processing Pipeline

A cross-language data pipeline demonstrating fundamental Digital Signal Processing (DSP). This project simulates a noisy sensor feed, processes the data through a custom C++ Infinite Impulse Response (IIR) low-pass filter, and visualizes the signal recovery.

## ⚙️ How It Works
The pipeline consists of three distinct stages, separating data generation, core processing, and visualization:
1. **Signal Generation (Python):** Synthesizes a pure 5Hz sine wave and injects random uniform noise to simulate environmental interference or sensor inaccuracy. Outputs raw data to a text stream.
2. **Filter Engine (C++):** Reads the raw data and applies an Exponential Moving Average (EMA) low-pass filter. The algorithm mathematically attenuates high-frequency noise while preserving the underlying low-frequency signal.
3. **Data Visualization (Python):** Uses `matplotlib` to overlay the raw noisy signal against the clean C++ output for visual verification of the filter's performance.

## 🧮 The Mathematics
The core C++ engine uses a first-order IIR filter formula:
`y[n] = (α * x[n]) + (1 - α) * y[n-1]`

* `y[n]` = Current filtered output
* `x[n]` = Current noisy input
* `y[n-1]` = Previous filtered output
* `α` (Alpha) = Smoothing factor. A lower alpha (e.g., 0.1) creates a stronger filtering effect by relying heavily on past data, while a higher alpha reacts more quickly to sudden changes.

## 🛠️ Tech Stack & Concepts
* **Languages:** C++, Python
* **Concepts:** Digital Signal Processing (DSP), Exponential Moving Averages, Cross-language data pipelines, File Stream I/O (`<fstream>`).
* **Libraries:** `math`, `random`, `matplotlib.pyplot`

## 🚀 How to Run the Pipeline

### Prerequisites
Ensure you have a C++ compiler (like `g++`) and Python installed, along with the `matplotlib` library (`pip install matplotlib`).

### Execution Steps
1. **Generate the Noisy Data:**
   ```bash
   python SignalGenerator.py
   (This creates signal_data.txt)

2. **Compile and Run the C++ Filter:**
   ```bash
   g++ FilterEngine.cpp -o FilterEngine
  ./FilterEngine
   (This reads the noisy data and outputs the clean signal to filtered_data.txt)
4. **Visualize the Results:**
   ```bash
   python VisualizeSignal.py
   (This generates and displays filter_results.png)
***
### Output Preview
![Graph of filtered signals](filter_result.png)
