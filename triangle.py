import turtle 
wn = turtle.Screen()
wn.bgcolor("black")
skk = turtle.Turtle()
skk.color("orange")

def sqrfunc(size):
	for i in range(4):
		skk.fd(size)
		skk.left(120)
		size = size + 5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
sqrfunc(166)
sqrfunc(186)
sqrfunc(206)
