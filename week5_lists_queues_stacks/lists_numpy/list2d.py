lst = [[i*j for j in range(10)] for i in range(10)]
print("lst: ", lst)

import numpy as np
avgs = [np.mean(i) for i in lst]
print("avgs: ", avgs, np.mean(avgs))

