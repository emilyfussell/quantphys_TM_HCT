from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

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
plt.ylabel("Rate of hepcidin mRNA transcription (a.u.)")
plt.title("Hepcidin mRNA transcription reduction due to testosterone dose")
plt.show()



hep_vals = [3,4,5]
res_2 =[]

t3 = np.linspace(0, 96)
t4 = np.linspace(96, 100)
res_2 = odeint(change_in_hepcidin, hep_vals[0], t1)
res_3 = odeint(change_in_hepcidin, hep_vals[1], t1)
res_4 = odeint(change_in_hepcidin, hep_vals[2], t1)

plt.plot(t3, res_2, 'b')
plt.plot(t4, level_val, 'b')
plt.plot(t3, res_3, 'r')
plt.plot(t4, level_val, 'r')
plt.plot(t3, res_4, 'g')
plt.plot(t4, level_val, 'g')
plt.xlabel("Hours")
plt.ylabel("Rate of hepcidin mRNA transcription")
plt.title("Sensitivity Analysis of Hepcidin mRNA transcription reduction due to testosterone dose")
plt.show()