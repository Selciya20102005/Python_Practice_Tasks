a=0
b=1
c=a+b
n=int(input())
print(a)
print(b)
for i in range(2,n):
 a,b=b,a+b
 print(b)