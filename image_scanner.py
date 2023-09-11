import pygame as pg
import os, time, random
pg.init()
WIN , HEI = 360, 480
inital_x, inital_y = 0, 0
window = pg.display.set_mode((WIN, HEI), 0, 32)
class color_dector:
    def __init__(self, x, y, size:tuple):
        self.x = x
        self.y = y
        self.size = size
s = color_dector(inital_x, inital_y, (1, 1))
golf = pg.Surface((s.size))
golf.fill((0, 255, 255))
window.fill((0,0,0))
color = ()
Run = True
color_list = []
while Run:
    pos = (s.x, s.y)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pg.draw.line(window, color, pos, pos, 1)
    #pg.draw.line(window)

    s.x += 1
    window.blit(golf, (s.x, s.y))
    if s.x > WIN:
        s.x = 0
        s.y += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                Run = False
                print("Ended!!")
    if s.y < HEI:
        color_list.append(color)
    pg.display.flip()

with open("color_list.txt", "w") as cs:
    for colorval in color_list:
        counter = 0
        for number in colorval:
            counter += 1
            cs.write(str(number))
            if counter != 3:
                cs.write(" ")
        cs.write("\n")
print(len(color_list))