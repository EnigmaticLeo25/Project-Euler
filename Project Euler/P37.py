import math
def prime(x):
    if(x==1):
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
def trunc(x):
    n =x
    
    while(n>1):
        n = int(n/10)
        
        if(not prime(n)):
            return False

    a=str(x)
    n=len(a)
    while(x>1):
        x=x%10**(n-1)
        
        n=n-1
        if(not prime(x)):
            return False
    return True
print(trunc(3797))

s=0
c=1
for i in range(11,1000000,2):
    if(prime(i)):
        if(trunc(i)):
            print(i,c)
            s=s+i
            c=c+1
print(s)