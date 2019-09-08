import matplotlib.pyplot as plt
import numpy as np
import math
N = 10000
T_1 = 1.0
c = 2

delta = T_1/np.float(N)
eps = 1.0/np.sqrt(np.float(N))
t_1 = np.linspace(0,T_1,N+1)
b = np.sqrt(delta)*np.random.randn(N) # Gaussian
Xn = eps*(b.cumsum())
Xn = np.concatenate(([0],Xn))

plt.subplot(1, 2, 1)
plt.plot(t_1,Xn,color='g')
plt.title('Brownian Motion Original')

#new brownian motion modified
t_2 = np.linspace(0,c*T_1,N+1)

Bcn = Xn/math.sqrt(c)

plt.subplot(1, 2, 2)
plt.plot(t_1,Bcn,color='r')
plt.title('Brownian Motion Modified')
plt.show()
