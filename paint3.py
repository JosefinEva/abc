import turtle

def draw_circle():
    window=turtle.Screen()
    window.bgcolor("yellow")

    panpan=turtle.Turtle()

    panpan.speed(8)
    panpan.color("purple")
   
    for i in range(1,7):
        panpan.right(60)
        panpan.circle(100)


    maige=turtle.Turtle()

    maige.speed(5)
    maige.color("purple")
    maige.right(90)
    maige.forward(250)
    
        
    window.exitonclick()

draw_circle()
