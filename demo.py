import numpy as np
print("Enter the range of the vector")
n=int(input())
vector1 = np.zeros(n)
vector2= np.zeros(n)
for i in range (n):
    vector1[i]=i+1
print("vector is = ",vector1)
vector2=vector1[::-1]
print("reverse of the vector is =",vector2)
print(vector2)