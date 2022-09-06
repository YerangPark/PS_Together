# import turtle

# turtle.shape("turtle")
# turtle.write(turtle.position())
# turtle.forward(50)
# turtle.write(turtle.position())
# turtle.left(90)
# turtle.forward(50)
# turtle.write(turtle.position())

from turtle import*
color('red', 'yellow')

begin_fill()

while True:
    forward(200)
    left(199)
    if abs(pos()) < 1:
        break

end_fill()