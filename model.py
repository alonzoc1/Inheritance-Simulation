import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special
from parasite  import Parasite


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False #start in a stopped state
cycle_count = 0
balls = []
black_holes = []
floaters = []
hunters = []
pulsators = []
specials = []
parasites = []
selected_obj = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, balls, black_holes, floaters, hunters, pulsators, specials, parasites
    balls, black_holes, floaters, hunters, pulsators, specials, parasites = [],[],[],[],[],[],[]
    running = False
    cycle_count = 0



#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running
    if running == True:
        update_all()
        stop()
    elif running == False:
        running = True
        step()
        


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected_obj
    selected_obj = kind
    #print(kind,'is life') ################################
    


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global selected_obj
    #print('it happened') ################################
    if selected_obj ==  "Ball":
        add('Ball('+str(x)+','+str(y)+')')
    elif selected_obj == "Floater":
        add('Floater('+str(x)+','+str(y)+')')
    elif selected_obj == "Hunter":
        add('Hunter('+str(x)+','+str(y)+')')
    elif selected_obj == "Pulsator":
        add('Pulsator('+str(x)+','+str(y)+')')
    elif selected_obj == "Black_Hole":
        add('Black_Hole('+str(x)+','+str(y)+')')
    elif selected_obj == "Special":
        add('Special('+str(x)+','+str(y)+')')
    elif selected_obj == "Remove":
        target = None
        break_ticker = False
        for i in [balls,floaters,hunters,pulsators,specials,black_holes]:
            for j in i:
                #print('TESTING: {} < {} and {} > {} and {} < {} and {} > {}\n'.format(j._x - j._width,x,j._x + j._width,x,j._y - j._height,y,j._y + j._height,y)) ######################
                if ((j._x - j._width) <= x) and ((j._x + j._width) >= x) and ((j._y - j._height) <= y) and ((j._y + j._height) >= y):
                    #print('match found\n\n') ####################################
                    target = j
                    break_ticker = True
                    break
            if break_ticker == True:
                break
        if target != None:
            remove(target)


#add simulton s to the simulation
def add(s):
    if type(s) == str:
        x = type(eval(s))
        y = eval(s)
        if x == Ball:
            balls.append(y)
        elif x == Floater:
            floaters.append(y)
        elif x == Hunter:
            hunters.append(y)
        elif x == Pulsator:
            pulsators.append(y)
        elif x == Black_Hole:
            black_holes.append(y)
        elif x == Special:
            specials.append(y)
    else:
        parasites.append(s)
        
    

# remove simulton s from the simulation    
def remove(s):
    global balls, black_holes, floaters, hunters, pulsators, specials, parasites
    if type(s) == Ball:
        balls.remove(s)
    elif type(s) == Black_Hole:
        black_holes.remove(s)
    elif type(s) == Floater:
        floaters.remove(s)
    elif type(s) == Hunter:
        hunters.remove(s)
    elif type(s) == Pulsator:
        pulsators.remove(s)
    elif type(s) == Special:
        s.self_destruct_parasites()
        specials.remove(s)
    elif type(s) == Parasite:
        parasites.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result = []
    for i in [balls,floaters,hunters,pulsators,specials,black_holes,parasites]:
        for j in i:
            if p(j):
                result.append(j)
    return set(result)


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for c in [balls,floaters,hunters,pulsators,specials,black_holes,parasites]:
            for b in c:
                b.update()


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    len_all = []
    for i in [balls,floaters,hunters,pulsators,specials,black_holes,parasites]:
        for j in i:
            len_all.append(1)
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    for c in [balls,floaters,hunters,pulsators,specials,black_holes,parasites]:
        for b in c:
            b.display(controller.the_canvas)
    controller.the_progress.config(text=str(cycle_count)+" updates/"+str(len(len_all))+" simultons")
    #this doesn't update "UPDATES" or "SIMULTONS" on the window
