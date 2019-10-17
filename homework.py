import numpy as np

data = np.loadtxt(fname='data.csv', delimiter=',')
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
