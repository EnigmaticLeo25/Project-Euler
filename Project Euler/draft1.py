import math
def makeList(x):
    l=[]
    for i in range(2,x+1):
        l.append(i)
    return l
l = makeList(10)

def prime(x):
    if(x==2 or x==3 or x==5 or x==7):
        return x
    for i in range(2,10000+1):
        if(x%i==0):
            return i
    return x
def step(l):
    b=[]
    c=1
    for i in range(len(l)):
        a = prime(l[i])
        l[i] = l[i]/a
        b.append(a)
    count = l.count(1)  
    for i in range(count):
        l.remove(1)
    for i in b:
        c=c*i
    l.append(c)
for i in range(125):
    step(l) 
    if(i>=0):
        print(l)
    
s=0     
for i in l:
    s=s+i
print(s)
    