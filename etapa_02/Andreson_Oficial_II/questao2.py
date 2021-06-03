import numpy as np
from matplotlib import pyplot as plt
import keyboard


mapa = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]


posx, posy = (1,1)


exitx, exity = (3,3)


rot = np.pi/4

while True:
    for i in range(60):
        rot_i = rot + np.deg2rad(i - 30)
        x, y = (posx, posy)
        sin, cos = (0.02*np.sin(rot_i), 0.02*np.cos(rot_i))
        n = 0
        while True:
            x, y = (x + cos, y + sin)
            n = n+1
            if mapa[int(x)][int(y)] !=0:
                h = 1/(0.02 * n)
                break
        plt.vlines(i, -h, h, lw = 8)

    plt.axis('off'); plt.tight_layout(); plt.axis([0, 60, -1, 1])
    plt.draw(); plt.pause(0.0001); plt.clf()



    key = keyboard.read_key()
    x, y = (posx, posy)

    if key == 'up':
        x, y = (x + 0.3*np.cos(rot), y + 0.3*np.sin(rot))
    elif key == 'down':
        x, y = (x - 0.3*np.cos(rot), y - 0.3*np.sin(rot))
    elif key == 'left':
        rot = rot - np.pi/8
    elif key == 'right':
        rot = rot + np.pi/8
    elif key == 'esc':
        break

    
    if mapa[int(x)][int(y)] ==0:
        if int(posx) == exitx and int(posy) == exity:
            break
        posx, posy = (x, y)

plt.close()