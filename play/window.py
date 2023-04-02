import numpy as np
import cv2
import random

MIN_X = 0.0
MIN_Y = 0.0
MAX_X = 0.0
MAX_Y = 0.0

WIDTH = 0
HEIGHT = 0

shapes = np.ndarray


def initialize(self):
    self.MAX_X = int(self.MAX_X)
    self.MAX_Y = int(self.MAX_Y)
    self.MIN_X = int(self.MIN_X)
    self.MIN_Y = int(self.MIN_Y)

    self.WIDTH = MAX_X - MIN_X
    self.HEIGHT = MAX_Y - MIN_Y

    self.shapes = np.zeros([HEIGHT, WIDTH, 3], np.uint8)
    #cv2.rectangle(shapes, (0, 0), (int(WIDTH/2), int(HEIGHT/2)), (255, 0, 0), -1)
    #cv2.rectangle(shapes, (int(WIDTH/2), 0), (WIDTH, int(HEIGHT/2)), (0, 255, 0), -1)
    #cv2.rectangle(shapes, (0, int(HEIGHT/2)), (int(WIDTH/2), HEIGHT), (0, 0, 255), -1)
    #cv2.rectangle(shapes, (int(WIDTH/2), int(HEIGHT/2)), (WIDTH, HEIGHT), (255, 0, 255), -1)

    here_entry_boundary = [(int(WIDTH*0.115), int(HEIGHT*0.490)), (int(WIDTH*0.881), int(HEIGHT*0.613))]
    here_entry_boundary_width = here_entry_boundary[1][0] - here_entry_boundary[0][0]
    here_entry_boundary_height = here_entry_boundary[1][1] - here_entry_boundary[0][1]
    here_entry_shapes = []

    for i in range(2):
        for j in range(7):
            cv2.rectangle(shapes,
                          (here_entry_boundary[0][0] + int(here_entry_boundary_width*j/7), here_entry_boundary[0][1] + int(here_entry_boundary_height*i/2)),
                          (here_entry_boundary[0][0] + int(here_entry_boundary_width*(j+1)/7), here_entry_boundary[0][1] + int(here_entry_boundary_height*(i+1)/2)),
                          (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), -1)



    #cv2.rectangle(shapes, here_entry_boundary[0], here_entry_boundary[1], (255, 255, 255), -1)


