
def changeX(x):
    if x == -10:
        return
    x = x - 1
    changeX(x)
    print(x)

changeX(1)
    
