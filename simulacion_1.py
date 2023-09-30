#importamos las librerías necesarias
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

scale = 100
circle_pos = [WIDTH / 2, HEIGHT / 2]

angle = 0

points = []

points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))


projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

projected_points = [
    [n, n] for n in range(len(points))
]

def connect_points(i, j, points):
    pg.draw.line(screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

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
    angle += 0.01
        
    screen.fill(WHITE)
    i = 0
    for point in points:
        rotated2dz = np.dot(rotate_z, point.reshape(3, 1))
        rotated2dzy = np.dot(rotate_y, rotated2dz)
        projected2d = np.dot(projection_matrix, rotated2dzy)
        
        x = int(projected2d[0][0] * scale)+ circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]
        
        projected_points[i] = [x, y] # type: ignore
        pg.draw.circle(screen, RED, (x, y), 5)
        i += 1
        
        for p in range(4):
            connect_points(p, (p+1) % 4, projected_points)
            connect_points(p+4, ((p+1) % 4) +4, projected_points)
            connect_points(p, ((p+4)), projected_points)
    
    pg.display.update()