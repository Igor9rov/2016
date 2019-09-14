
# coding: utf-8

# In[ ]:

import numpy
import scipy.io

all_variables = scipy.io.loadmat('C:\Users\Игорь\Documents\MATLAB\mfilter.mat')

pyhmf = all_variables['hmf']
pyhmf_taylor = all_variables['hmf_taylor']
pyhwav = all_variables['hwav']
pysig = all_variables['sig']
pyt = all_variables['t']
pyw = all_variables['w']
pyx = all_variables['x']
pyy = all_variables['y']
pyy_taylor = all_variables['y_taylor']

