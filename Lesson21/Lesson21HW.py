# You will create a small student subject record system. The program stores student details inside a dictionary, searches for records, 
# adds a new student, updates a subject list, removes duplicate student entries, removes one record using pop(), checks the final length,
# and prints each remaining record clearly.

student = {
    "student1":{"Name" : "Ben", "Class" : "7B", "Subject" : "Mathematics", "Marks" : 97, "Grade" : "A"},
    "student2":{"Name" : "Andrew", "Section" : "6A", "Subject" : "Mathematics", "Marks" : 95, "Grade" : "A"},
    "student3":{"Name" : "Harry", "Section" : "8C", "Subject" : "Mathematics", "Marks" : 87, "Grade" : "B"},
    "student4":{"Name" : "James", "Section" : "9B", "Subject" : "Mathematics", "Marks" : 89, "Grade" : "B"},
}

print("Student Record:", student)

print("Harry's Record:", student.get("student3"))
print("Andrew's Record:", student.get("student2"))

student["student5"] = {"Name" : "Marcus", "Section" : "5C", "Subject" : "Mathematics", "Marks" : 86, "Grade" : "B"}
print("Record of added student:", student["student5"])



