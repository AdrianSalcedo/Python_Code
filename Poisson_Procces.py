import numpy as np
import matplotlib.pyplot as plt

N = 15
Mean = 2.5

X_n = np.random.exponential(Mean,N)
X_n = np.concatenate (([0],X_n))

S_n = X_n.cumsum()

N_t = np.linspace(0,N,N+1)

plt.step(S_n,N_t)
plt.title('Poisson Process')
plt.ylabel('$N_t$')
plt.xlabel('$S_n$')
plt.show()