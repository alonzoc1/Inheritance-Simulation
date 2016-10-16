# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey



class Ball(Prey):
    def __init__(self, x,y):
        Ball.randomize_angle(self)
        Prey.__init__(self,x,y,10,10,self._angle,5)
    
    def update(self):
        Prey.move(self)
    
    def display(self, canvas):
       canvas.create_oval(self._x-5      , self._y-5,
                                self._x+5, self._y+5,
                                fill='blue')