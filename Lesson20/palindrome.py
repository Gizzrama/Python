tuple1 = (1, 2, 3, 3, 5, 1)
tuple2 = tuple(reversed(tuple1))

if tuple2 == tuple1:
    print("The tuple is a palindrome")

else:
    pass


#ANOTHER WAY
start = 0
end = len(tuple1) - 1
answer = True
while start <= end:
    if tuple1[start] != tuple1[end]:
        answer = False
        break 
    start += 1
    end -= 1

if answer == True:
    print("The tuple is a palindrome")

else:
    print("The tuple is not a palindrome")
    


    