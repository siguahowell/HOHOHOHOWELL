import numpy as np
x=np.linspace(1,100,100)
x.resize(10,10)
x=x**2
divisible=np.array([x[x%3==0]])
print(divisible)