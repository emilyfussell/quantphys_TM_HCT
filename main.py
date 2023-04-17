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
# plot graph of TM Hct pop averages
plt.plot(time_recen, hct_TM, label="Beta5 = 0.10, experimental value")
plt.xlabel("Time, 0 = beginning of HT")
plt.ylabel("Average Hct percentage")
plt.title("Population Avg of Hct Values for TM people before and after HT")
plt.show()
""" hct eqs for sensitivity analysis are marked w sa (1-4)
 beta 5 is the variable that is manipulated for sensitivity analysis, this is bc beta 5
 refers to the time after hormone therapy, depending on length of hormone therapy Hct levels change"""
hct_TM_sa1 = 45 + beta_1 + (beta_2 * time_recen) + (beta_3 * post_time) + (beta_4 * time_recen) + (0.08 * post_time)
hct_TM_sa2 = 45 + beta_1 + (beta_2 * time_recen) + (beta_3 * post_time) + (beta_4 * time_recen) + (0.09 * post_time)
hct_TM_sa3 = 45 + beta_1 + (beta_2 * time_recen) + (beta_3 * post_time) + (beta_4 * time_recen) + (0.11 * post_time)
hct_TM_sa4 = 45 + beta_1 + (beta_2 * time_recen) + (beta_3 * post_time) + (beta_4 * time_recen) + (0.12 * post_time)
# plot sensitivity analysis
plt.plot(time_recen, hct_TM, label="Beta5 = 0.10, experimental value")
plt.plot(time_recen, hct_TM_sa1, label="Beta5 = 0.08")
plt.plot(time_recen, hct_TM_sa2, label="Beta5 = 0.09")
plt.plot(time_recen, hct_TM_sa3, label="Beta5 = 0.11")
plt.plot(time_recen, hct_TM_sa4, label="Beta5 = 0.12")
plt.legend(['Beta5 = 0.10', 'Beta5 = 0.08', 'Beta5 = 0.09', 'Beta5 = 0.11', 'Beta5 = 0.12'])
plt.xlabel("Time, 0 = beginning of HT")
plt.ylabel("Average Hct percentage")
plt.title("Sensitivity Analysis of Population Avg of Hct Values for TM people before and after HT")
plt.show()
