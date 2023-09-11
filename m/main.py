# Im going to actuly try and finish this

import pygame as pg
import sys, math
WIN, HEI = 800, 800
screen = pg.display.set_mode((WIN, HEI))
clock = pg.time.Clock()
FPS = 60
class create_object:
    def __init__(self, surface, colour, point1, point2, point3):
        self.surface = surface
        self.color = colour
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.points = (point1, point2, point3)

def calculate_size(obj:object):
    #A ( x 1 , y 1 ) , B ( x 2 , y 2 ) and C ( x 3 , y 3 )
    x1 = obj.point1[0]
    y1 = obj.point1[1]

    x2 = obj.point2[0]
    y2 = obj.point2[1]

    x3 = obj.point3[0]
    y3 = obj.point3[1]
    
    area = (0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    return area
    
triangle = create_object(screen, (0,255,255), point1=(50,100), point2=(100, 50), point3=(150, 100))
area_triangle = calculate_size(triangle)
triangle2 = create_object(screen, (0, 0, 255), (WIN/2, 25), (WIN/2, 100), (WIN/2, 46))
pg.draw.polygon(triangle.surface, triangle.color, triangle.points)
pg.draw.polygon(triangle2.surface, triangle2.color, triangle2.points)
while True:
    pg.display.set_caption(str(area_triangle))
    dt1 = clock.tick(FPS) / 1000
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()