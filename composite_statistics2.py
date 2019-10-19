import glob
import numpy
import matplotlib.pyplot

filenames = glob.glob('inflammation*.csv')
composite_data = numpy.zeros((60,40))

for f in filenames:
    data = numpy.loadtxt(fname = f, delimiter=',')
    composite_data += data

composite_data/=len(filenames)

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.hist(numpy.mean(composite_data, axis=0))

axes2.set_ylabel('max')
axes2.hist(numpy.max(composite_data, axis=0))

axes3.set_ylabel('min')
axes3.hist(numpy.min(composite_data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()
