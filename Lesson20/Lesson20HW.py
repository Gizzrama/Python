#You will create a tracker for a weekly habit. The program will store habit details in one tuple and daily completion values in another tuple. 
# It will check the tuple length, access specific days, slice selected day ranges, create a new tuple with one extra day, count completed and missed days, 
# and print a final summary.

true_count = 0
false_count = 0
status = False
habit = ("Gaming", True, 2, 120)
daily = (1, 1, 1, 1, 0, 0, 1)
daily1 = (1, 1, 1, 1, 0, 0, 1, 0)
print("Habit, its status, amount of days I do this and time in minutes:", habit)
print("Number of days I complete my daiy habits:", len(daily))

for i in daily:
    if i == 1:
        status = True
        true_count += 1
        

    else:
        status
        false_count += 1

print("The status of the first day of the week:", daily[0], status)
print("The status of the fourth day of the week:", daily[4], status)
print("Status for the first three days:", daily[0:3])
print("The status for weekends:", daily[5:7])
print("Number of completed days for daily habits:", true_count)
print("Number of missed days:", false_count)

