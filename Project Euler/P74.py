import math
def df(x):
    s=0
    a = str(x[0])
    for i in a:
        s=s+math.factorial(int(i))
    if(s==145):
        return [s,x[1]+1]
    if(s==169 or s==1454 or s==363601):
        return [s,x[1]+3]
    if(s==871 or s==872 or s==45361 or s==45362):
        return [s,x[1]+2]
    if(x[0]==s):
        return x
    x[0]=s
    x[1]=x[1]+1
    if(s==2 or s==1):
        return x
    return df(x)

c=0 
print(24+120+120+720*7*8)
for i in range(3,1000000):
    if(i==10 or i==11):
        continue
    a=df([i,1])
    if(i%50000==0):
        print(i)
    if(a[1]==60):
        print(a)
        c=c+1
print(c)