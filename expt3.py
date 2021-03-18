list = []
md=1000
n = int(input("Enter the size of array:-"))
list=[int(i)for i in input().split()]
print(list)
u=int(input("Enter the U values:-"))
v=int(input("Enter the V values:-"))
for i in list:
    if list[i] == u or list[i]==v:
        catch1 = i
        break
while i < n:
    if list[i] == u or list[i] == v:
         if list[catch1] != list[i] and (i-catch1) < md:
             md = i-catch1;
             catch1 = i
         else:
            catch1 = i
    i+=1
print(md)
