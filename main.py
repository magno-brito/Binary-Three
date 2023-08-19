import turtle
from Node import Node
import random


screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(2)

node = Node(5,t)
node.insert(1)
node.insert(10)
node.insert(-2)
node.insert(4)
node.insert(3)
node.insert(-1)
node.insert(7)
node.insert(11)
node.insert(8)



t.right(90)

node.drawTree(100,node)
node.labels("In order",200,200)
node.inOrderPrint(node)

    
     


          



t.getscreen()._root.mainloop()  # <-- run the Tkinter main loop
