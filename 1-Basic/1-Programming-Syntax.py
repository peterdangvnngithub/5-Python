x = "awesome"


def myFunction():
    global x
    x = "fantastic"
    print("Python is: " + x)


def forLoop():
    start = 2
    stop = 5
    for i in range(start, stop):
        print("Index: " + str(i))

forLoop()
