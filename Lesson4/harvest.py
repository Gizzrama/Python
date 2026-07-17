name = input("Please enter your name")
print(name)
field1 = 5
field2 = 6
field3 = 7
field4 = 8
field5 = 9
total = field1 + field2 + field3 + field4 + field5
print("Total harvest is", total)
average = total/5
print("Average per field is", average)
price_per_kg = int(input("Enter price per kg"))
earnings = price_per_kg * total
print("Total earnings are", earnings)
bags = total//4
leftover = total%4
print("There are", bags, "completely packed")
print("There is", leftover, "that is leftover")
x = 15
y = 5
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x>=y)
print(x<=y)

#ASSIGNMENT OPERATORS
x = 15
y = 5
x = x + 5
print(x)
x+=y   
print(x)     #it is x = x+y
x-=y
print(x)
x*=6
print(x)
x/=3
print(x)
x//=5
print(x)
x%=7
print(x)

