
def total_calculator(total, tip_percentage):
    bill_amount = tip_percentage * 0.01 + total
    final_bill = round(bill_amount, 2)
    return final_bill

total = float(input("What is the total?"))
tip_percentage = float(input('What is the tip percentage?'))

print(total_calculator(total, tip_percentage))