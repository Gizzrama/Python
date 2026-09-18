#You will create a simple snack counter for a school setting. 
#The program will store snacks in two sets, add a new snack, find snacks that appear in both boxes, and use an array to store snack counts. 
#Finally, it will count a selected value, reverse the array, and print a clear summary.
import array as arr

lunch_box1 = {"guacomole", "coke", "nachos", "chocolate bar", "Lays"}
lunch_box2 = {"brownie", "burger", "hash brown", "ketchup"}
lunch_box2.add("juice")
        

snack_count = arr.array("i", [4, 7, 8])
snack_count.insert(0, 3)
snack_count.append(9)
snack_count.reverse()


print("\nSUMMARY")
print("First lunch box:", lunch_box1)
print("Second lunch box:", lunch_box2)
print("Added snack in lunch box:", )
print("Shared snacks:", lunch_box1.intersection(lunch_box2))
print("Final snack count:", snack_count)