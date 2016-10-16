# A Hunter is both a  Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
import model


class Hunter(Pulsator,Mobile_Simulton):
    def __init__(self, x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.randomize_angle(self)
        Mobile_Simulton.set_speed(self, 5)
        
    def update(self):
        Pulsator.update(self)
        temp = model.find(self.hunt_contains_obj)
        closest = None
        ticker = None
        for i in temp:
            if ticker == None:
                ticker = self.distance(i.get_location())
                closest = i
            else:
                if self.distance(i.get_location()) < ticker:
                    ticker = self.distance(i.get_location())
                    closest = i
        if closest != None:
            self._angle = atan2((closest.get_location()[1]-self._y),(closest.get_location()[0]-self._x))
        self.move()
    
    def hunt_contains_obj(self, xy):
        return self.contains_obj(xy, 200)
