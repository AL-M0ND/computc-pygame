import pygame
from sprites import snake
from sprites import food
import game


print(pygame.init())
state = game.Game_state()


def process_input(state):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            match event.scancode:
                case 82 | 26: state.snake.head.direction = "u"
                case 81 | 22: state.snake.head.direction = "d"
                case 80 | 4: state.snake.head.direction = "l"
                case 79 | 7: state.snake.head.direction = "r"
        if event.type == pygame.QUIT:
            state.running = False
    return True


screen = pygame.display.set_mode((600, 600))
background_color = (100, 100, 100)
test = snake.Snake()
count = 1
running = True
while state.running is True:

    screen.fill(background_color)
    process_input(state)
    count += 1
    if count % 9 == 0:
        new_food = food.Food(state)
        pygame.draw.rect(screen, (0, 0, 0), (new_food.pos["x"], new_food.pos["y"], 20, 20))

    state.update_game(screen)

    # test.update_snake(screen)
    # state.update_food(screen)
    # state.test_collision(test)
    pygame.display.update()
    pygame.time.delay(300)
    print('--------------')
