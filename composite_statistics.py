import glob as gb
import numpy as np
import matplotlib.pyplot as mat

filenames = sorted(gb.glob('inflammation*.csv'))

data1 = np.loadtxt(fname=filenames[0], delimiter=',')
data2 = np.loadtxt(fname=filenames[1], delimiter=',')
combined_average = np.mean(data1,axis=0) - np.mean(data2, axis=0)

fig = mat.figure(figsize=(10.0, 3.0))

mat.ylabel('Difference in average')
mat.plot(combined_average)

fig.tight_layout()
mat.show()
