from datetime import datetime

def calculate_age(dob):

    birth_date = datetime.strptime(dob, "%Y-%m-%d")

    today = datetime.today()

    age = today.year - birth_date.year

    # Birthday not yet reached this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    days_lived = (today - birth_date).days

    day_name = birth_date.strftime("%A")

    return age, days_lived, day_name


dob = input("Enter your Date of Birth (YYYY-MM-DD): ")

age, days, weekday = calculate_age(dob)


print(f"Age : {age} years")
print(f"Days Lived : {days}")
print(f"Born On : {weekday}")