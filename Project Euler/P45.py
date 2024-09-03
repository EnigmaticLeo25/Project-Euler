


import math
t=[]
for i in range(1,15786):
    j = i*(2*i-1)
    t.append(j)
p=[]
for i in range(1,10866):
    j = i*(3*i-1)/2
    p.append(j)
    

print(t)
print(p)
for i in t:
    if (i in p):
        print(i)
        
        
       

        