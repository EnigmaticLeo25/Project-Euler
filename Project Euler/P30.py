import numpy as np
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
def check(x):
    s=0
    for i in digits(x):
        s =s+(i**5)
    if(s==x):
        return True
    return False
s=0
for i in range(10,10000000):
    
    if(check(i)):
        print(i)
        s=s+i
print(s)    