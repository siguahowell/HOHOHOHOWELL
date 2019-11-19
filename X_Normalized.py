#problem 1
import numpy as np
#create a 5x5 in random
x=np.random.random((5,5))
#get the mean
x_mean=x.mean()
#get the standard deviation
x_std=x.std()
#get the normalized
norm=((x-x_mean)/x_std)
print(norm)    