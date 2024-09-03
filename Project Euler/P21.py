
import math
def factorsum(x):
    s=0
    if(x==1):
        return 0
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            s=s+i+int(x/i)
            
    return s+1
s=0
for i in range(1,10000):
    a=factorsum(i)
    if(a>10000 or a==i):
        continue
    if(factorsum(a)==i):
        s=s+i
        print(i,a)
print(s)
print(5000*10001)
print(factorsum(9973))
print(factorsum(1))