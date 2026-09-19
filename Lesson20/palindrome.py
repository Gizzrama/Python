#One way to determine if the tuple is a palindrome or not
number = eval(input("Enter a few numbers separated by a comma:"))
palindrome = tuple(number)
tuple2 = tuple(reversed(palindrome)) #--> reveresed() can be applied to a tuple, one of the only functions that works on tuples

if tuple2 == palindrome:
    print("The tuple is a palindrome")

else:
    print("The tuple is not a palindrome")


#Another Way
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
    


    