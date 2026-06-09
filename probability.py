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


# from scipy.stats import norm

# parameters
mu = 70   #mean
sigma = 10 # Standard deviation


# X-axis-values
x = np.linspace(30,110,1000)



# normal PDF
y = np.norm.pdf(x,mu,sigma)


#plot the bell curve
plt.plot(x,y,color = "black",linewidth = 2,label = "normal distribution")


# sigma 68% region (mu =10)
x1 = np.linspace(mu - sigma,mu + sigma, 1000)
plt.fill_between(x1,norm.pdf(x1,mu,sigma),color = "green",alpha = 0.3,label = "68% region (1alpha)")
#shade 95% region (mu = 2 alpha)
x2 = np.linspace()



import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,100,100_000)