import math
def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False 
    return True

s=0
for i in range(7,100000):
    if(prime(i)):
        s=s+i
        if(prime(s)):
            print(s)
        if(s>1000000):
            break

