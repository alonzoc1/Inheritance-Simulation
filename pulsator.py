# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.hunger = 0
    
    def update(self):
        x = Black_Hole.update(self)
        if x == set():
            self.hunger += 1
        else:
            self.hunger = 0
            self.change_dimension(1,1)
        if self.hunger == 30:
            self.hunger = 0
            self.change_dimension(-1,-1)
            if self._width == 0 or self._height == 0:
                self.seppuku()
    
    def update_radius(self, radius):
        self._radius = radius
        
        