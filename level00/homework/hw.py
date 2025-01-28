from turtle import*


#we wont to paint a house 


#step 1: draw a square 
speed(3)
width(5)
color("green")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square 

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()
#end of a door

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(120)
forward(120)
left(62)
forward(115)
end_fill()

penup()
goto(170,170)
pendown()

color("red")
begin_fill()
right(30)
forward(50)
left(88)
forward(55)
left(88)
forward(50)
left(92)
forward(55)

end_fill()

penup()
goto(97,97)
penup()

color("red")
left(7)
forward(14)

pendown()
begin_fill()
color("red")
left(83)
forward(50)
right(90)
forward(55)
right(90)
forward(50)
right(89)
forward(55)
end_fill()

exitonclick()