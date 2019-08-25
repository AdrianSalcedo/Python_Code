# Generate the Poisson Process
import numpy as np
def Poisson_Sampler(Mean,N):
    X_n = np.random.exponential(Mean, N)
    X_n = np.concatenate(([0], X_n))

    S_n = X_n.cumsum()

    N_t = np.linspace(0, N, N + 1)
    return(S_n,N_t)