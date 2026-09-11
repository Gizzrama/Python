fruit_basket1 = {"apple", "mango", "watermelon", "kiwi", "blueberry", "banana"}
fruit_basket2 = {"pineapple", "muskmelon", "strawberry", "grapes"}

print("The fruits in the first basket are", fruit_basket1)
print("The fruits in the second basket are", fruit_basket2)

fruit_basket2.add("mango")
print("The fruits in the second basket are", fruit_basket2)

intersect = fruit_basket1.intersection(fruit_basket2)
print("The common fruit in both the baskets is", intersect)

for i in fruit_basket1:
    print(i)

    

