#list = used to stroe multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti"]

food[0] = "sushi"

print(food[0])

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()

for i in food:
    print(i + ", ", end="")