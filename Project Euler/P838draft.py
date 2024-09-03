import math
def coprime(m,n):
    if(m<n):
        small=m
    else:
        small=n
    for i in range(2,small+1):
        if(m%i==0 and n%i==0):
            return False
    return True
print(coprime(897,33))

n = 2800
m = int(n/10)
l=[]
for i in range(m):
    a = 10*(i) + 3
    l.append(a)

c=3
def prime(x):
    if(x%3==0):
        return 1
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return i
    return x
s=[]
b=[]
d=[]
for i in l:
    a = prime(i)
    if(prime(i)==i):
        s.append(a)
    else:
        if(i%3!=0):
            b.append(a)
            d.append(i)
s=set(s)
s=list(s)
s.sort()
print(s)
b=set(b)
b=list(b)
b.sort()
print(b)


'''for i in l:
    flag=0
    for j in s:
        if(j>i):
            break
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        s.append(prime(i))'''
'''for i in b:
    for j in s:
        if(j>math.sqrt(i)):
            break
        else:
            if(i%j==0):
                b.remove(i)'''
                
f=[]
for i in b:
    if (i%10==3):
        b.remove(i)
for i in b:
    if (i%10==1):
        b.remove(i)
        f.append(i)
print("b:",b)
print(d)  
print(f)       
for i in s:
    c=c*i
print(c)
a = math.log(c)
print(a)

for i in l:
    if(coprime(i, c)):
        print(i)
print("Length of d:",len(d))
print("Length of s:",len(s))
print("Length of l:",len(l))
for i in b:
    c=0
    for j in d:
        if(j%i==0):
            c+=1
    print(i,";",c)
    
        
#s=3*13*23*43*53*73*83*103*113*7*163*173*193*223*233*263*283*293*313*17*353*373*383*433*443*463

#133 = 7x19
#323 = 17x19