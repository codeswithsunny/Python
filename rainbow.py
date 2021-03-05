# import turtle library
import turtle             
colors = [ "red","orange","yellow","green","blue","pink"]
my_arrow = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_arrow.pencolor(colors[x % 6])
   my_arrow.width(x/50 + 1)
   my_arrow.forward(x)
   my_arrow.left(59)
