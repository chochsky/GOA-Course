# გავიმეოროთ ძველი მასალა

from turtle import *

width(10)
speed(30)

color("blue")
begin_fill()

forward(100)
left(120)
forward(100)
left(120)
forward(100)

end_fill()


penup()
goto(100, 0)
pendown()

color("red")
begin_fill()

left(60)
forward(100)
right(120)
forward(100)

end_fill()

exitonclick()