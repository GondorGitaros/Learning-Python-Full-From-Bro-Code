# *args = parameter that will pack all arguments into a tuple. Useful so that a function can accept a verying amout of arguments


#csak szórakoztam egy kicsit:

#def add(*args):
#    sum = 0
#    for i in args:
#        sum += i
#        if i == args[-1]:
#            print(str(i), end="")
#            print(" = " + str(sum))
#        else:
#            print(str(i) + " + ",end="")
#    return sum
#add(2,7,43,321,40,123,0,12,56)



def add(*args):
    sum = 0
    args = list(args)
    args.append(0)
    for i in args:
        print(i)
    for i in args:
        sum = sum + i
    return sum

print(add(1,2,3,54,5,))