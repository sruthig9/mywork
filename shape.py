import turtle

sally = turtle.Turtle()

def star(length, color):
    sally.fillcolor(color)
    sally.begin_fill()

    x = 0
    while x < 5:
        sally.forward(int(length))
        sally.right(144)
        x = x+1
    sally.end_fill()

def triangle(length, color):
    sally.fillcolor(color)
    sally.begin_fill()
    
    x = 0
    while x < 3:
        sally.forward(int(length))
        sally.right(120)
        x = x+1
    sally.end_fill()

def circle(length, color):
    sally.fillcolor(color)
    sally.begin_fill()
    sally.circle(int(length))
    sally.end_fill()
    

input_shape = input("What shape do you want to draw?")
input_length = input("Choose how big your shape should be:")
input_color = input("What color?")
if input_shape == 'triangle':
    triangle(input_length, input_color)
elif input_shape == "circle":
    circle(input_length, input_color)
elif input_shape == "star":
    star(input_length, input_color)

turtle.done()