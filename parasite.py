#See special for details on the parasite class

from mobilesimulton import Mobile_Simulton
import model
from math import atan2

class Parasite(Mobile_Simulton):
    def __init__(self,x,y,target,mother):
        Mobile_Simulton.randomize_angle(self)
        Mobile_Simulton.__init__(self,x,y,7,7,self._angle,7)
        self.immunity = True
        self.target = target
        self.mothership = mother
        self.success = True
        self.check = True
    
    def update(self):
        temp = model.find(lambda o: o != None)
        if self.check == True:
            if self.target not in temp and self.immunity == True:
                self.immunity = False
                self.success = False
                self.check = False
            if self.immunity == True and self.target in temp:
                self._angle = atan2((self.target.get_location()[1]-self._y),(self.target.get_location()[0]-self._x))
                if self.distance(self.target.get_location()) <= 5:
                    model.remove(self.target)
                    self.immunity = False
                    self.check = False
        else:
            self._angle = atan2((self.mothership.get_location()[1]-self._y),(self.mothership.get_location()[0]-self._x))
        self.move()
    
    def display(self,canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2,self._x+self._width/2, self._y+self._height/2,fill='purple')
    
    def self_destruct(self):
        model.remove(self)
    
    def ping_is_removed(self):
        pass