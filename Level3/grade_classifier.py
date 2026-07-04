score = int(input("Enter score: "))
if score >= 95:
    print("Grade A")
elif score >= 85:
    print("Grade B")
elif score >= 75:
    print("Grade C")
elif score >= 65:
    print("Grade D")
else:
    print("Grade F")

print("Pass" if score >= 65 else "Fail")