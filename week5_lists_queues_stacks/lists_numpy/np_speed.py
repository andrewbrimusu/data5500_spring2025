import numpy
import random
import time

start = time.time()
randoms = []
for i in range(100000000):
    randoms.append(random.randint(1,50))
end = time.time()
#print(randoms)
print("time lapsed: ", end - start)

start2 = time.time()
rands = numpy.random.randint(50, size=10000000)
end2 = time.time()
#print(rands)
print("array time lapsed: ", end2 - start2)

































# checkpoint activity
# There is no checkpoint activity for this
# content video.
# This is just an exercise to show you how
# powerful numpy arrays can be.