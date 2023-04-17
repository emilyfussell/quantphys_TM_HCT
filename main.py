import matplotlib.pyplot as plt
import numpy as np
# model 2 variables
beta_1 = -0.063
beta_2 = 0.05
beta_3 = -0.11
beta_4 = 0.44
beta_5 = 0.10

time_recen = np.linspace(-20, 10, 1500) # recentered time value, with beginning of HRT at 0
post_time = np.linspace(0, 10, 1500) # time after beginning of HRT
# hematocrit equation from longitudinal paper - individual factors are negated as looking at average
# the fudge factor is 45 (or intercept value) to account for beginning HCT values
hct_TM = 45 + beta_1 + (beta_2 * time_recen) + (beta_3 * post_time) + (beta_4 * time_recen) + (beta_5 * post_time)

plt.plot(time_recen, hct_TM)
plt.title("TM Hct value before and after HRT")
plt.xlabel("Time, 0 = beginning of HRT")
plt.ylabel("Average Hct percentage")
plt.show()
