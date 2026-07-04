import json

profile = {
    "name": "Selciya K",
    "age": 20,
    "skills": ["Python", "React", "SQL"],
    "level": 4
}
with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

print("Profile saved successfully!")
with open("profile.json", "r") as file:
    data = json.load(file)
print(f"Name : {data['name']}")
print(f"Age  : {data['age']}")
print(f"Skills : {', '.join(data['skills'])}")
print(f"Level : {data['level']}")