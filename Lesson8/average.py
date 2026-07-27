
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

avg = (a + b + c)/3
print(avg)


if avg > a and avg > b and avg > c:
    print("Average is higher than all numbers.")

elif avg > a and avg > b:
    print("Average is higher than a and b.")

elif avg > a and avg > c:
    print("Average is higher than a and c.")

elif avg > b and avg > c:
    print("Average is higher than b and c.")

elif avg > a:
    print("The average is greater than a.")

elif avg > b:
    print("The average is greater than b.")

elif avg > c:
    print("The average is greater than c.")

else:
    print("Invalid input")

