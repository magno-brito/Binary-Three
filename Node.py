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
        self.turtle.setheading(0)
        self.turtle.penup()
        self.turtle.goto(x,y)
        self.turtle.color('#101884')
        self.turtle.write(title,font=("arial",12,"bold"))
        self.turtle.goto(x+18,y-20)
        

    def inOrderPrint(self,node):
        if node is None:
            return
        else:
            self.inOrderPrint(node.left)
            if node:
                self.turtle.setheading(270)
                self.turtle.color('#195c84')
                self.turtle.write(str(node.data) + ", ", font=("arial",10,"bold"))
                self.turtle.forward(30)
            self.inOrderPrint(node.right)

    def preOrderPrint(self,node):
        if node is None:
            return
        else:
            if node:
                self.turtle.setheading(270)
                self.turtle.color('#195c84')
                self.turtle.write(str(node.data) + ", ", font=("arial",10,"bold"))
                self.turtle.forward(30)
            self.preOrderPrint(node.left)
            self.preOrderPrint(node.right)
    
    def posOrderPrint(self,node):
        if node is None:
            return
        else:
            self.posOrderPrint(node.left)
            self.posOrderPrint(node.right)
            if node:
                self.turtle.setheading(270)
                self.turtle.color('#195c84')
                self.turtle.write(str(node.data) + ", " , font=("arial",10,"bold"))
                self.turtle.forward(30)
    
    
    def drawTree(self,length, node):
        if node.data is not None:
            self.turtle.forward(length)
            self.turtle.color("#003FB3")
            self.turtle.write(node.data, font=("arial",10,"bold"))
            self.turtle.color("black")
            self.turtle.left(15)
            if node.right:
                self.drawTree(3*length/4,node.right)
            self.turtle.right(30)
            if node.left:
                self.drawTree(3*length/4,node.left)
            self.turtle.left(15)
            self.turtle.backward(length)
            
            
        else:
            return 
        
    
         
        
    
            


            

