import time
# for loop = a statement that will execute it's block of code a limited amount of times
#while loop = unlimited
#for loop = limited

for i in range(10):
	print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "Császár Dániel":
    print(i)


for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!")