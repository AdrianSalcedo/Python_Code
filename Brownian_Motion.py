import numpy as np
import matplotlib.pyplot as plt

def brownian_path_sampler(step_size,number_max_of_steps):
    normal_sampler = np.sqrt(step_size)*np.random.randn(number_max_of_steps)
    w_t = np.zeros(number_max_of_steps+1)
    w_t[1:] = np.cumsum(normal_sampler)

    return w_t

step_size = 2**-6
number_max_of_steps = 2**12
T = step_size*number_max_of_steps
time = np.linspace(0,T,number_max_of_steps+1)


for i in np.arange(20):
    B_t= brownian_path_sampler(step_size,number_max_of_steps)
    plt.plot(time,B_t)

plt.plot(time,np.sqrt(time))
plt.plot(time,2*np.sqrt(time))
plt.plot(time,3*np.sqrt(time))
plt.plot(time,-np.sqrt(time))
plt.plot(time,-2*np.sqrt(time))
plt.plot(time,-3*np.sqrt(time))

plt.show()