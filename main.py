import turtle
from Node import Node

t = turtle.Turtle()
t.speed(1)

node = Node(1)
node.insert(2)
node.insert(-1)

print(node.left.data)
print(node.data)
print(node.right.data)

t.getscreen()._root.mainloop()  # <-- run the Tkinter main loop
