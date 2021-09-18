#%%
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [4,8,1,2]

plt.plot(x,y,'b')

plt.title('Gráfico.')
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')

plt.yticks(y)
plt.xticks(x)

plt.grid(axis = 'y', linestyle = ':')

plt.show()
#%%
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.5)

plt.plot(x,x**2,'bx:', label = 'x^2')
plt.plot(x,x**3,'gs--', label = 'x^3')
plt.plot(x,x,'r-.', label = 'x')
plt.legend()

plt.title('Gráfico.')
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')

plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.5)

fig, (ax1,ax2,ax3) = plt.subplots(3,1,figsize=(15,12))

ax1.plot(x,x**2,'bx:',label = 'x^2')
ax1.legend()
ax1.set_ylabel('Eixo Y')
ax1.set_xlabel('Eixo X')

ax2.plot(x,x**3,'gs--', label = 'x^3')
ax2.legend()
ax2.set_ylabel('Eixo Y')
ax2.set_xlabel('Eixo X')

ax3.plot(x,x,'r-.', label = 'x')
ax3.legend()
ax3.set_ylabel('Eixo Y')
ax3.set_xlabel('Eixo X')

plt.suptitle('Gráfico.')

plt.show()
#%%
import matplotlib.pyplot as plt

gp = ['A','B','C']
dados = [5,20,10]

plt.figure(figsize=(9,3))

plt.subplot(1,3,1)
plt.bar(gp,dados)
plt.subplot(132)
plt.scatter(gp,dados)
plt.subplot(133)
plt.plot(gp,dados)

plt.suptitle('Plots')

plt.show()






#%%