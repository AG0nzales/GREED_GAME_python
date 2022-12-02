
import turtle
import random


score = 0


wn = turtle.Screen()
wn.title("GEMS & ROCKS GAME")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(8)

# Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

#GEMS
gems = []

# Add the gem
for _ in range(20):
    gem = turtle.Turtle()
    gem.speed(0)
    gem.shape("classic")
    gem.color("blue")
    gem.penup()
    gem.speed = random.randint(2, 4)
    gem.goto(0, 250)
    gems.append(gem)
    

#rocks
rocks = []

rock_color = ["red", "yellow", "green", "gray", "pink"]
# Add the rock
for _ in range(20):
    rock = turtle.Turtle()
    rock.speed(0)
    rock.shape("square")
    rock.color(random.choice(rock_color))
    rock.penup()
    rock.speed = random.randint(2, 4)
    rock.goto(100, 250)
    rocks.append(rock)


# MAKE SCORE
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("SCORE: {}".format(score), align="center", font=font)


# Functions
def go_left():
    player.direction = "left"
    
def go_right():
    player.direction = "right"
    
# Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main game loop
while True:
    #UPDATE SCREEN
    wn.update()
    
    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)
    
    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    #GEMs MOVEMENT
    # gem.sety(gem.ycor() - 3)
    for gem in gems:
        y = gem.ycor()
        y -= gem.speed
        gem.sety(y)
        
        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            gem.goto(x, y)

        # Check for collision
        if gem.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            gem.goto(x, y)
            score += 10
            pen.clear()
            pen.write("SCORE: {}".format(score), align="center", font=font)
    
    #ROCKS MOVEMENT
    # rock.sety(rock.ycor() - 3)
    for rock in rocks:
        y = rock.ycor()
        y -= rock.speed
        rock.sety(y)
        
        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            rock.goto(x, y)

        # Check for collision
        if rock.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            rock.goto(x, y)
            score -= 10
            pen.clear()
            pen.write("SCORE: {}".format(score), align="center", font=font)


wn.mainloop()