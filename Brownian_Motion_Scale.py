import numpy as np
import matplotlib.pyplot as plt

def brownian_path_sampler_Scale(step_size,number_max_of_steps,scale):
    normal_sampler = np.sqrt(scale*step_size)*np.random.randn(number_max_of_steps-1)
    w_t = np.zeros(number_max_of_steps)
    w_t[1:] = np.cumsum(normal_sampler)
    w_t=np.array(w_t)/np.sqrt(scale)
    return w_t

scale = 0.5
step_size = 2**-12
number_max_of_steps = 2**12
T = scale*step_size*number_max_of_steps
time = np.linspace(0,T,number_max_of_steps)

for i in np.arange(20):
    B_t= brownian_path_sampler_Scale(step_size,number_max_of_steps,scale)
    plt.plot(time,B_t)

plt.plot(time,np.sqrt(time),time,2*np.sqrt(time),time,3*np.sqrt(time),time,-np.sqrt(time),time,-2*np.sqrt(time),time,-3*np.sqrt(time))

plt.show()