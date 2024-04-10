from matplotlib import pyplot as plt
import numpy as np

plt.figure(figsize=(6.4*3, 4.8*3))  # Aseta kuvan koko kolminkertaiseksi

x = np.linspace(-3*np.pi, 3*np.pi, 1000)  # Aseta x-akselin arvot
y = np.sin(x)

plt.plot(x, y, color='magenta', linestyle='--', label='sin(x)')  # Piirrä sin(x) käyrä
plt.legend(loc='upper right')  # Lisää selite

# Aseta merkinnät x-akselille käyttäen LaTeX-merkintöjä
plt.xticks([-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi],
           [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$'])

# Aseta merkinnät y-akselille käyttäen LaTeX-merkintöjä
plt.yticks([-1, 0, 1],
           [r'$-\pi$', '0', r'$\pi$'])

plt.grid(True)  # Näytä ruudukko

plt.show()
