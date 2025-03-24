from sprites import segment
import pygame


class Snake:

    COLORS = {1: (94, 60, 208),
              2: (56, 61, 150),
              3: (175, 54, 60),
              4: (214, 126, 44)}

    def __init__(self):
        self.color = self.COLORS[2]
        self.head = segment.Segment(True, False, 20)
        self.tail = segment.Segment(False, True, 0)
        self.tail.prev = self.head

    def add_segment(self):
        new_segment = segment.Segment(False, False, 20)
        self.tail.prev.next = new_segment
        new_segment.prev = self.tail.prev
        self.tail.prev = new_segment
        new_segment.pos = {"x": new_segment.prev.pos["x"] - new_segment.width, "y": new_segment.prev.pos["y"]}
        new_segment.surface = pygame.Rect(new_segment.pos["x"], new_segment.pos["y"], new_segment.width, new_segment.height)

    def update_snake(self, screen):
        node = self.tail.prev
        while node is not self.head:
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
        pygame.draw.rect(screen, self.color,(node.pos["x"], node.pos["y"], node.width, node.height))

    def draw(self, screen):
        node = self.tail.prev
        while node is not self.head:
            x = node.pos["x"]
            y = node.pos["y"]
            pygame.draw.rect(main, (0, 255, 255), (x, y, node.width, node.height))
            node = node.prev
        x = node.pos["x"]
        y = node.pos["y"]
        pygame.draw.rect(screen, (0, 255, 255), (x, y, node.width, node.height))
