from math import sqrt
def prime(x):
    for i in range(2,int(sqrt(x))+1):
        if(x%i==0):
            return False
    return True
def factorList(x):
    l=[]
    for i in range(2,int(sqrt(x))+1):
        if(x%i==0):
           a = int(x/i)
           l.append(i)
           l.append(a)
    return l
l = factorList(600851475143)
print(l)
max=0
for i in l:
    if(prime(i)):
        if(max<i):
            max=i
print(max)