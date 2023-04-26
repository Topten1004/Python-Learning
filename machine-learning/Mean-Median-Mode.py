import numpy

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)

median = numpy.median(speed)

mode = stats.mode(speed)

print("mean:", mean)

print("median:", median)

print("mode:", mode)