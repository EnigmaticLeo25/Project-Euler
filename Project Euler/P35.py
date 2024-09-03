import math
def prime(x):
    if(x==1):
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
def circ(x):
    a = len(str(x))
    z = 10**(a-1)
    for i in range(a-1):
        d = x%z
        r = int(x/z)
        d = d*10 + r
        
        if(not prime(d)):
            return False
        x=d
        
    return True
c=0
for i in range(2,1000000):
    if(prime(i)):
        if(circ(i)):
            print(i)
            c+=1
print(c)
        