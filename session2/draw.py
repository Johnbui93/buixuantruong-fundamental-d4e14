from turtle import*
speed(-1)
for edge in range(3,10):
    for i in range(edge):
        forward(100)
        left(360/edge)

mainloop()