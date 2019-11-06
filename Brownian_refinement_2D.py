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

dB1,B1_t = brownian_path_sampler(delta,N) #generating the first Brownian path
dB2,B2_t = brownian_path_sampler(delta,N) #generating the second Brownian path

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
B_t_aux1 = 0
Binc_1 = []
Binc_1.append(B_t_aux1)
B_t_aux2 = 0
Binc_2 = []
Binc_2.append(B_t_aux2)

for j in np.arange(L): #Here we do the increment in the new step size
    B_t_aux1 = np.sum(dB1[j*p:(j+1)*p]) # operation for generate the increment in the first path
    Binc_1.append(B_t_aux1) # Vector with the increments in the first path
    B_t_aux2 = np.sum(dB2[j * p:(j + 1) * p])  # operation for generate the increment in the second path
    Binc_2.append(B_t_aux2) # Vector with the increments in the second path

Binc_1 = np.array(Binc_1) # Transform the vector list to vector numeric for the first path
Binc_11 = Binc_1.cumsum() # do the cumulative sum in the new step size for the first path
Binc_2 = np.array(Binc_2) # Transform the vector list to vector numeric for the second path
Binc_22 = Binc_2.cumsum() # do the cumulative sum in the new step size for the second path



plt.plot(B1_t,B2_t)
plt.plot(Binc_11,Binc_22,'-r')
#plt.plot(new_time,Binc_1,)
#plt.legend(('$\delta$ = {}'.format(delta), '$\Delta$ = {}'.format(Delta)), prop = {'size':10}, loc = 'upper left')#right')

plt.xlabel('Brownian_Path_1')
plt.ylabel('Brownian_Path_2')


plt.show()

########################################################################################################################