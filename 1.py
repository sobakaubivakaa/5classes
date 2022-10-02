class Rectangle:
    def __init__ (self,color="green", width=100,height=100, change = 0):
        self.color = color
        self.width = width
        self.height = height
        self.change = change
    def square(self):
        return self.width *self.height
    def setchange(self,number):
        self.change = number
        print(self.change)
rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect1 = Rectangle("yellow",23,34)
print(rect1.color)
print(rect1.square())
print("-----------------------------------")
print(rect1.change)
rect1.setchange(5) 
