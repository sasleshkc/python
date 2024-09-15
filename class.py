class point:
    def __init__(self,height, width):
        self.height=height                
        self.width=width                
    def speak(self):
        print("hello world")
    
point1=point("5ft","3ft")
point1.speak()
print(point1.height)
print(point1.width)

        