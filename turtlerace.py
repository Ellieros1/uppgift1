from turtle import *

write(0)
forward(100)
write(5)
left(90) #sväng 90 grander
forward(100)
write(2)
for i in range(10):
    left(30) #sväng 30 grader
    forward(50) #framåt 40 pixlar
    write(i) #skriv ett tal


exitonclick()