total_homework = 3
completed_count = 0
task_num = 1

while task_num <= total_homework:
    if task_num == 1:
        print("Math Homework")
    
    elif task_num == 2:
        print("Business Homework")
    
    elif task_num == 3:
        print("English Homework")
    
    else:
        print("Please enter numbers 1 - 3 only.")
        continue
    
    task_status = input("Is your task finished? Enter yes or no: ").strip().lower()

    if task_status == "yes":
        print("Good Job!")
        completed_count+=1
        task_num+=1
        print(f"Tasks Remaining: {total_homework - completed_count}")
        
        

    elif task_status == "no":
        print("You got this.")
        
        
    
    else:
        print("Please enter either yes or no.")
        continue
        
print("\n")     
print("ALL HOMEWORK COMPLTETED! GOOD JOB!")
print("\n")
print("Here is an example of a while loop with a condition that does not change on its own.")

value = 1
safety_count = 0


while value == 1:
    print("This is a never ending loop since value is always equal to 1.")
    safety_count += 1

    if safety_count == 3:
        print("This loop will now break since the safety count is incremented by one after each comment, and")
        print("this if conditional statement tells us that if the safety count reached 3, then the code should break, which happened as you were reading this.")
        break


print("---THE FINAL SUMMARY---")
print("\n")
print("The original task count is ", total_homework)
print("The completed task count is ", completed_count)
print("The remaining task count is ", total_homework - completed_count)


    
    
