class Animal:
    def __init__(self):
        self.size = 2
        
    def breath(self):
        print("Inhale")
    
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def breath(self):
        super().breath()
        print("Swimmmm")
        
    def swim(self):
        print("moving in water")
        
fish = Fish()
fish.swim()
fish.breath()