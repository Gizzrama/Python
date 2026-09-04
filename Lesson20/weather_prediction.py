t = (0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1)
sunny = 0
rainy = 0

for i in range(0, len(t)):
    if t[i] == 1:
        sunny = sunny + 1

    else:
        rainy = rainy + 1

if sunny > rainy:
    print("It is a sunny day")

else:
    print("It is a rainy day")



    