# You will create a small student subject record system. The program stores student details inside a dictionary, searches for records, 
# adds a new student, updates a subject list, removes duplicate student entries, removes one record using pop(), checks the final length,
# and prints each remaining record clearly.

student = {
    "student1" : {"Name" : "Ben", "Section" : "7B", "Subject" : "Mathematics", "Marks" : 97, "Grade" : "A"},
    "student2" : {"Name" : "Andrew", "Section" : "6A", "Subject" : "Science", "Marks" : 95, "Grade" : "A"},
    "student3" : {"Name" : "Harry", "Section" : "8C", "Subject" : "English", "Marks" : 87, "Grade" : "B"},
    "student4" : {"Name" : "Ben", "Section" : "7B", "Subject" : "Mathematics", "Marks" : 97, "Grade" : "A"},
}

print("Student Record:", student)

print("Harry's Record:", student.get("student3"))
print("Andrew's Record:", student.get("student2"))

student["student5"] = {"Name" : "Marcus", "Section" : "5C", "Subject" : "History", "Marks" : 86, "Grade" : "B"}
print("Record of added student:", student["student5"])

student["student2"]["Subject"] = "Music"
print("\nAfter updating student2's record:", student.get("student2"))

seen = []
duplicate = []

for i in student:
    kid = student[i]
    if kid in seen:
        duplicate.append(i)

    else:
        seen.append(kid)

for j in duplicate:
    student.pop(j)

print("Remaining number of students in the record", len(student))



