from itertools import permutations


import math
def collatz(x):
    l=[]
    while(math.log2(x)!=int(math.log2(x))):
        l.append(x)
        if(x%2==0):
            x=int(x/2)
        else:
            x = 3*x +1
        
    return l
l = collatz(113)
print(l)
c=0 
k=[]
'''for i in range(1,1000000):
    l = collatz(i)
    
    if(len(l)==10):
        print(l)
        s=""
        for j in range(9):
            if(l[j]%2==0):
                s=s+"d"
            else:
                s=s+"^"
        print(s)
        k.append(s)
            
k = set(k)
print(len(list(k)))'''
l=[]
for i in range(8):
    s=""
    for j in range(i):
        s=s+'d'
    print(s)
t=0

            