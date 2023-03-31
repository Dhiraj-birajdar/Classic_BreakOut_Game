from turtle import Turtle, Screen


screen = Screen()
screen.setup(height=800, width=600)
colors = ['red', 'green', 'blue']
bricks = []


def draw_bricks():
    global bricks
    x = -276
    y = 370
    for r in range(4):
        y -= 1 * 22
        for c in range(13):
            t = Turtle('square')
            t.color(colors[c%3])
            t.speed(0)
            t.shapesize(1, 2)
            bricks.append(t)
            t.goto(x+c*45, y)


def move_left():
    pad.backward(20)


def move_right():
    pad.forward(20)


ball = Turtle('circle')
pad = Turtle('square')
pad.speed(0)
pad.shapesize(1, 4)
pad.goto(0, -380)
screen.listen()
screen.onkeypress(key='Left', fun=move_left)
screen.onkeypress(key='Right', fun=move_right)
draw_bricks()

screen.exitonclick()
