from math import sqrt
def triangle(x):
    
    l=[]
    i=0
    s=0
    for j in range(x):
        i = i + 1
        s = s + i
        l.append(s)
    return l
l =triangle(10)
print(l)


def factors(x):
    s = 0
    for i in range(1,int(sqrt(x))+1):
        if(x%i==0):
            s=s+2
    return s
        



for i in triangle(100000):
    if(factors(i)>500):
        print(i)
        break
print("loop unsuccesful")