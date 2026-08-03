total_homework = 4
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
        print("Have some freetime")
    
    task_status = input("Is your task finished? Enter yes or no")

    if task_status == "yes":
        print("Good Job!")
        completed_count+=1
        task_num+=1
        print(total_homework - completed_count)

    elif task_status == "no":
        print("You got this.")
    
    else:
        print("Please enter either yes or no.")


print("Good work! You have completed all your homework!")

safety_count = 0

while True:
    
    
