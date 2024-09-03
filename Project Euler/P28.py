import numpy as np
a = np.zeros((1001,1001))
print(a)
s=0
c=1
b=0
for i in range(2001):
    print(c)
    if(i%4==0):
        b=b+2
    s=s+c
    c=c+b
print(s)
