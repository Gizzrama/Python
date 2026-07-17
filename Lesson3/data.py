#DATATYPES & USER INPUT 
name = input("Please type your name")
print(f"Hello, I am your agent {name}")
agent_number = int(input("Enter your agent number"))
speed_rating = float(input("Enter your speed rating"))
mission_count = int(input("Enter your mission count"))
is_active = bool(input("Enter True or False"))
print(f"{agent_number}, {speed_rating}, {mission_count}, {is_active}")
print(type(agent_number), type(speed_rating), type(mission_count), type(is_active))

#TYPECASTING
age = "14"
print(f"The age is {age}, The type is {type(age)}")
a = int(age)
print(f"The age is {a}, The type is {type(a)}")

marks = 90.99
print(f"The age is {marks}, The type is {type(marks)}")
m = int(marks)
print(f"The age is {m}, The type is {type(m)}")

#STRING OPERATIONS
#Indexing
name = input("Please enter your name")
print(name)
print(name[0])
print(name[2])
print(name[-1])
print(name[-2])

#Slicing
print(name[0:4])

#Concentation
first_name = "Srihari"
surname = "T"
print(first_name + surname)



