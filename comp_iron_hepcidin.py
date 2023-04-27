import matplotlib.pyplot as plt
import numpy as np

hep_vals = np.linspace(0.5, 10, 1000)
rbc_g = (14.625 + (hep_vals - 6.66749)/(-0.3149))

plt.plot(hep_vals,rbc_g)
plt.xlabel("Hepcidin concentration in nM")
plt.ylabel("Rbc production in millions per g body weight")
plt.title("The effect of Hepcidin concentration on RBC production per g body weight")
plt.show()


body_weights = [65000, 73000, 57100, 46400, 125000] # in g
rbc_pp = []
for weight in body_weights:
    rbc_pp.append(((10**6 * (14.625 + (hep_vals - 6.66749)/(-0.3149))) * weight)/(10**12))
plt.xlabel("Hepcidin concentration in nM")
plt.ylabel("Total RBC production patient (*10^12) ")
plt.title("Total patient RBC production in response to hepcidin concentration")
plt.plot(hep_vals, rbc_pp[0], label="Patient A with body weight of 65kg")
plt.plot(hep_vals, rbc_pp[1], label="Patient B with body weight of 73kg")
plt.plot(hep_vals, rbc_pp[2], label="Patient C with body weight of 57.1kg")
plt.plot(hep_vals, rbc_pp[3], label="Patient D with body weight of 46.4kg")
plt.plot(hep_vals, rbc_pp[4], label="Patient E with body weight of 125kg")
plt.legend(['Patient A with a body weight of 65 kg', 'Patient B with a body weight of 73 kg', 'Patient C with a body weight of 57.1 kg',
            'Patient D with a body weight of 46.4 kg', 'Patient E with a body weight of 125 kg'])
plt.show()
