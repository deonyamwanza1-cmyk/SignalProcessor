#include <iostream>
#include <fstream>
#include <vector>
#include <string>

class LowPassFilter {
private:
    double alpha;     // Smoothing factor (0.0 to 1.0)
    double prev_out;  // Stores y[n-1]

public:
    // Constructor: alpha represents the 'strength' of the filter
    LowPassFilter(double a) : alpha(a), prev_out(0.0) {}

    // The core math: y[n] = a * x[n] + (1 - a) * y[n-1]
    double process(double input) {
        double output = (alpha * input) + (1.0 - alpha) * prev_out;
        prev_out = output;
        return output;
    }
};

int main() {
    const std::string input_file = "signal_data.txt";
    const std::string output_file = "filtered_data.txt";

    // Alpha of 0.1 is a strong filter (smoother result)
    // Alpha of 0.9 is a weak filter (noisier result)
    LowPassFilter lpf(0.1);

    std::vector<double> signal_buffer;
    double value;

    // 1. Read the data into a vector
    std::ifstream fin(input_file);
    if (!fin) {
        std::cerr << "Error: Could not open " << input_file << std::endl;
        return 1;
    }

    while (fin >> value) {
        signal_buffer.push_back(value);
    }
    fin.close();

    std::cout << "Read " << signal_buffer.size() << " samples. Processing..." << std::endl;

    // 2. Apply the filter and save to a new file
    std::ofstream fout(output_file);
    for (double noisy_sample : signal_buffer) {
        double clean_sample = lpf.process(noisy_sample);
        fout << clean_sample << "\n";
    }
    fout.close();

    std::cout << "Filtering complete! Saved to " << output_file << std::endl;

    return 0;
}