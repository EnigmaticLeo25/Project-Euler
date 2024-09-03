def collatz(x):
    s=0
    while(x!=1):
        if(x%2==0):
            x=x/2
        else:
            x=3*x+1
        s+=1
    return s
max = 1
value = 1
for i in range(1,1000000):
    g = collatz(i)
    if(g>max):
        max = g
        value = i
print(max,value)