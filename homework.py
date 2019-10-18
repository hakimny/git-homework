import numpy as np
import matplotlib.pyplot as matplot

data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(data)
maxData = np.max(data)
minData = np.min(data)
meanData = np.mean(data)
stdData = np.std(data)

print(f'Max Value = {maxData:.2f}! | Min Value = {minData:.2f} | Mean Value = {meanData:.2f} | Standard Deviation = {stdData:.2f} ')

# Max,Min, Mean, Standard Deviation per patient

i = 1
for patient in data:
	print(f'Patient {i}:  Max Value = {np.max(patient):.2f} | Min Value =  {np.min(patient):.2f} | Mean Value = {np.mean(patient):.2f} | Standard Deviation = {np.std(patient):.2f}')
	i = i + 1

max_inflammation_per_patient = np.max(data,axis=0)
avg_inflammation_per_patient = np.mean(data, axis=0)
min_inflammation_per_patient = np.min(data,axis=0)
# print(f'Max Data for each patient: {max_inflammation_per_patient}')
# print(f'Mean Value for each day: {avg_inflammation_per_day}')

# Visualize Data


# image = matplotlib.pyplot.imshow(data)
# matplotlib.pyplot.show()


# avg_plot = matplot.plot(avg_inflammation_per_day)
# matplot.show()


# Visualize all 3 graphs

fig = matplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(avg_inflammation_per_patient)

axes2.set_ylabel('max')
axes2.plot(max_inflammation_per_patient)

axes3.set_ylabel('min')
axes3.plot(min_inflammation_per_patient)

fig.tight_layout()

matplot.show()
