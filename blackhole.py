# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        
    def contains(self,xy, search):
        #return ((((xy[0]-self._x)**2) + ((xy[1]-self._y)**2)) <= 25)
        return (Simulton.distance(self, xy) <= (search))
    
    def contains_obj(self, obj, search=False):
        if isinstance(obj, Prey) != True:
            return False
        if search == False:
            search = self._width/2
        return self.contains(obj.get_location(), search)
    
    def update(self):
        temp = model.find(self.contains_obj)
        for i in temp:
            model.remove(i)
        return temp
    
    def seppuku(self):
        model.remove(self)
    
    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2,self._x+self._width/2, self._y+self._height/2,fill='black')