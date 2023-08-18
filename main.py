import turtle
from Node import Node
import random


t = turtle.Turtle()
t.hideturtle()
t.speed(2)

node = Node(5,t)
vetor = []
for i in range(20):
    value = random.randrange(20)
    vetor.append(value)
    node.insert(value)



t.right(90)

node.drawTree(100,node)
    
     


          
# tree(t,200,node)


t.getscreen()._root.mainloop()  # <-- run the Tkinter main loop
