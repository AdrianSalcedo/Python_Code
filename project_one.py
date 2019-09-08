import matplotlib.pyplot as plt
import numpy as np

N = 10000
T = 1.0
delta = T/np.float(N)
eps = 1.0/np.sqrt(np.float(N))
t = np.linspace(0,T,N+1)
b = np.random.binomial(1,0.5,N) # bernoulli 0,1
omega = 2.0*b-1  #bernoulli -1, 1
Xn = eps*(omega.cumsum()) # bernoulli -h,h
Xn = np.concatenate(([0],Xn))
plt.plot(t,Xn)
plt.show()