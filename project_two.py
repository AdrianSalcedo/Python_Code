import matplotlib.pyplot as plt
import numpy as np

N = 10000
T = 1.0
delta = T/np.float(N)
eps = 1.0/np.sqrt(np.float(N))
t = np.linspace(0,T,N+1)
b = np.sqrt(delta)*np.random.randn(N) # Gaussian
Xn = eps*(b.cumsum())
Xn = np.concatenate(([0],Xn))
plt.plot(t,Xn)
plt.show()