import turtle

array = [1,2,3,4,5,6,7,8,9,10]

t = turtle.Turtle()
t.speed(1)
for i in range(len(array)):
    
    t.right(100)
    t.forward(100)
    t.write(array[i])
    t.right(100)
    t.forward(100)

t.getscreen()._root.mainloop()  # <-- run the Tkinter main loop
