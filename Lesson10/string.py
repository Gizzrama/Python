name = input("Enter anything: ").strip()

#for i in range(len(name) - 1, -1, -1):
   # print(name[i])
n = ""
for i in name:
    n = i + n

print(n)