import turtle

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')

t=turtle.Turtle()
t.speed(0)

#first page
t_ground = turtle.Turtle()
t_ground.penup()
t_ground.pencolor("snow1")
t_ground.fillcolor('snow1')
t_ground.speed(0)
t_ground.goto(-1000, -100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto (1000, -100)
t_ground.goto(1000, -1000)
t_ground.goto(-1000, -1000)
t_ground.goto(-1000, -100)
t_ground.end_fill()



t.penup()
t.goto(-100,-140)
t.pendown()
t.fillcolor('whitesmoke')
t.begin_fill()
t.circle(60)
t.end_fill()


t.penup()
t.goto(-100,-40)
t.pendown()
t.fillcolor('whitesmoke')
t.begin_fill()
t.circle(45)
t.end_fill()

# third circle
t.penup()
t.goto(-100,40)
t.pendown()
t.fillcolor('whitesmoke')
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-112,75)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(-90,75)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(-100,63)
t.pendown()
t.fillcolor('orange')
t.begin_fill()
t.circle(3)
t.end_fill()



t.penup()
t.goto(-100,50)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-112,55)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(-120,63)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-80,63)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-87,55)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(-135,0)
t.pendown()
t.fillcolor('goldenrod4')
t.begin_fill()
t.goto(-170, -50)
t.goto(-175, -40)
t.goto(-140,0)
t.goto(-135,0)
t.end_fill()





t.pensize(5)
t.penup()
t.goto(-30,-40)
t.pendown()
t.pencolor("goldenrod4")
t.goto(-65, 0)


t.pencolor('black')

t.penup()
t.goto(-100,-20)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(-100,-60)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()
t.goto(-100,-100)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()



t.penup()
t.pencolor('white')
t.goto(300,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.pencolor('white')
t.goto(200,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.pencolor('white')
t.goto(100,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.pencolor('white')
t.goto(0,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()



t.penup()
t.pencolor('white')
t.goto(-100,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.pencolor('white')
t.goto(-200,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.pencolor('white')
t.goto(-300,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()



t.pensize(9)
t.penup()
t.goto(-30,-40)
t.pendown()
t.pencolor("red")
t.left(70)
t.forward(30)
t.left(280)
t.forward(15)
t.left(280)
t.forward(8)


t.pensize(30)
t.penup()
t.goto(200,-140)
t.pendown()
t.pencolor("red")
t.left(180)
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)

t.pensize(5)
t.penup()
t.goto(190,-100)
t.pendown()
t.pencolor("green")
t.left(50)
t.forward(20)
t.left(180)
t.forward(20)
t.left(280)
t.forward(20)


t.penup()
t.pencolor('darkgrey')
t.goto(-100,290)
t.pendown()
t.fillcolor('darkgrey')
t.begin_fill()
t.circle(80)
t.end_fill()




t.penup()
t.goto(-240, -105)
t.penup()
t.goto(-10,100)
t.write("Merry Christmas!", font=("silly monkey", 24, "bold"), align="center")

#candycane200


#This is the last line of code
turtle.done()