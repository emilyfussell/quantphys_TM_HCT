from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import math


def change_in_hepcidin(hep, t):
    return 3.2774*np.exp(-0.021 * t) - hep / (74.1/60)



t1 = np.linspace(0, 96)
t2 = np.linspace(96, 1000)
hep0 = [4]
level_val = []
for val in t2:
    level_val.append(0.55)
res = odeint(change_in_hepcidin, hep0, t1)
plt.plot(t1, res, 'b')
plt.plot(t2, level_val, 'b')
plt.xlabel("Hours")
plt.ylabel("Hepcidin mRNA transcription")
plt.title("Hepcidin mRNA transcription reduction due to testosterone dose")
plt.show()
plt.show()