import pygame


class Game_state:
    def __init__(self):
        self.score = 0
        self.food = []
        self.running = True

    def get_food(self):
        return self.food

    def update_food(self, screen):
        for item in self.food:
            pygame.draw.rect(screen, (0, 0, 0), (item.pos["x"], item.pos["y"], 20, 20))

    def test_collision(self, user_snake):
        if user_snake.head.next is not None:
            node = user_snake.head.next
            while node.next is not None:
                if user_snake.head.pos == node.pos:
                    self.running = False
                    break
                node = node.next
        for item in self.food:
            if user_snake.head.pos == item.pos:
                user_snake.add_segment()
                self.food.remove(item)
