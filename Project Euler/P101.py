def f(x):
    return 1-x+x**2-x**3+x**4-x**5+x**6-x**7+x**8-x**9+x**10


for i in range(1,11):
    print(f(i))
    
import numpy as np   
    
s=1
l=[]
for i in range(1,12):
    l.append(f(i))
        
print(l)  


for i in range(2,11):
    a = np.zeros((i,i))
    b = np.zeros(i)
    for j in range(1,i+1):
        c = np.zeros(i)
        for k in range(1,i+1):
            c[k-1] = j**(i-k)
        a[j-1] = c
        b[j-1] = l[j-1]
  
    e =np.linalg.solve(a,b)
    print(e)
    t=0
    for j in range(len(e)):
        t=t+e[j]*((i+1)**(i-j-1))
    print(t)
    s=s+t
print(s)