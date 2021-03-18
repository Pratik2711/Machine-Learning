#19. Create random vector of size 10 and replace the maximum value by 0.
import numpy as np
vector=np.random.random(10)
vector[vector.argmax()]=0
print(vector)

'''OUTPUT:
[0.77911596 0.         0.52946133 0.91469944 0.61869604 0.10230727
 0.15494199 0.72297462 0.4793761  0.83724818]'''

