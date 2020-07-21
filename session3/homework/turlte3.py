#1
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# from turtle import*
# speed(-1)
# for edge in range(3,8):
#     # color(colors[edge])
#     for i in range(edge):
#         color(colors[edge - 3])
#         forward(100)
#         left(360/edge)

# mainloop()

#2
from turtle import*
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
number = range(5)
for nshape in number:
    color(colors[nshape])
    begin_fill()
    edge =[50,100,50,100]
    for i in edge:
        forward(i)
        right(90)
    forward(50)
    end_fill()

mainloop()