# from scipy.stats import binom
# n = 5
# k = 3
# p = 0.5
# prob = binom.pmf(k,n,p)
# print(prob)
import numpy as np 
import matplotlib.pyplot as plt
values = np.random.uniform(0,10,10_00_000)
plt.hist(values,bins = 100,density = True,alpha = 0.3)
plt.title("Continous uniform Distribution between 0 and 10")
plt.xlabel("x")
plt.ylabel("probability Density")
plt.grid(True)
plt.show()