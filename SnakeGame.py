import turtle
import math
from random import randint
from time import sleep


pos = [0, 0]
# tela
sc = turtle.Screen()

sc.bgcolor("black")
sc.title("Snake Game")
sc.setup(sc.window_height())
sc.tracer(False)

mtari = 2
numero_linhas = mtari
linhas = []
for i in range(numero_linhas):
    linhas.append(turtle.Turtle())
ly = -(sc.window_height()/2)
for i in range(len(linhas)-1):
    linhas[i].color("red")
    ly = ly + (sc.window_height() / numero_linhas)
    linhas[i].hideturtle()
    linhas[i].penup()
    linhas[i].pensize(2)
    linhas[i].sety(ly)
    linhas[i].setx(-(sc.window_width()/2))
    linhas[i].pendown()
    linhas[i].setx(sc.window_width()/2)

numero_colunas = mtari
colunas = []
for i in range(numero_colunas):
    colunas.append(turtle.Turtle())
lx = -(sc.window_width()/2)
for i in range(len(colunas)-1):
    lx = lx + (sc.window_width() / numero_colunas)
    colunas[i].hideturtle()
    colunas[i].penup()
    colunas[i].pensize(2)
    colunas[i].setx(lx)
    colunas[i].sety(-(sc.window_height()/2))
    colunas[i].pendown()
    colunas[i].sety(sc.window_height()/2)

# Snake
snake_speed = 26
snake = []
for i in range(1):
    snake.append(turtle.Turtle())

for turtles in snake:
    turtles.penup()
    turtles.color("white")
    turtles.shape('square')
    turtles.shapesize(1.2)


# fruit
fruit = turtle.Turtle()
fruit.penup()
fruit.color("red")
fruit.shape('circle')
fruit.shapesize(1.2)
fruit.setpos(randint(-200, 200), randint(-200, 200))

# direção da Snake
# 0 = parado
# 1 = cima
# 2 = direta
# 3 = baixo
# 4 = esquerda

direction = 2

def setDirUp():
    global direction
    if direction != 3:
        direction = 1


def setDirDown():
    global direction
    if direction != 1:
        direction = 3


def setDirRight():
    global direction
    if direction != 4:
        direction = 2


def setDirLeft():
    global direction
    if direction != 2:
        direction = 4


def isCollision(t1, t2, dis):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False


sc.listen()
sc.onkey(setDirUp, "Up")
sc.onkey(setDirDown, "Down")
sc.onkey(setDirRight, "Right")
sc.onkey(setDirLeft, "Left")
sc.onkey(sc.bye, "Escape")




x = 0
ultimo_comer = 1000
isStarted = False
while True:
    sc.update()
    if direction == 1:
        pos[1] += snake_speed
    if direction == 3:
        pos[1] -= snake_speed
    if direction == 2:
        pos[0] += snake_speed
    if direction == 4:
        pos[0] -= snake_speed


    if isCollision(snake[x], fruit, 20):
        snake.append(turtle.Turtle())
        snake[-1].penup()
        snake[-1].color("white")
        snake[-1].shape('square')
        snake[-1].shapesize(1.2)
        snake[-1].speed(0)
        snake[-1].setpos(1000, 1000)
        snake[-1].hideturtle()

        while True:
            fx = randint(-200, 200)
            if fx % snake_speed == 0:
                break
        while True:
            fy = randint(-200, 200)
            if fy % snake_speed == 0:
                break
        fruit.setpos(fx, fy)

    if x == len(snake)-1:
        x = 0
    else:
        x += 1

    for i in range(len(snake)):
        if snake[x] != snake[i]:
            if isCollision(snake[x], snake[i], 5):
                snake_speed = 0

    if snake_speed != 0:
        snake[x].setpos(pos)
    snake[x].showturtle()



    sleep(0.1)




sc.mainloop()
