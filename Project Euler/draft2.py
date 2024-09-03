def makeList(x):
    l=[]
    for i in range(2,x+1):
        l.append(i)
    return l
l = makeList(10)
def step(l):
    m = min(l)
    i = l.index(m)
    l[i] = l[i]**2
    print(l)

for i in range(25):
    step(l)
s=sum(l)
print(s%1234567891)
