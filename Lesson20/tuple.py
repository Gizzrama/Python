tuple1 = (1, 2, 3.4, "Srihari", True)
tuple2 = tuple(reversed(tuple1))

while True:
    print(f"The elements present in the tuple are", tuple1)
    print(f"The first element stored in this tuple is", tuple1[0])
    print(f"The last element in the tuple is", tuple1[-1])

    print(f"The first three elements are", tuple1[0:3])
    print(f"The last three element in the tuple are", tuple1[-4:-1])
    print("The reverse order of the tuple is", tuple2)
    break

