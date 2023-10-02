import numpy as np
import pygame as pg
import random
import math as mt

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600
pg.display.set_caption('3D projection')
screen = pg.display.set_mode((WIDTH, HEIGHT))
angle = 0

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

rotate_x = np.matrix([
        [1, 0, 0],
        [0, mt.cos(angle), -mt.sin(angle)],
        [0, mt.sin(angle), mt.cos(angle)]
    ])
    
rotate_y = np.matrix([
        [mt.cos(angle), 0, mt.sin(angle)],
        [0, 1, 0],
        [mt.sin(angle), 0, mt.cos(angle)]
    ])
        
rotate_z = np.matrix([
        [mt.cos(angle), -mt.sin(angle), 0],
        [mt.sin(angle), mt.cos(angle), 0],
        [0, 0, 1]
    ])

class Instances():
    def __init__(self, i, j, points):
        self.i = i
        self.j = j
        self.points = points
        self.projected_points = [
            [n, n] for n in range(len(self.points))
            ]
    
    def connect_points(self):
        pg.draw.line(screen, BLACK, (self.points[self.i][0], self.points[self.i][1]), (self.points[self.j][0], self.points[self.j][1]))
        
    

clock = pg.time.Clock()
while True:
    clock.tick(60)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()
    
    screen.fill(WHITE)
    
    pg.display.update()