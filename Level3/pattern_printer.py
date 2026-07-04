rows=int(input("enter the row_count:"))
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=' ')
    print()