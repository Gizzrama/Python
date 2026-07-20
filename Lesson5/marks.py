print("Admission Eligibility Checker:")
maths = int(input("Enter your marks for math"))
science = int(input("Enter your marks for science"))
english = int(input("Enter your marks for english"))

total = maths + science + english
average = total/3

if maths >= 60 and science >= 50 and english >= 40 and average > 60:
    print("Congrats! You can take the admission")

else:
    print("Sorry, you are not eligible")
    

