#turtle 1
# from turtle import*
# shape('turtle')
# speed()
# color('red')
# for i in range (4):
# 	left(30)
# 	forward(100)
# 	right(60)
# 	forward(100)
# 	right(120)
# 	forward(100)
# 	right(60)
# 	forward(100)
# 	right(60)


# mainloop()
#turtle 2
from turtle import*

speed()
for edge in range (3,7):
	for i in range(edge):
		if edge == (3):
			color('blue')
			forward(100)
			left(360/edge)
		else:
			if edge == 5:
				color('blue')
				forward(100)
				left(360/edge)
			else:
				color('red')
				forward(100)
				left(360/edge)

mainloop()