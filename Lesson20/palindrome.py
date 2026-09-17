number = eval(input("Enter a few numbers separated by a comma:"))
palindrome = tuple(number)
#tuple1 = (1, 2, 3, 3, 5, 1)
tuple2 = tuple(reversed(palindrome))

if tuple2 == palindrome:
    print("The tuple is a palindrome")

else:
    print("The tuple is not a palindrome")


#ANOTHER WAY
start = 0
end = len(palindrome) - 1
answer = True
while start <= end:
    if palindrome[start] != palindrome[end]:
        answer = False
        break 
    start += 1
    end -= 1

if answer == True:
    print("The tuple is a palindrome")

else:
    print("The tuple is not a palindrome")
    


    