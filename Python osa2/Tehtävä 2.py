from matplotlib import pyplot as plt
import numpy as np

plt.figure(figsize=(6.4*3, 4.8*3))  # Kuvan koko 3x

x = np.linspace(-3*np.pi, 3*np.pi, 1000)  # x-akselin arvot
y = np.sin(x)

plt.plot(x, y, color='magenta', linestyle='--', label='sin(x)')  #sin(x) käyrä
plt.legend(loc='upper right')  # Lisää selitteen

plt.xticks([-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi],
           [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$']) # merkinnät x-akselille
plt.yticks([-1, 0, 1]) # Merkinnät y-akselille

plt.grid(True)  # Ruudukko

plt.show()
