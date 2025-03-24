import pygame
import random

COLORS = {1: (94, 60, 208),
          2: (56, 61, 150),
          3: (175, 54, 60),
          4: (214, 126, 44)}


class Segment:
    def __init__(self, head, tail, width):
        self.next = None
        self.prev = None
        self.color = COLORS[random.randint(1, 4)]
        if head:
            self.width = width
            self.height = self.width
            self.direction = "r"
            self.pos = {"x": 140, "y": 200}
            self.surface = pygame.Rect(self.pos["x"], self.pos["y"], self.width, self.height)
        elif tail:
            self.width = 0
            self.pos = {"x": 0, "y": 0}
            self.height = 0
            self.surface = pygame.Rect(self.pos["x"], self.pos["y"], self.width, self.height)
        else:
            self.width = width
            self.height = self.width
            # self.pos = {"x": self.prev.pos["x"] - self.width, "y": self.prev.pos["y"]}
