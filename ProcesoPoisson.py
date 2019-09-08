import matplotlib.pyplot as plt
import numpy as np

t=10.2
lam=2
S_n=0
i=1

while True:
    i=i+1
    X_n=np.random.exponential(lam,1)
    S_n=S_n+X_n
    S=np.concatenate((S_n,X_n))
    #print(X_n)
    #print(S_n)

    if S_n>t:
        break
print(S)