import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def rhs(y, t_zero):
    s_p = y[0]
    l_p = y[1]
    i_p = y[2]
    s_v = y[3]
    i_v = y[4]
    
    s_p_prime = beta * ( l_p +i_p) - a * s_p * i_v
    l_p_prime = a * s_p * i_v - b * l_p - beta * l_p
    i_p_prime = b *l_p - beta * i_p 
    s_v_prime = - Lambda * s_v * i_p  - g * s_v + (1 - theta) * mu
    i_v = Lambda * s_v * i_p - g * i_v + theta * mu
    rhs_np_array = np.array([s_p_prime, l_p_prime, i_p_prime, s_v_prime, i_p_prime])
    return(rhs_np_array)


beta = 0.01
a = 0.1
g = 0.06
mu = 1.0
theta = 0.04
b =  0.075
Lambda = 0.003

y_zero = np.array([0.9, 0.0, 0.1, 0.89, 0.11 ])
t = np.linspace(0, 70, 1000)
sol = odeint(rhs, y_zero, t )
plt.plot(t, sol[:, 2], 'b', label='I_p')
plt.plot(t, sol[:, 4], 'r', label='I_v')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
