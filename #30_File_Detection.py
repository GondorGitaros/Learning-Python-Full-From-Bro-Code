import os
path = "C:\\Users\\csasz\\OneDrive\\Asztali gép\\folder"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("The Location is a directiory!")
else:
    print("That location doesn't exists!")