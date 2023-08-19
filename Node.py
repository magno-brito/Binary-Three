class Node:
    def __init__(self,data,turtle):
        self.data = data
        self.left = None
        self.right = None
        self.turtle = turtle

    def insert(self, value):
        if self.data is None:
            self.data = value
        else:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value,self.turtle)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value,self.turtle)
                else:
                    self.right.insert(value)

    def labels(self, title,x,y):
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(x,y)
        self.turtle.write(title,font=("arial",12,"bold"))
        self.turtle.goto(x,y-20)
        self.turtle.left(90)

    def inOrderPrint(self,node):
        if node is None:
            return
        else:
            self.inOrderPrint(node.left)
            if node:
                self.turtle.write(node.data, font=("arial",12,"bold"))
                self.turtle.forward(30)
            self.inOrderPrint(node.right)
    
    def drawTree(self,length, node):
            if(length<10):
                return
            else:
                if node.data:
                    self.turtle.forward(length)
                    self.turtle.color("red")
                    self.turtle.write(node.data, font=("arial",12,"bold"))
                    self.turtle.color("black")
                    self.turtle.left(30)
                    if node.right:
                        self.drawTree(3*length/4,node.right)
                    self.turtle.right(60)
                    if node.left:
                        self.drawTree(3*length/4,node.left)
                    self.turtle.left(30)
                    self.turtle.backward(length)
                else:
                    return 

            


            

