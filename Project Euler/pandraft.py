a=1
b=1
c=0
def pandigital(x):
    if("1" in x and "2" in x and "3" in x and "4" in x and "5" in x and "6" in x and "7" in x and "8" in x and "9" in x):
        return True
    return False
for i in range(1000000):
   c=a+b
   a=b
   b=c
   s= str(c)
   l = len(s)
   if(l>19):
        s1 = s[:9]
        s2 = s[l-9:]
        if(pandigital(s1) and pandigital(s2)):
            print(i+3)
            break
  
   