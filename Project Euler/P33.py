m=1
for i in range(10,100):
   a=str(i)
   num1 = int(a[1])
   for j in range(10*num1,10*num1+10):
       if(i>=j):
           continue
       b = str(j)
       if(j%10==0):
           continue
       c = int(a[0])/(j%10)
       
       
       if(c==(i/j)):
           print(i,j,c)
           m=m*c
print(m)
           
           
   
    

        
