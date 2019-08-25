import numpy as np
import matplotlib.pyplot as plt
from Poisson_Sampler import Poisson_Sampler

#m Main Program

#data
N = 70
te = [] # generate a list
Mean = 3

#loops for generate the process

for i in np.arange(0,N):
    S_n,N_t = Poisson_Sampler(Mean,N)
    t_jump = S_n[1]
    te.append(t_jump)

#Create an array (change the vector list to a numerical vector)

te = np.array(te)

#plot the process

plt.subplot(1, 2, 1)
plt.step(S_n,N_t)
plt.title('Poisson Process')
plt.ylabel('$N_t$')
plt.xlabel('$S_n$')

# plot the histogram of first jump

plt.subplot(1, 2, 2)
plt.hist(te,color='r')
plt.title('Histogram of first jump')
plt.show()
