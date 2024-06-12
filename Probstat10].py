#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import scipy.stats as stats

plant_a = np.array([4.17, 5.58, 5.18, 6.11, 4.50, 4.61, 5.17, 4.53, 5.33, 5.14])
plant_b = np.array([4.81, 4.17, 4.41, 3.59, 5.87, 3.83, 6.03, 4.89, 4.32, 4.69])
plant_c = np.array([6.31, 5.12, 5.54, 5.50, 5.37, 5.29, 4.92, 6.15, 5.80, 5.26])

data_syifa=[plant_a,plant_b,plant_c]

f_statistic,p_value=stats.f_oneway(plant_a,plant_b,plant_c)

print(f"Nilai F: {f_statistic}")
print(f"Nilai p: {p_value}")


# In[ ]:




