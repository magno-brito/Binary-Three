import turtle
from Node import Node
import random


screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(2)

node = Node(5,t)
node.insert(6)
node.insert(9)
node.insert(11)
node.insert(0)
node.insert(1)
node.insert(4)



node.drawTree(100,node)
node.labels("In order",0,200)
node.inOrderPrint(node)
node.labels("Pre order",0,250)
node.preOrderPrint(node)
node.labels("Pós order",0,300)
node.posOrderPrint(node)

    
     

t.getscreen()._root.mainloop()  
