l=[]
for i in range(2,101):
    for j in range(2,101):
        a = i**j
        l.append(a)
l=set(l)
print(len(l))

#P56
def digitsum(x):
    s=0
    str1 = str(x)
    for i in str1:
        s=s+int(i)
    return s

max=0
for i in range(2,100):
    for j in range(2,100):
        a = i**j
        m = digitsum(a)
        if(m>max):
            max=m
print(max)