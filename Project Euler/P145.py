
def rev(x):
    a=str(x)
    return int(a[::-1])

def odd(x):
    a=str(x)
    for i in a:
        if(int(i)%2==0):
            return False
    return True
c=0
for i in range(10,10000000,2):
    if(i%10==0):
        continue
    s=0
    j = rev(i)
    s=i+j
    if(odd(s)):
        c=c+2
        if(c%100000==0):
            print(c,i,j)
print(c)

