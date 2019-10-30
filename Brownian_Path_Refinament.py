import numpy as np
import matplotlib.pyplot as plt

def multiple(valor, multiple):
    #
    #Funcion para calcular si el numero es multiplo
    #utilizando el modulo de la division

    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False


def brownian_path_sampler(step_size,number_max_of_steps):
    normal_sampler = np.sqrt(step_size)*np.random.randn(number_max_of_steps)
    w_t = np.zeros(number_max_of_steps+1)
    w_t[1:] = np.cumsum(normal_sampler)

    return w_t

step_size = 2**-16 #delta minuscula
number_max_of_steps = 2**16 # número total de pasos
T = step_size*number_max_of_steps # tamaño total del intervalo
new_number_max_of_steps = 2**9 # nuevo tamaño total de intervalos

new_step_size = number_max_of_steps/new_number_max_of_steps # generando nuevo delta mayuscula Delta= p*delta( p=Delta/delta)
p=new_step_size # tamaño para el nuevo Delta

print(new_step_size)

multiples_p=[] #vector auxiliar para generar nuevo path
time = np.linspace(0,T,number_max_of_steps+1) #discretización del tiempo

for i in np.arange(number_max_of_steps+1):
    if multiple(i, p):
        multiples_p.append(i)


B_t= brownian_path_sampler(step_size,number_max_of_steps)





plt.plot(time,B_t)
plt.plot(time[multiples_p],B_t[multiples_p],'-.r')
plt.title('$\delta$ = {}, p= {}, $\Delta$ = {}'.format(step_size, p, new_step_size, 1/new_number_max_of_steps))
#plt.title()


plt.show()