import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)  # time
signal = np.sin(2 * np.pi * 5 * t)  # clean signal
noise = np.random.normal(0, 0.4, t.shape)  # random noise
noisy_signal = signal + noise  # add noise

plt.plot(t, signal, label="Clean Signal")
plt.plot(t, noisy_signal, label="Noisy Signal", alpha=0.7)
plt.title("Signal with Noise")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
