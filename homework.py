import numpy as np

data = np.loadtxt(fname='data.csv', delimiter=',')
print(data)
maxData = np.max(data)
minData = np.min(data)
meanData = np.mean(data)
stdData = np.std(data)
print(f'MaxValue = {maxData}! | MinValue = {minData} | Mean Value = {meanData} | Standard Deviation = {stdData} ')
