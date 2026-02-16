# Robot data using dictionary (data structure)

robot = {
    "name": "Robo",
    "age": 2,
    "skills": ["Talking", "Walking", "Dancing", "Math Help"]
}

print("Hello! I am a robot 🤖")
print("My name is", robot["name"])
print("My age is", robot["age"], "years")

print("My skills are:")
for skill in robot["skills"]:
    print("-", skill)
