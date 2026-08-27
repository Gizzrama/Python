#Prompt: You will create a shopping discount calculator that asks for a bill amount, discount percentage, and number of people. 
#The program will calculate the discount, find the final amount, split the bill, catch invalid entries, handle division by zero, 
#and keep asking until the input is valid.

valid = False

while not valid:
    try:
        bill_amount = float(input("Enter the total bill amount: "))
        discount_percentage = float(input("Enter the discount percentage: "))
        people = int(input("Enter the total number of people: "))

        if bill_amount <= 0 or discount_percentage < 0 or people < 0:
            raise ValueError

        discount = bill_amount * (discount_percentage / 100)
        final_amount = bill_amount - discount
        bill_split = final_amount/people

    except ValueError:
        if bill_amount<= 0:
            print("You can't have paid nothing if you dined at our restaurant. Please enter a higher value.")
            print("\n")

        elif discount_percentage < 0:
            print("Discount percentage can't be negative. Please enter a higher value.")
            print("\n")

        elif people < 0:
            print("People can't be negative. Enter a higher value.")
            print("\n")
            
        else:
            pass

    except ZeroDivisionError:
        print("There can't be zero people. Please enter a higher value.")
        print("\n")
    else:
        print("\n")
        print("--FINAL BILL--")
        print("Discount Percentage: ", discount_percentage)
        print("Discount: ", discount)
        print("Total: ", final_amount)
        print("Bill Split: ", bill_split)
        valid = True
    finally:
        print("End billing. Next customer please")
        print("\n")


        

        
