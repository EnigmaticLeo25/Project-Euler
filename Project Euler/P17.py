l1={1:'one',2:"two",3:'three',4:'four',5:"five",6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred'}

s="onethousand"
for i in range(1,1000):
    if(i%100==0):
        d = int(i/100)
        s=s+l1[d]+l1[100]
        continue
    if(i>100):
        d=int(i/100)
        s=s+l1[d]+l1[100]+'and'
        
        
    d= i%100
    if(d<20):
        s=s+l1[d]
    else:
        m = int(d/10)
        me = d%10
        if(me!=0):
            s=s+l1[m*10]+l1[me]
        else:
            s=s+l1[m*10]
            
                
print(s)
print(len(s))



