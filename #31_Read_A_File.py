
try:
    with open("C:\\Users\\csasz\\OneDrive\\Asztali gép\\test.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")