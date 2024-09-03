import math
for i in range(500):
    for j in range(500):
        c = math.sqrt(i**2 + j**2)
        if(i+j+c==1000):
            print(i,j,c,i*j*c)
            break

