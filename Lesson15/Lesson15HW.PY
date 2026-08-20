def total_bill(bill_amount, tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    return total

def seating_arrangements(guests):
    """This shows the total amount of seating arrangements for the number of guests dining at the restaurant"""
    if guests == 0 or guests == 1:
        return 1
    
    elif guests > 1:
        return guests * seating_arrangements(guests - 1)

    else:
        print("ERROR: Minimum value is 0")

guests = int(input("Welcome! How many are dining at our restaurant today?"))

    
print(total_bill(150, 20))
print(seating_arrangements(guests).__doc__)

print(f"The total number of seating arrangements for {guests} guests are {seating_arrangements(guests)}")
