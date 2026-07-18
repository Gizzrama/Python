#ARITHMETIC OPERATORS
# +, -, *, /, //(floor division: divides two operands(integers) and rounds the result to the nearest integer), 
#% (Modulus: shows the remainder of the division), (**): Exponentiation
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
print("There are", bags, "bags completely packed")
print("There is", leftover, "that is leftover")

#COMPARISON OPERATORS --> Always result in true or false statements
# (==): If x is equal to y | (!=): Not equal to, (<): Less than, (>): Greater than, 
#(<=): Less than or equal to, (>=): Greater than or equal to
x = 15
y = 5
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x>=y)
print(x<=y)

#ASSIGNMENT OPERATORS --> Assigning a value to a variable
#(+=): to be read x = x+y, (-=): to be read as x = x-y ...
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

#| Operator | Name | Equivalent Syntax | Example (Assuming x = 5) |
#| :--- | :--- | :--- | :--- |
#| `=` | Simple Assignment | x = y | x = 5 |
#| `:=` | Walrus Operator | `(x := y)` | `if (n := len(a)) > 10:` |
#| `+=` | Addition Assignment | `x = x + y` | `x += 3` (x becomes 8) |
#| `-=` | Subtraction Assignment | `x = x - y` | `x -= 2` (x becomes 3) |
#| `*=` | Multiplication Assignment | `x = x * y` | `x *= 4` (x becomes 20) |
#| `/=` | Division Assignment | `x = x / y` | `x /= 2` (x becomes 2.5) |
#| `//=` | Floor Division Assignment | `x = x // y` | `x //= 2` (x becomes 2) |
#| `%=` | Modulus Assignment | `x = x % y` | `x %= 3` (x becomes 2) |
#| `**=` | Exponentiation Assignment | `x = x ** y` | `x **= 2` (x becomes 25) |
#| `@=` | Matrix Multiplication | `x = x @ y` | `x @= y` (Used in NumPy) |
#| `&=` | Bitwise AND Assignment | `x = x & y` | `x &= 3` (x becomes 1) |
#| `\|=` | Bitwise OR Assignment | `x = x \| y` | `x \|= 3` (x becomes 7) |
#| `^=` | Bitwise XOR Assignment | `x = x ^ y` | `x ^= 3` (x becomes 6) |
#| `>>=` | Right Shift Assignment | `x = x >> y` | `x >>= 1` (x becomes 2) |
#| `<<=` | Left Shift Assignment | `x = x << y` | `x <<= 1` (x becomes 10) |
 

