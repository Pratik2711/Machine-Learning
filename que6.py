#6. Reverse a vector (first element becomes last)

import numpy as np
print("Enter the range of the vector")
n=int(input())
vector1 = np.zeros(n)
vector2= np.zeros(n)
print("Enter the elements in the vector")
for i in range (n):
    vector1[i]=int(input())
print("vector is = ",vector1)
vector2=vector1[::-1]
print("reverse of the vector is =",vector2)

'''OUTPUT: 
Enter the range of the vector
5
Enter the elements in the vector
11
22
33
44
55
vector is =  [11. 22. 33. 44. 55.]
reverse of the vector is = [55. 44. 33. 22. 11.]'''