import math

def numdiv(x):
    s=2
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            if(i!=int(x/i)):
                s=s+2
            else:
                s=s+1
    return s
                
c=0
t=numdiv(2)
for i in range(3,10000000):
    a = numdiv(i)
    if(t==a):
        
        c=c+1
    t = a
    if(i%100000==0):
        print(i)
print(c)