# import pygame
import random
# from sprites import snake
import game


class Food:
    def __init__(self, state):
        collision = True
        while collision is True:
            self.pos = {"x": random.randrange(0, 601, 20), "y": random.randrange(0, 601, 20)}
            node = state.snake.head
            while node is not None:
                if self.pos == node.pos:
                    collision = True
                    break
                elif self.pos != node.pos:
                    collision = False
                    node = node.next
        state.food.append(self)
