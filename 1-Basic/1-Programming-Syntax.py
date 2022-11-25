x = "awesome"


def myFunction():
    global x
    x = "fantastic"
    print("Python is: " + x)


myFunction()

print("Python is: " + x)
