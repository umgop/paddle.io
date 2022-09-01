import turtle as t
import time

screen = t.Screen()
screen.setup(width=400, height=400)
screen.bgcolor("black")
screen.tracer(0)

t.speed(0)

# TODO: Draw a Border along the walls (Edges)
# Hint: use t.forward and t.left
border = t.Turtle()
border.penup()
border.goto(-195, -195)
border.color("green")
border.pensize(5)
border.pendown()

border.forward(390)
border.left(90)
border.forward(370)
border.left(90)
border.forward(390)
border.left(90)
border.forward(370)
border.hideturtle()

# Create ball
ball = t.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)

# Create Paddle
left = t.Turtle()
left.penup()
left.shape("square")
left.color("blue")
left.goto(-180, 0)
left1 = t.Turtle()
left1.penup()
left1.shape("square")
left1.color("blue")
left1.goto(-180,-20)
left2 = t.Turtle()
left2.penup()   
left2.shape("square")
left2.color("blue")
left2.goto(-180,-40)


right = t.Turtle()
right.penup()
right.shape("square")
right.color("blue")
right.goto(180, 160)
right1 = t.Turtle()
right1.penup()
right1.shape("square")
right1.color("blue")
right1.goto(180,140)
right2 = t.Turtle()
right2.penup()   
right2.shape("square")
right2.color("blue")
right2.goto(180,120)


# Create a pen to write score
pen = t.Turtle()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 180)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 12, "normal"))



# TODO: Move Paddle to Bottom of screen
# Hint: use pen up, goto, pendown

# Step size to move the ball

# Define a functions fsr each arrow key
def go_right_up():
  y = right.ycor()
  y1=right1.ycor()
  y2=right2.ycor()
  y=y+10
  y1=y1+10
  y2=y2+10
 
  
  if y < 160:
    right.sety(y)
    right1.sety(y1)
    right2.sety(y2)
    

  

def go_right_down():
  y = right.ycor()
  y1=right1.ycor()
  y2=right2.ycor()
  y=y-10
  y1=y1-10
  y2=y2-10
  if y > -180:
 
    right.sety(y)
    right1.sety(y1)
    right2.sety(y2)
  

def go_left_up():
  y = left.ycor()
  y1= left1.ycor()
  y2= left2.ycor()
  y=y+10
  y1=y1+10
  y2=y2+10
  
  if y < 180:
    left.sety(y) 
  
    left1.sety(y1)
 
    left2.sety(y2)

def go_left_down():
  y = left.ycor()
  y1= left1.ycor()
  y2= left2.ycor()
  y=y-10
 
  y1=y1-10
  y2=y2-10
  
  
 
  if y > -180:
    left.sety(y)
    left1.sety(y1)
    left2.sety(y2)
    
  pass


# Tell the program which functions go with which keys

screen.onkey(go_right_down, 'down')
screen.onkey(go_left_up, 'w')
screen.onkey(go_left_down, 's')

screen.listen()

right_score = 0
left_score = 0
game_on = True
x_step = 2
y_step = 2
def ball_follows():
  left = (-180,ball_y)
  left1 = (-180,ball_y-20)
  left2 = (-180,ball_y -40)
    
while game_on:
  ball_x=ball.xcor()
  ball_y=ball.ycor()
  right_x=right.xcor()
  right1_x=right1.xcor()
  right2_x=right2.xcor()
  right_y=right.ycor()
  right1_y=right1.ycor()
  right2_y=right2.ycor()
  left_x=left.xcor()
  left1_x= left1.xcor()
  left2_x=left2.xcor()
  left_y=left.ycor()
  left1_y=left1.ycor()
  left2_y=left2.ycor()
  if ball_x > 180:
    x_step = -2
  elif ball_x < -180:
    x_step = 2
  if ball_y > 160:
    y_step = -2
  elif ball_y < -180:
    y_step = 2
  ball_x = ball_x + x_step
  ball_y = ball_y + y_step
  ball.setx(ball_x)
  ball.sety(ball_y)
  if abs(ball_x-right_x) <= 15 and abs(ball_y-right_y) <= 15 :
    right_score = right_score+1
    x_step =  0 - abs(x_step) - .5
   
  if abs(ball_x-right1_x) <= 15 and abs(ball_y-right1_y) <= 15 :
    right_score = right_score+1
    x_step =  0 - abs(x_step) - .5
  if abs(ball_x-right2_x) <= 15 and abs(ball_y-right2_y) <= 15 :
    right_score = right_score+1
    x_step =  0 - abs(x_step) - .5
  
  if abs(ball_x-left_x) <= 15 and abs(ball_y-left_y) <= 15 :
    left_score = left_score + 1
    x_step = .5 + abs(x_step)
  
  if abs(ball_x-left1_x) <= 15 and abs(ball_y-left1_y) <= 15 :
    left_score = left_score + 1
    x_step = .5 + abs(x_step)
   
  if abs(ball_x-left2_x) <= 15 and abs(ball_y-left2_y) <= 15 :
    left_score = left_score + 1
    x_step = .5 + abs(x_step)
   
  if ball_x >= 180 or ball_x <= -180:
    game_on= False
    if right_score > left_score:
        print("Right is Victorious")
    else:
        print("Left Score is Victorious")
  
    
  screen.update()
  # Reverse Direction on wall collusion in x or y

  # TODO: See if Ball new position is same as Paddle 
  # If it's the same position, then change direction of ball

  # TODO: Keep Score on Hits.  Miss is End Game
  pen.clear()
  pen.write("Right_Score: {} Left Score: {}".format(right_score, left_score), align="center", font=("Courier", 12, "normal"))
  time.sleep(0.01)

