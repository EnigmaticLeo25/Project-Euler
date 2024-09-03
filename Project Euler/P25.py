a=1
b=1
c=0
for i in range(10000):
   c=a+b
   a=b
   b=c
   s= str(c)
   l = len(s)
   if(l==1000):
       print(i+3)
       break

   print(c)