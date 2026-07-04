cart = [
    ("Laptop", 50000),
    ("Mouse", 500),
    ("Keyboard", 1500)
]
for item, price in cart:
    print(f"{item}: {price}")
most_expensive = max(cart, key=lambda x: x[1])
cheapest = min(cart, key=lambda x: x[1])
print("Most expensive:", most_expensive)
print("Cheapest:", cheapest)