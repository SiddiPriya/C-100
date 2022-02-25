class Sticks(object):
    def __init__(self,color,width,height):
        self.color=color
        self.width=width
        self.height=height
    def display(self):
        print("I am there")

stick1=Sticks("blue",7,7)
stick1.display()