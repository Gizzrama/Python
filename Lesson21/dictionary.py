student = {
    "Name": "Xavier",
    "Age": 15
}

print(student)
print(student["Name"])
print(student.get("Age"))

student["Age"] = 17
print(student)

for i in student:
    print(i,":", student[i])

