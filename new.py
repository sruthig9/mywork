from turtle import *

shape("arrow")
bgcolor("black") 
title("Colourful Spiral") 
pensize(2)
colormode(255) #Setting our color
               #mode for rgb values
speed(0)

w=600
h=600
setup(width=w, height=h)
penup()
goto((-w/2)+10,(h/2)-15)
pendown()

def drawSpiral(lineLength,colorIntensity):
    if lineLength > 20: #Terminating Case
        colorAdj=colorIntensity-1
        adj=lineLength-30
        pencolor(colorAdj,0,255)
        forward(adj)
        right(90)
        drawSpiral(adj+25,colorAdj) #Modified Call

drawSpiral(w,255) #Base Case
hideturtle()