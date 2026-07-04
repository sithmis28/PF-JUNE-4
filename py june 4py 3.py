a=int(input("enter your units consumed:"))
if a<=30:
  bill=a*20
  print("bill is Rs:",bill)
else:
  if a<=60:
    bill=(30*20)+(a-30)*40
    print("bill is Rs:",bill)
  else:
    bill=(30*20)+(30*40)+(a-60)*60
    print("bill is Rs:",bill)
    
