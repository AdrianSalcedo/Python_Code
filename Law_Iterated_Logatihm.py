import numpy as np
import matplotlib.pyplot as plt

def brownian_path_sampler(step_size,number_max_of_steps):
    normal_sampler = np.sqrt(step_size)*np.random.randn(number_max_of_steps-1)
    w_t = np.zeros(number_max_of_steps)
    w_t[1:] = np.cumsum(normal_sampler)

    return w_t

step_size = 2**-12
number_max_of_steps = 2**12
T = 2**12 #step_size*number_max_of_steps
time = np.linspace(0,T,number_max_of_steps)

k = 2**8 +1
new_time = time[k:]

#for i in np.arange(20):
B_t= brownian_path_sampler(step_size,number_max_of_steps)
    #plt.plot(time,B_t)

new_B_t = B_t[k:]

law_of_iterated_log = new_B_t/np.sqrt(2*new_time*np.log(np.log(new_time)))

plt.plot(new_time, law_of_iterated_log)
plt.show()