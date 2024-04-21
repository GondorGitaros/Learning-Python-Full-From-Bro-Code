# dictionary = a changeable, unordered collectoin of unique key:value pairs. Fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"Washington DC", "India":"New Debli", "China":"Beijing", "Russia":"Moscow"}


capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("China")
capitals.clear()

print(capitals["Russia"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)