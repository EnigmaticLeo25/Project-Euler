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
n = 2**1000
print(digits(n))
s=0
for i in digits(n):
   s+=i
print(s)
