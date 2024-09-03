import numpy as np
def fact(x):
    c=1
    for i in range(1,x+1):
        c=c*i
    return c
def digits(a):
    b = str(a)
    n = len(b)
    l = np.zeros(n)
    while(a>=1):
        
        digit = a%10
        l[n-1] = digit
        a = int(a/10)
        n-=1
    l = l.astype(int) 
    return l

s = fact(100)
print(s)
l=0
for i in digits(s):
   l = l+i
print(l)