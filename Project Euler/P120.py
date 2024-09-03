s=0

for i in range(3,1001):
    if(i%2==0):
        s=s+i*(i-2)
        
    else:
        s=s+i*(i-1)
print(s)