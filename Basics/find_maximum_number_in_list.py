num_arr = list(map(int, input("Enter numbers: ").split()))
maximum = num_arr[0]
for num in num_arr:
    if num > maximum:
        maximum = num
print("Maximum Number:", maximum)