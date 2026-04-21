import math
import random

# --- CONFIGURATION ---
FILENAME = "signal_data.txt"
DURATION = 2.0            # Total duration in seconds
SAMPLING_RATE = 1000      # How many data points per second (1kHz)
FREQUENCY = 5             # The "true" signal frequency (5Hz)
NOISE_LEVEL = 0.6         # Amplitude of the random noise (0.0 to 1.0)

def generate_noisy_sine():
    total_samples = int(DURATION * SAMPLING_RATE)
    
    print(f"Generating {total_samples} samples...")
    
    with open(FILENAME, "w") as f:
        for i in range(total_samples):
            # 1. Calculate the time step 't'
            # t = current_index / total_samples_per_second
            t = i / SAMPLING_RATE
            
            # 2. Calculate the pure sine wave value
            # Formula: sin(2 * pi * frequency * time)
            clean_value = math.sin(2 * math.pi * FREQUENCY * t)
            
            # 3. Create random "noise" (interference)
            # This mimics electronic jitter or radio interference
            noise = random.uniform(-NOISE_LEVEL, NOISE_LEVEL)
            
            # 4. Combine them
            noisy_value = clean_value + noise
            
            # 5. Save to file (formatted to 4 decimal places)
            f.write(f"{noisy_value:.4f}\n")

    print(f"Done! Signal saved to '{FILENAME}'.")

if __name__ == "__main__":
    generate_noisy_sine()
