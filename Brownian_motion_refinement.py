import numpy as np
import matplotlib.pyplot as plt

########################################################################################################################
def brownian_path_sampler(step_size,number_max_of_steps):
    normal_sampler = np.sqrt(step_size)*np.random.randn(number_max_of_steps)
    w_t = np.zeros(number_max_of_steps+1)
    w_t[1:] = np.cumsum(normal_sampler)

    return (normal_sampler,w_t)
########################################################################################################################
def multiple(valor, multiple):
    #
    #Funcion para calcular si el numero es multiplo
    #utilizando el modulo de la division

    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
########################################################################################################################
N = 2**16 # max numer of step size
T = 1 # total length of interval
delta = 1/N #step size

dB,B_t = brownian_path_sampler(delta,N) #generating the path

p = 2**8 # scale for new step size
Delta = p*delta # new step size
L = int(N/p) # new number of step size

time = np.linspace(0,T,N+1) # discretization of time by N
new_time = np.linspace(0,T,L+1) # new discretization of time by L

## Here we do the multiple of p to check that the new path with the new step size is
# equal to the original path in the corresponding component
multiples_p= []
for i in np.arange(N):
    if multiple(i, p):
        multiples_p.append(i)

########################################################################################################################
B_t_aux = 0
Binc = []
Binc.append(B_t_aux)


for j in np.arange(L): #Here we do the increment in the new step size
    B_t_aux = np.sum(dB[j*p:(j+1)*p]) # operation for generate the increment
    Binc.append(B_t_aux)  # Vector with the increments

Binc = np.array(Binc) # Transform the vector list to vector numeric
Binc_1 = Binc.cumsum() # do the cumulative sum in the new step size


plt.plot(time,B_t)
plt.plot(new_time,Binc_1,'-r')
plt.legend(('$\delta$ = {}'.format(delta), '$\Delta$ = {}'.format(Delta)), prop = {'size':10}, loc = 'upper left')#right')

plt.xlabel('Time')
plt.ylabel('Brownian Path')


plt.show()

########################################################################################################################