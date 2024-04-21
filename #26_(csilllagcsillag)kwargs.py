# **kwargs = őarameter that will pack all arguments into a dictionary. Useful so that a function can accept a verying amout of keword arguments.

def hello(**kwargs):
    #print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(str(value),end=" ")

hello(a="Császár",b="Középső",c="Dániel")