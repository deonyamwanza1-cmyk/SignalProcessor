import matplotlib.pyplot as plt

# Load the data
noisy = [float(line) for line in open('signal_data.txt')]
filtered = [float(line) for line in open('filtered_data.txt')]

plt.figure(figsize=(10, 5))
plt.plot(noisy, label='Raw Noisy Signal', alpha=0.5, color='gray')
plt.plot(filtered, label='C++ Filter Output', color='red', linewidth=2)

plt.title('Digital Low-Pass Filter Performance')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Save as a high-quality image for your portfolio
plt.savefig('filter_results.png', dpi=300)
plt.show()
