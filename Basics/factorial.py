fact=1
num=int(input())
if num==0 or num==1:
  print(1)
else:
  for i in range(1,num+1):
    fact*=i
  print(fact)