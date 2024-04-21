#tuple = collection which is ordered and unchangeable used to group together related data

student = ("Daniel",16,"male")

print(student.count(16))
print(student.index("Daniel"))

for x in student:
    if x == student[-1]:
        print(str(x))
        break
    print(str(x) + ", ", end="")


if "Daniel" in student:
    print("Daniel is here")