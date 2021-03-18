'''1. You are given a number N and following by an array of N numbers and followed by two
elements U and V. Find the minimum distance between the elements U and V in the array.
The array may have duplicates.
For example, if the array is (1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9)
Minimum distance (U=4, V=7): 4'''
import numpy as np
list = []
a = int(input("Size of array:\n"))
print("Enter the elements")
for i in range(a):
    list.append(float(input(" ")))
arr = np.array(list)
print(np.floor(arr))
print("Enter the value of U\n")
u=int(input())
print("Enter the value of V\n")
v=int(input())
for i in arr:
    if arr== u or arr==v:
        result1=np.where(arr==u) or result=np.where(arr==v)
        result2=result1
        break
while i < n:
    if arr== u or arr== v:
         if arr[result1] != arr[result2] and (result2-result1) < min_dist:
             min_dist = result1-result2;
             result2 = result1
         else:
            result2 = result1
    result1+=1
print(min_dist)
