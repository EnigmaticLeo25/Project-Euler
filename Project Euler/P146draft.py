import math
def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
l=[]


c=0
l=[1,3,7,9,13,27]
j=[1,3,7,9,11,13,17,19,21,23,27]
for i in range(10,1000000,10):
    d=[]
    for num in j:
        if(prime(i**2+num)):
            d.append(num)
    if(d==l):
        c=c+i
        print(i)
    if(i%1000==0):
        print(i)
print(c)