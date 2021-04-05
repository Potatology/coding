from turtle import*

myTurtle = Turtle()
window = myTurtle.getscreen()

def drawSpiral(myTurtle, len):
    if len > 0:
        myTurtle.forward(len)
        myTurtle.right(90)
        myTurtle.forward(len)
        myTurtle.right(33)
        myTurtle.forward(len//2)
        drawSpiral(myTurtle, len - 5)

def tree(len, t):
    if len > 5:
        t.forward(len)
        t.right(20)
        tree(len-15, t)
        t.left(40)
        tree(len-10, t)
        t.right(20)
        t.backward(len)

#drawSpiral(myTurtle, 200)
tree(40, myTurtle)
window.exitonclick()