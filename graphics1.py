import turtle
cir= turtle.Turtle()
cir.color("cyan")
cir.speed(0)

def draw_square():
    for side in range(4):
        cir.forward(100)
        cir.right(90)
        for side in range(4):
            cir.forward(50)
            cir.right(90)

cir.penup()
cir.back(20)
cir.pendown()

for squaare in range(80):
    draw_square()
    cir.forward(5)
    cir.left(5)
    
cir.hideturtle()
