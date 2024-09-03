def chain(x):
    s=0
    a = str(x)
    for i in a:
        d = int(i)
        s=s+d*d
    if(s==89 or s==1):
        return s
    else:
        return chain(s)
print(chain(85))
c=0
for i in range(1,10000000):
    a= chain(i)
    if(a==89):
        c+=1
    if(i%500000==0):
        print(i)
print(c)


