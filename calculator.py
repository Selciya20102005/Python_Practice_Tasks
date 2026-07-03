num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
operator = input("Enter operator: ")

match operator:
    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid operator")