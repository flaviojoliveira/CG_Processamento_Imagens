from graphics import *
from time import *


def animation():

#framerate = 1/30.0

liam = [Image(Point(250, 250),  str(i) + '.png') for i in range(4)]
liamFrame = 0
liam[liamFrame].draw(win)
while win.closed == False:

    liam[liamFrame].undraw()
    liamFrame = (liamFrame + 1) % len(liam)
    liam[liamFrame].draw(win)

    win.update()
    sleep(.1)

win = GraphWin('Animation', 600, 600, autoflush=False)
animation()