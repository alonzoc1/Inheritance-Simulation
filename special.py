#This special class is actually comprised of two types of "Hunters": A 'Mothership' and
#it's 'Parasites'. The mothership moves very slowly (2 pix per update) in a straight line, but if a
#prey reaches its vision (200), it will fire out a parasite, which is like a Hunter
#that does not shrink/grow. After the parasite eats the prey (or if the prey is eaten elsewhere),
#it will return to the mothership and the mothership will grow. It cannot shrink. It can eat on its
#own, but does not seek out targets on its own, relying on its parasites. It can only have two parasites
#out at once.

from blackhole import Black_Hole
from mobilesimulton import Mobile_Simulton
from hunter import Hunter
import model
from parasite import Parasite

class Special(Hunter, Mobile_Simulton):
    def __init__(self,x,y):
        Mobile_Simulton.randomize_angle(self)
        Mobile_Simulton.__init__(self,x,y,12,12,self._angle,2)
        self.target1 = None
        self.target2 = None

    def update(self):
        x = Black_Hole.update(self)
        if x != set():
            self.change_dimension(1,1)
        targets_in_range = model.find(self.hunt_contains_obj)
        closest = None
        ticker = None
        for i in targets_in_range:
            if ticker == None:
                if self.target1 != i and self.target2 != i:
                    ticker = self.distance(i.get_location())
                    closest = i
            else:
                if self.distance(i.get_location()) < ticker:
                    if self.target1 != i and self.target2 != i:
                        ticker = self.distance(i.get_location())
                        closest = i
        if closest != None:
            if self.target1 == None:
                self.target1 = closest
                self.launch_parasite(True)
            elif self.target2 == None:
                self.target2 = closest
                self.launch_parasite(False)
        self.remove_close_parasites()
        #print(self.get_dimension())
        self.move()
        
    def is_parasite(self, obj):
        return type(obj) == Parasite
    
    def self_destruct_parasites(self):
        all_parasites = model.find(self.is_parasite)
        for i in all_parasites:
            if i.target == self.target1 or i.target == self.target2:
                model.remove(i)
    
    def remove_close_parasites(self):
        all_parasites = model.find(self.is_parasite)
        for i in all_parasites:
            if self.distance(i.get_location()) <= self._width/2:
                #print(i.immunity)
                if i.immunity == False:
                    #print('removing') ########################
                    model.remove(i)
                    if i.target == self.target1:
                        self.target1 = None
                    elif i.target == self.target2:
                        self.target2 = None
                    if i.success == True:
                        self.change_dimension(1,1)
    
    def launch_parasite(self, b):
        if b:
            model.add(Parasite(self._x,self._y,self.target1,self))
        else:
            model.add(Parasite(self._x,self._y,self.target2,self))

    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2,self._x+self._width/2, self._y+self._height/2,fill='yellow')