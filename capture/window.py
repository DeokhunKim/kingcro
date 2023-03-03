import numpy as np
import cv2

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
    cv2.rectangle(shapes, (0, 0), (int(WIDTH/2), int(HEIGHT/2)), (255, 0, 0), -1)
    cv2.rectangle(shapes, (int(WIDTH/2), 0), (WIDTH, int(HEIGHT/2)), (0, 255, 0), -1)
    cv2.rectangle(shapes, (0, int(HEIGHT/2)), (int(WIDTH/2), HEIGHT), (0, 0, 255), -1)
    cv2.rectangle(shapes, (int(WIDTH/2), int(HEIGHT/2)), (WIDTH, HEIGHT), (255, 0, 255), -1)

