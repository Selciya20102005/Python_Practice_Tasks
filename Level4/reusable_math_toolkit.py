import math


def area_circle(r):
    return math.pi * (r ** 2)

def area_rectangle(w, h):
    return w * h

def is_even(n):
    return n % 2 == 0

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result



radius = 5
width = 10
height = 6
number = 8
fact_num = 5

print(f"Area of Circle: {area_circle(radius):.2f}")
print(f"Area of Rectangle ({width}x{height}) : {area_rectangle(width, height)}")
print(f"Is {number} Even?: {is_even(number)}")
print(f"Factorial of {fact_num}: {factorial(fact_num)}")