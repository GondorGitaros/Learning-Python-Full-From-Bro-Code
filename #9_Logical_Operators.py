# Logical operators (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))
if temp >=0 and temp <=30:
    print("the temeratue is good today!")
    print("Go outside!")
elif not(temp >=0 and temp <=30):
    print("the temperatire os bad today!")
    print("stay inside!")
