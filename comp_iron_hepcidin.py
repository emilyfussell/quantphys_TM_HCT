import matplotlib.pyplot as plt
import numpy as np

hep_vals = np.linspace(0.5, 10, 1000)
rbc_g =  (14.625 + (hep_vals - 6.66749)/(-0.3149))

plt.plot(hep_vals,rbc_g)
plt.xlabel("Hepcidin concentration in nM")
plt.ylabel("Rbc production in millions per g body weight")
plt.title("The effect of Hepcidin concentration on RBC production per g body weight")
plt.show()

MCV_cells = -11.152 * ((14.625 + (hep_vals - 6.66749)/(-0.3149))/1000) + 144.76
plt.plot(hep_vals,MCV_cells)
plt.xlabel("Hepcidin concentration in nM")
plt.ylabel("MCV of blood cells")
plt.show()


body_weights = [65000, 73000, 57100, 46400, 125000] # in g
rbc_pp = []
for weight in body_weights:
    rbc_pp.append(((10**6 * (14.625 + (hep_vals - 6.66749)/(-0.3149))) * weight)/(10**12))
plt.xlabel("Hepcidin concentration in nM")
plt.ylabel("Total RBC production patient (*10^-12) ")
plt.plot(hep_vals, rbc_pp[0], label="Patient A with body weight of 65kg")
plt.plot(hep_vals, rbc_pp[1], label="Patient B with body weight of 73kg")
plt.plot(hep_vals, rbc_pp[2], label="Patient C with body weight of 57.1kg")
plt.plot(hep_vals, rbc_pp[3], label="Patient D with body weight of 46.4kg")
plt.plot(hep_vals, rbc_pp[4], label="Patient E with body weight of 125kg")
plt.show()
