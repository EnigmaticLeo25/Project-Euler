import math
def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)
 
def g(x):
    s=0
    c=-1
    for i in range(1,x+1):
        hcf = math.gcd(x,i**2)
        p = c*hcf
        s=s+p
        c=c*-1
    return s
def prime(x):
    if(x==2):
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
mc=0
prev = 0
for i in range(1,100):
    if(i%100000==0):
        print(i)
    if(i%2==1):
        mc=mc-i
    else:
        if(prime(int(i/2))):
            mc=mc+(i-1)
        else:
            mc=mc+g(i)
    gr = g(i)
    print(i,"\t",gr,gr/i)
        

print(mc)
def fg(x):
    s=0
    c=-1
    for i in range(1,x+1):
        hcf = math.gcd(x,i)
        p = c*hcf
        s=s+p
        c=c*-1
    return s
bro=[]
for i in range(2,1000,2):
    l = g(i)/fg(i)
    bro.append(l)
    if(l==1.5):
        print(i,l)
bro = set(bro)
bro = list(bro)
bro.sort()
print(bro)