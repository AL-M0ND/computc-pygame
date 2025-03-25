import pygame
from sprites import snake


class Game_state:
    def __init__(self):
        self.score = 0
        self.food = []
        self.running = True
        self.snake = snake.Snake()

    def get_food(self):
        return self.food

    def update_food(self, screen):
        for item in self.food:
            pygame.draw.rect(screen, (0, 0, 0), (item.pos["x"], item.pos["y"], 20, 20))

    def test_collision(self):
        if self.snake.head.next is not None:
            node = self.snake.head.next
            while node.next is not None:
                if self.snake.head.pos == node.pos:
                    self.running = False
                    break
                node = node.next

        if self.snake.head.pos["x"] > 600:
            self.snake.head.pos["x"] = 0
        if self.snake.head.pos["x"] < 0:
            self.snake.head.pos["x"] = 600
        if self.snake.head.pos["y"] > 600:
            self.snake.head.pos["y"] = 0
        if self.snake.head.pos["y"] < 0:
            self.snake.head.pos["y"] = 600

        for item in self.food:
            if self.snake.head.pos == item.pos:
                self.snake.add_segment()
                self.food.remove(item)

    def update_snake(self, screen):
        node = self.snake.tail.prev
        while node is not self.snake.head:
            x = node.pos["x"] = node.prev.pos["x"]
            y = node.pos["y"] = node.prev.pos["y"]
            pygame.draw.rect(screen, node.color, (x, y, node.width, node.height))
            node = node.prev

        if node.direction == "r":
            node.pos["x"] += node.width
        if node.direction == "l":
            node.pos["x"] -= node.width
        if node.direction == "d":
            node.pos["y"] += node.width
        if node.direction == "u":
            node.pos["y"] -= node.height
        pygame.draw.rect(screen, self.snake.color, (node.pos["x"], node.pos["y"], node.width, node.height))

    def update_game(self, screen):
        self.update_snake(screen)
        self.update_food(screen)
        self.test_collision()
