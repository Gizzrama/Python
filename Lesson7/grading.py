maths = int(input("Enter your marks for math: "))
english = int(input("Enter your marks for english: "))
science = int(input("Enter your marks for science: "))
commerce = int(input("Enter your marks for commerce: "))
geography = int(input("Enter your marks for geography: "))
print(f"{maths} \n{english} \n{science} \n{commerce} \n{geography}")

total = maths + english + science + commerce + geography
average = int(total/5)

if average in range(91, 100):
    print("You are an A student")

elif average in range(81, 90):
    print("You are an B student")

elif average in range(71, 80):
    print("You are a C student")

elif average in range(61, 70):
    print("You are a D student")

else:
    print("Please enter a valid number")