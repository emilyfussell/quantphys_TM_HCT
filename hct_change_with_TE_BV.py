from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# function to calculate how TE changes the hct content of each patient's blood with in the testosterone ranges!


b_vols = [4324.871958, 4439.284321, 4240.061031, 3645.904102, 6638.562557]
hi = np.linspace(0.41, 0.56, 400)  # x axis hct values (baseline hct vals)
delta_hct = []
for val in b_vols:
    dh = (1125.0 * hi - 1.0) / (val * 0.91)
    delta_hct.append(dh)


plt.plot(hi, delta_hct[0], label="Patient A with BV of 4325 mL")
plt.plot(hi, delta_hct[1], label="Patient B with BV of 4439 mL")
plt.plot(hi, delta_hct[2], label="Patient C with BV of 4240 mL")
plt.plot(hi, delta_hct[3], label="Patient D with BV of 3646 mL")
plt.plot(hi, delta_hct[4], label="Patient E with BV of 6639 mL")
plt.legend(['Patient A with BV of 4325 mL', 'Patient B with BV of 4439 mL', 'Patient C with BV of 4240 mL',
            'Patient D with BV of 3646 mL', 'Patient E with BV of 6639 mL'])
plt.xlabel("Initial Hct Values")
plt.ylabel("Change in Hct after TE")
plt.title("Effects of TE in Trans Men")
plt.show()
