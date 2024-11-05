from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

shruda = Turtle()
shruda.color('red')
shruda.shape('turtle')

shruda.penup()
shruda.goto(-160, 100)
shruda.pendown()

for turn in range(10):
  shruda.right(36)

mashalla = Turtle()
mashalla.color('blue')
mashalla.shape('turtle')

mashalla.penup()
mashalla.goto(-160, 70)
mashalla.pendown()

for turn in range(72):
  mashalla.left(5)

bishmilla = Turtle()
bishmilla.shape('turtle')
bishmilla.color('green')

bishmilla.penup()
bishmilla.goto(-160, 40)
bishmilla.pendown()

for turn in range(60):
  bishmilla.right(6)

nicoflow = Turtle()
nicoflow.shape('turtle')
nicoflow.color('orange')

nicoflow.penup()
nicoflow.goto(-160, 10)
nicoflow.pendown()

for turn in range(30):
  nicoflow.left(12)

for turn in range(100):
  shruda.forward(randint(1,5))
  mashalla.forward(randint(1,5))
  bishmilla.forward(randint(1,5))
  nicoflow.forward(randint(1,5))
  