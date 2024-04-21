# 2D(multi dimensional) lists = a list of lists


drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]

print(food[0][0])



#ezt mar csak en tettem hozza
for i in food:
    for j in i:
        if j == "ice cream":
            print(j)
            break
        print(j + ", ", end="")