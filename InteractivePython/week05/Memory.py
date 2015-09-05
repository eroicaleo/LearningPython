# implementation of card game - Memory

import simplegui
import random

# Global variables
decker = list(range(8)) * 2
expose = [False for i in range(16)]

state = 0
last1 = -1
last2 = -1
turns = 0

# helper function to initialize globals
def new_game():
    global state, last1, last2, turns, expose
    random.shuffle(decker)
    state = 0
    last1 = -1
    last2 = -1
    turns = 0
    expose = [False for i in range(16)]
    label.set_text('Turns = ' + str(turns))

     
# define event handlers
def mouseclick(pos):
    global state, last1, last2, turns
    # add game state logic here
    ix = pos[0] // 50
    
    if expose[ix]:
        return
    
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
        
        turns += 1
        label.set_text('Turns = ' + str(turns))
    elif state == 2:
        if decker[last1] != decker[last2]:
            expose[last1] = False
            expose[last2] = False
      
        state = 1
    # print 'I am in state', state
    last2, last1 = last1, ix
    expose[ix] = True

def drawCard(canvas, card, ix):
    if expose[ix]:
        x, y = 15+50*ix, 65
        canvas.draw_text(str(card), (x, y), 40, 'White', 'monospace')
    else:
        canvas.draw_polygon([(ix*50, 0), ((1+ix)*50, 0), ((1+ix)*50, 100), (ix*50, 100)], 2, 'Black', 'Green')
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for (ix, card) in enumerate(decker):
        drawCard(canvas, card, ix)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
