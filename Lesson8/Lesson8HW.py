#GROCERY COST COMPARISON TOOL
rice_price = 17
milk_price = 8
fruit_price = 12
baskets = 3
members = int(input("How many people are in your family including pets? "))

basket_cost_per_person = (rice_price + milk_price + fruit_price) * baskets / members
print("Basket cost per person: ", basket_cost_per_person)

grocery_items = int(input("enter the total number of grocery items: "))

if grocery_items % members == 0:
    print(f"All the items can be shared equally among {members} people")

else:
    print(f"The total number of items cannot be shared equally among {members} people.")


recorded_average = 25
incorrect_weekly_cost = 35
correct_weekly_cost = 38
weeks = 3

recorded_total = recorded_average * weeks
print("The recorded total is: ", recorded_total)

correct_total = recorded_total - incorrect_weekly_cost + correct_weekly_cost
correct_average = correct_total / weeks
print("The correct total is: ", correct_total) 

Store_A = 23
Store_B = 26
Store_C = 25

if correct_average < Store_A:
    print("The average is less than store A's average.")

elif correct_average > Store_A:
    print("The average is greater than store A's average.")

elif correct_average == Store_A:
    print("The average is equal to store A's average.")

elif correct_average < Store_B:
    print("The average is less than store B's average.")

elif correct_average > Store_B:
    print("The average is greater than store B's average.")

elif correct_average == Store_B:
    print("The average is equal to store B's average.")

elif correct_average < Store_C:
    print("The average is less than store C's average.")

elif correct_average > Store_C:
    print("The average is greater than store C's average.")

elif correct_average == Store_C:
    print("The average is equal to store C's average.")

else:
    print("Enter a integer or float value")


