import numpy as np
import matplotlib.pyplot as plt

#function_compute_sample_path
def brownian_path_sampler(step_size,number_max_of_steps):
    normal_sampler = np.sqrt(step_size)*np.random.randn(number_max_of_steps-1)
    w_t = np.zeros(number_max_of_steps)
    w_t[1:] = np.cumsum(normal_sampler)

    return w_t

#data
step_size = 2**-12
number_max_of_steps = 2**12
T = 2**12 #step_size*number_max_of_steps
time = np.linspace(0,T,number_max_of_steps)
epsilon = 20

k = 2**8 +1
new_time = time[k:]


#sample_path_defined
B_t= brownian_path_sampler(step_size,number_max_of_steps)
new_B_t = B_t[k:]

#create the bounded for sample_path
Bounded_1 = np.array((1-epsilon)*np.sqrt(2*new_time*np.log(np.log(new_time))))
Bounded_2 = np.array((1+epsilon)*np.sqrt(2*new_time*np.log(np.log(new_time))))

#plot the sample_path and the bounded
plt.plot(new_time,new_B_t,new_time,Bounded_1,new_time,Bounded_2)
#new_B_t = B_t[k:]
#law_of_iterated_log = new_B_t/np.sqrt(2*new_time*np.log(np.log(new_time)))
#plt.plot(new_time, law_of_iterated_log)


plt.show()