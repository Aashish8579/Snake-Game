import turtle
import random
import time

delay = 0.1  # for time
score = 0
highestscore = 0

# snake bodies
bodies = []

# Getting a screen  |  canvas
s = turtle.Screen()  # To get a screen
s.title("nibba nibbi game")   # It will give title as a snake game
s.bgcolor("gray")
s.setup(width=600, height=600)

# Create Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")  # color inside of the square
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# Scoreboard
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("green")
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score: 0  Highest Score: 0", align="center", font=("Courier", 24, "normal"))

# Movement functions
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Update scoreboard
def update_scoreboard():
    sb.clear()
    sb.write(f"Score: {score}  Highest Score: {highestscore}", align="center", font=("Courier", 24, "normal"))

# Event handling - Key mappings
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# Main loop
while True:
    s.update()  # this is to update the screen

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.direction = "stop"

        # Hide snake bodies
        for body in bodies:
            body.hideturtle()
        bodies.clear()

        # Reset score
        score = 0
        delay = 0.1

        # Update scoreboard
        update_scoreboard()

    # Check collision with food
    if head.distance(food) < 20:
        # Move food to a new random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the length of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)

        # Increase score
        score += 10

        # Reduce delay to speed up the game
        delay -= 0.001

        # Update highest score
        if score > highestscore:
            highestscore = score

        # Update scoreboard
        update_scoreboard()

    # Move snake body segments
    for index in range(len(bodies)-1, 0, -1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with the snake's own body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the bodies
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            score = 0
            delay = 0.2

            # Update scoreboard
            update_scoreboard()

    time.sleep(delay)

s.mainloop()
