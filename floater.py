# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    def __init__(self, x,y):
        Floater.randomize_angle(self)
        Prey.__init__(self,x,y,10,10,self._angle,5)
    
    def update(self):
        x = random()
        y = random()
        if x <= .3:
            Floater.randomize_angle(self)
            if ((self._speed + y - .5) >= 3) and (self._speed+y-.5) <= 7:
                self._speed = self._speed + y - .5
        Prey.move(self)
    
    def display(self, canvas):
        canvas.create_oval(self._x-5, self._y-5,self._x+5, self._y+5,fill='red')