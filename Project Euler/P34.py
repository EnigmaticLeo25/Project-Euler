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
l = digits(157)
print(l)
def check(x):
    s=0
    for i in digits(x):
       s =s+fact(i)
    if(s==x):
        return True
    return False
print(check(157))
for i in range(10,10000000):
    if(check(i)):
       print(i)
