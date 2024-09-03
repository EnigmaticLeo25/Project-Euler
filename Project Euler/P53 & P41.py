#P53
import math
count=0
print(math.comb(23,10))
for i in range(1,101):
    for j in range(1,i+1):
        if(math.comb(i,j)>1000000):
            count+=1
        
print(count)

def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False 
    return True

#P41
from itertools import permutations
for i in range(4,10):
    l=[]
    for j in range(1,i+1):
        l.append(j)
    print(l)
    perm = permutations(l)
    li=[]
    for i in list(perm):
        s=""
        for j in i:
            s=s+str(j)
        li.append(s)
    for i in li:
        if prime(int(i)):
            print(i)
     