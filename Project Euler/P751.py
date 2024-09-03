import math
b1 = 2.223561019313554106173177
for i in range(15):
    bn = math.floor(b1)*(b1-math.floor(b1) +1)
    b1 = bn
    an = math.floor(bn)
    print(an)
   