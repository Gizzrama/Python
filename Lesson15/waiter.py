#In this piece of code, we are trying to calculate the final bill.
def total_calculator(total, tip_percentage):
    bill_amount = tip_percentage * 0.01 + total
    final_bill = round(bill_amount, 2)# --> The round() function in python is used to round any non-whole number to the nearest decimal places. Here, it is to 2 d.p.
    return final_bill

total = float(input("What is the total?"))
tip_percentage = float(input('What is the tip percentage?'))

print(f"The final bill is:", total_calculator(total, tip_percentage))

