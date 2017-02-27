import random
rmnum=random.randint(1,10)
i=1
while i<=3:
 i+=1
 tmp=input("please input a number")
 num=int(tmp)
 if num==rmnum:
   print("it is right")
 else:
   if num>rmnum:
     print(" it is too big")
   else:
     print(" it is too small")
print(" it\'s over")
