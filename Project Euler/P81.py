import numpy as np
f = open("0081_matrix.txt","r")
str = f.readline()
l = np.zeros((80,80))
print(l)
row=0
while(str!=None):
    col=0
    str = str.split(",")
    for i in str:
        l[row][col] = int(i)
        col+=1
    str=f.readline()
    row+=1
    if(row==80):
        break
l = l.astype(int)
for i in range(len(l)-1,-1,-1):
    for j in range(len(l)-1,-1,-1):
        if(i==len(l)-1 and j==len(l)-1):
            continue
        if(i==len(l)-1):
            l[i][j]=l[i][j]+l[i][j+1]
            continue
        if(j==len(l)-1):
            l[i][j]=l[i][j]+l[i+1][j]
            continue
        l[i][j] = l[i][j]+min(l[i+1][j],l[i][j+1])
        
            
print(l)         
    