import numpy as np
f = open("0082_matrix.txt","r")
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



def mindist(i,j,l):
    m=[]
    for k in range(0,i):
        start = l[k][j] + li[k][j-1]
        for g in range(k+1,i):
            start = start + l[g][j]
        start = start + l[i][j]
        m.append(start)
    for k in range(len(l)-1,i,-1):
        start = l[k][j] + li[k][j-1]
        for g in range(k-1,i,-1):
            start = start + l[g][j]
        start = start + l[i][j]
        m.append(start)
        
    m.append(l[i][j]+li[i][j-1])
    return min(m)
        


li=[[0]*len(l) for i in range(len(l))]
for j in range(0,len(l)):
    if(j==0):
        for i in range(len(l)):
            li[i][j] = l[i][j]
        
    else:
        for i in range(len(l)):
            li[i][j] = mindist(i,j,l)
    
                
print(li) 
j = len(l)-1
c=[]
for i in range(len(l)):
    c.append(li[i][j])
print(min(c))
        