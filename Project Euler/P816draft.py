import math
def pointgen(x):
    s0=290797
    s1=(s0**2)%50515093
    p=[]
    p.append([s0,s1,1])
    for i in range(x-1):
        s2=(s1**2)%50515093
        s3 = (s2**2)%50515093
        s1=s3
        p.append([s2,s3,i+2])

    return p
p = pointgen(2000000)
      

d=[]
for i in range(len(p)):
    a=p[i][0]
    b=p[i][1]
    c= math.sqrt(a**2 + b**2)
    d.append([c,i+1])
print(min(d))
m= min(d)[0]
d.sort()

c1=0
c2=0
e=[]
for i in range(len(d)-1):
    a = d[i][0]
    b = d[i+1][0]
   
    if(math.fabs(a-b)<m):
        c1=d[i][1]
        c2=d[i+1][1]
        a1=p[c1-1][0]
        b1=p[c1-1][1]
        c=p[c2-1][0]
        d1=p[c2-1][1]
        e.append([[a1,b1],[c,d1]])

print("bruh")    
print(e)  
    