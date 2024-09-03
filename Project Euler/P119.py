def digitsum(x):
    s=0
    while(x>0):
        a = x%10
        s=s+a
        x = int(x/10)
    return s

def seq(x):
    s = digitsum(x)
    a=s
    if(a==1):
        return False
    
    while(a<=x):
        if(a==x):
            return True
        else:
            a=a*s
    return False
l=[]
for i in range(2,128):
    for j in range(2,20):
        l.append(i**j)

m=[]
l.sort()
for i in l:
    if i not in m:
        m.append(i)
print(l)
c=-2
for i in m:
    if(seq(i)):
        print(i)
        print(c)
        c=c+1
