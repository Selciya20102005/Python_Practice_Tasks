numbers = list(map(int, input("Enter numbers: ").split()))
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)