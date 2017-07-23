#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(0)
f, ax = plt.subplots()

ax.plot(rng.uniform(size=100))

f, ax = plt.subplots()

x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x)

ax.plot(x, y)

print "done1"

f, ax = plt.subplots()

y2 = np.sin(x**2)
ax.plot(x, y, label=r'$\sin(x)$')
ax.plot(x, y2, label=r'$\sin(x^2)$')
ax.set_title('Some functions')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
ax.legend()

print "done2"

#this will show the plots when you execute the python script.
plt.show()

print "finished"