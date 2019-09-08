import matplotlib.pyplot as plt
import numpy as np

N = 15
mean = 2

X_n = np.random.exponential(mean,N)
X_n = np.concatenate(([0],X_n))
print(X_n)
S_n = X_n.cumsum()
print(S_n)

N_t = np.linspace(0, N, N+1)
#print(N_t)

plt.step(S_n,N_t)
plt.title("Poisson Process", fontdict={'fontname': 'Times New Roman', 'fontsize': 21}, y=1.03)
plt.ylim(0)
plt.show()