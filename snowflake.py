import turtle

def x_turtle():
    x = turtle.Turtle()
    x.pencolor(0, 0, 1.0)
    x.pensize(6)
    
    for _ in range(5):
        
        x.left(90)
        
        x.pencolor(0, 0, 0.9)
        x.pensize(4)
        x.left(30)
        x.forward(100)
        x.back(100)
        x.right(30)

        x.pencolor(0, 0, 1.0)
        x.pensize(6)

        
        x.forward(140)
        x.penup()
        x.back(140)
        x.pendown()
        x.right(15)
        x.forward(20)
        x.left(30)
        x.forward(15)
        x.right(50)
        x.forward(70)
        x.left(145)
        x.forward(45)
        x.right(150)
        x.forward(30)
        x.left(80)
        x.forward(20)
        x.right(25)
        x.forward(25)

        x.left(150)
        x.forward(25)
        x.right(25)
        x.forward(20)
        x.left(80)
        x.forward(30)
        x.right(150)
        x.forward(45)
        x.left(145)
        x.forward(70)
        x.right(50)
        x.forward(15)
        x.left(30)
        x.forward(20)

        



    
x_turtle()

