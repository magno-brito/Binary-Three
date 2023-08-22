import turtle
from Node import Node
import random


screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(-1)

node = Node(5,t)
node.insert(6)
node.insert(9)
node.insert(9.5)
node.insert(11)
node.insert(4)
node.insert(3)
node.insert(2)
node.insert(0)
node.insert(3.4)
node.insert(-1)
node.insert(11.4)
node.insert(10)
node.insert(8)
node.insert(5.5)



node.drawTree(150,node)
node.labels("In order",-300,200)
node.inOrderPrint(node)
node.labels("Pre order",-200,200)
node.preOrderPrint(node)
node.labels("Pós order",-100,200)
node.posOrderPrint(node)

    
     

t.getscreen()._root.mainloop()  
