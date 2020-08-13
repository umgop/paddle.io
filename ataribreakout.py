import turtle as t
import random
import time

# Breakout Game
# https://en.wikipedia.org/wiki/Breakout_(video_game)
# https://elgoog.im/breakout/
# Advanced Version: https://www.youtube.com/watch?v=8u4yAr91988

screen = t.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)
t.speed(0)


# TODO: Draw a Border along the walls (Edges)
# Hint: use t.forward and t.left
border = t.Turtle()
border.penup()
border.goto(-400, -400)
border.color("maroon")
border.pensize(200)
border.pendown()

border.forward(800)
border.left(90)
border.forward(800)
border.left(90)
border.forward(800)
border.left(90)
border.forward(800)


border.hideturtle()



# Create ball
ball = t.Turtle()
ball.color("red")
ball.shape("circle")
ball.penup()

# Create Obstacles
obs = []
x =-280
y = 280
for _ in range(10):
  p1 = t.Turtle()
  p1.color("yellow")
  p1.shape("square")
  p1.penup()
  p2 = t.Turtle()
  p2.color("blue")
  p2.shape("square")
  p2.penup()
  p3 = t.Turtle()
  p3.color("blue")
  p3.shape("square")
  p3.penup()
  p4 = t.Turtle()
  p4.color("yellow")
  p4.shape("square")
  p4.penup()
  
  p1.goto(x, y)
  p2.goto(x+20,y)
  p3.goto(x,y-20)
  p4.goto(x+20,y-20)
  x = x+ 60
  obs.append(p1)
  obs.append(p2)
  obs.append(p3)
  obs.append(p4)

obs2 = []  
x2 = -280
y2 = 220
for _ in range(10):
  r = t.Turtle()
  r.color("white")
  r.shape("square")
  r.penup()
  r2 = t.Turtle()
  r2.color("red")
  r2.shape("square")
  r2.penup()
  r3 = t.Turtle()
  r3.color("red")
  r3.shape("square")
  r3.penup()
  r4 = t.Turtle()
  r4.color("white")
  r4.shape("square")
  r4.penup()
  
  r.goto(x2, y2)
  r2.goto(x2+20,y2)
  r3.goto(x2,y2-20)
  r4.goto(x2+20,y2-20)
  x2 = x2 +60
  obs2.append(r)
  obs2.append(r2)
  obs2.append(r3)
  obs2.append(r4)
  
  
obs3 = []  
x3 = -280
y3 = 160
for _ in range(10):
  w = t.Turtle()
  w.color("white")
  w.shape("square")
  w.penup()
  w2 = t.Turtle()
  w2.color("white")
  w2.shape("square")
  w2.penup()
  w3 = t.Turtle()
  w3.color("white")
  w3.shape("square")
  w3.penup()
  w4 = t.Turtle()
  w4.color("white")
  w4.shape("square")
  w4.penup()
  
  w.goto(x3, y3)
  w2.goto(x3+20,y3)
  w3.goto(x3,y3-20)
  w4.goto(x3+20,y3-20)
  x3 = x3 +60
  obs3.append(w)
  obs3.append(w2)
  obs3.append(w3)
  obs3.append(w4)
  
print(len(obs2))


  
obs4 = []  
x4 = -280
y4 = 100
for _ in range(10):
  s = t.Turtle()
  s.color("red")
  s.shape("square")
  s.penup()
  s2 = t.Turtle()
  s2.color("red")
  s2.shape("square")
  s2.penup()
  s3 = t.Turtle()
  s3.color("red")
  s3.shape("square")
  s3.penup()
  s4 = t.Turtle()
  s4.color("red")
  s4.shape("square")
  s4.penup()
  
  s.goto(x4, y4)
  s2.goto(x4+20,y4)
  s3.goto(x4,y4-20)
  s4.goto(x4+20,y4-20)
  x4 = x4 + 60
  obs4.append(s)
  obs4.append(s2)
  obs4.append(s3)
  obs4.append(s4)
  
print(len(obs2))


# Create Paddle
# TODO: Move Paddle to Bottom of screen
# Hint: use pen up, goto, pendown

paddle = []
x = 0
y = -290
for _ in range(7):
  p = t.Turtle()
  p.color("white")
  p.shape("square")
  p.penup()
  p.goto(x, y)
  x = x + 20
  paddle.append(p)


# Move the player left and right
def move_left():
  global paddle
  
  for i in range(7):
    x = paddle[i].xcor()
    x = x - 10
    paddle[i].setx(x)


def move_right():
  global paddle
  for p in paddle:
    x = p.xcor()
    x = x + 10
    p.setx(x)

screen.onkey(move_left, 'space')
screen.onkey(move_right, 'space')
screen.listen()



# Tell the program which functions go with which keys





# Step size to move the ball
x_step = 1.5
y_step = 2
score = 0
game_on =True
while game_on:
  ball_x = ball.xcor()
  ball_y = ball.ycor()
  
  if ball_x > 290:
    x_step = -2
  elif ball_x < -290:
    x_step = 2
  if ball_y > 290:
    y_step = random.randint(-20,-5)
  if ball_y < -290:
    game_on = False
    screen.clear()
    print("game_over")
    
  ball_x = ball_x + x_step
  ball_y = ball_y + y_step
  ball.setx(ball_x)
  ball.sety(ball_y)
  
  
  for p in paddle:
    px = p.xcor()
    py = p.ycor()
    if abs(py - ball_y) <= 5 and abs(px - ball_x) <= 5:
       y_step = 2
       ball_y = ball_y + y_step
       ball.sety(ball_y)
       print("paddle hit")
       x_step = random.randint(1,20)
       y_step = random.randint(1,20)
  

  # TODO: See if Ball new position is same as Paddle 
  # If it's the same position, then change direction of ball

  for p1 in obs:
    diffx = abs(ball.xcor() - p1.xcor())
    diffy = abs(ball.ycor() - p1.ycor())
    if diffx <= 20 and diffy <= 20:
      p1.goto(-700,700)
      p2.goto(-700,700)
      p3.goto(-700,700)
      p4.goto(-700,700)
     
  for p2 in obs:
    diffx2 = abs(ball.xcor() - p2.xcor())
    diffy2 = abs(ball.ycor() - p2.ycor())
    if diffx2 <= 20 and diffy2 <= 20:
      p1.goto(-700,700)
      p2.goto(-700,700)
      p3.goto(-700,700)
      p4.goto(-700,700)
      
      
  for p3 in obs:
    diffx3 = abs(ball.xcor() - p3.xcor())
    diffy3 = abs(ball.ycor() - p3.ycor())
    if diffx3 <= 20 and diffy3 <= 20:
      p1.goto(-700,700)
      p2.goto(-700,700)
      p3.goto(-700,700)
      p4.goto(-700,700)
      
  for p4 in obs:
    diffx4 = abs(ball.xcor() - p4.xcor())
    diffy4 = abs(ball.ycor() - p4.ycor())
    if diffx4 <= 20 and diffy4 <= 20:
      p1.goto(-700,700)
      p2.goto(-700,700)
      p3.goto(-700,700)
      p4.goto(-700,700)
      
      
  
  
  for r in obs2:
    diff = abs(ball.xcor() - r.xcor())
    diff2 = abs(ball.ycor() - r.ycor())
    if diff <= 20 and diff2 <= 20:
      r.goto(-700,700)
      r2.goto(-700,700)
      r3.goto(-700,700)
      r4.goto(-700,700)
     
  for r2 in obs2:
    diff3 = abs(ball.xcor() - r2.xcor())
    diff4 = abs(ball.ycor() - r2.ycor())
    if diff3 <= 20 and diff4 <= 20:
      r.goto(-700,700)
      r2.goto(-700,700)
      r3.goto(-700,700)
      r4.goto(-700,700)
     
  for r3 in obs2:
    diff5 = abs(ball.xcor() - r3.xcor())
    diff6 = abs(ball.ycor() - r3.ycor())
    if diff5 <= 20 and diff6 <= 20:
      r.goto(-700,700)
      r2.goto(-700,700)
      r3.goto(-700,700)
      r4.goto(-700,700)
      
  for r4 in obs2:
    diff7 = abs(ball.xcor() - r4.xcor())
    diff8 = abs(ball.ycor() - r4.ycor())
    if diff7 <= 20 and diff8 <= 20:
      r.goto(-700,700)
      r2.goto(-700,700)
      r3.goto(-700,700)
      r4.goto(-700,700)
     
      
  
  
  
  
  for w in obs3:
    wdiff = abs(ball.xcor() - w.xcor())
    wdiff2 = abs(ball.ycor() - w.ycor())
    if wdiff <= 20 and wdiff2 <= 20:
      w.goto(-700,700)
      w2.goto(-700,700)
      w3.goto(-700,700)
      w4.goto(-700,700)
      
  for w2 in obs3:
    wdiff3 = abs(ball.xcor() - w2.xcor())
    wdiff4 = abs(ball.ycor() - w2.ycor())
    if wdiff3 <= 20 and wdiff4 <= 20:
      w.goto(-700,700)
      w2.goto(-700,700)
      w3.goto(-700,700)
      w4.goto(-700,700)
     
      
  for w3 in obs3:
    wdiff5 = abs(ball.xcor() - w3.xcor())
    wdiff6 = abs(ball.ycor() - w3.ycor())
    if wdiff5 <= 20 and wdiff6 <= 40:
      w.goto(-700,700)
      w2.goto(-700,700)
      w3.goto(-700,700)
      w4.goto(-700,700)
     
  for w4 in obs2:
    wdiff7 = abs(ball.xcor() - w4.xcor())
    wdiff8 = abs(ball.ycor() - w4.ycor())
    if wdiff7 <= 20 and wdiff8 <= 20:
      w.goto(-700,700)
      w2.goto(-700,700)
      w3.goto(-700,700)
      w4.goto(-700,700)
      
      
  
  
  
  for s in obs4:
    sdiff = abs(ball.xcor() - s.xcor())
    sdiff2 = abs(ball.ycor() - s.ycor())
    if sdiff <= 20 and sdiff2 <= 20:
      s.goto(-700,700)
      s2.goto(-700,700)
      s3.goto(-700,700)
      s4.goto(-700,700)
      
  for s2 in obs4:
    sdiff3 = abs(ball.xcor() - s2.xcor())
    sdiff4  = abs(ball.ycor() - s2.ycor())
    if sdiff3 <= 20 and sdiff4 <= 20:
      s.goto(-700,700)
      s2.goto(-700,700)
      s3.goto(-700,700)
      s4.goto(-700,700)
      
  for s3 in obs4:
    sdiff5 = abs(ball.xcor() - s3.xcor())
    sdiff6 = abs(ball.ycor() - s3.ycor())
    if sdiff5 <= 20 and sdiff6 <= 20:
      s.goto(-700,700)
      s2.goto(-700,700)
      s3.goto(-700,700)
      s4.goto(-700,700)
      
  for s4 in obs4:
    sdiff7 = abs(ball.xcor() - s4.xcor())
    sdiff8 = abs(ball.ycor() - s4.ycor())
    if sdiff7 <= 20 and sdiff8 <= 20:
      s.goto(-700,700)
      s2.goto(-700,700)
      s3.goto(-700,700)
      s4.goto(-700,700)
     
      
       

  
    
    
    
  screen.update()
  time.sleep(0.01)
  
    # if diffx < 5 and diffy < 5:
      # Detected collusion
      # Remove an element
      # p.color("black")
      # obs.remove(p)
      

  
