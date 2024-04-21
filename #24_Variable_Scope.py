# scope = The region that a variable is recognized. A vaiable is only available from inside the region it is created. A global and locally scoped versions of a vriable can be created.

name = "Császár" # gobal scope (available inside & outside functions)

def display_name():
    name = "Daniel" #local scope (available only inside this function)
    print(name)

print(name)
display_name()