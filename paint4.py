import turtle

def draw_circle():
    window=turtle.Screen()
    window.bgcolor("yellow")

    pan=turtle.Turtle()

    a=60

    pan.color("red")
    pan.pensize(1)
   

    for n in range(1,11):
    
        pan.forward(100)
        pan.left(105)
        pan.forward(50)
        pan.right(75)
        pan.backward(100)
        pan.left(45)

    pan.right(120)
    pan.forward(200)
        
    window.exitonclick()

draw_circle()
