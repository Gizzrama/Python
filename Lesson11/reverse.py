number = int(input("Enter any number greater than 0: "))
reverse = 0
while number >0:
    n = number%10
    reverse = reverse*10 + n
    number = number//10

print(f"The reverese of this number is {reverse}")
