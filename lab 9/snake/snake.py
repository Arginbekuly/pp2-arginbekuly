import pygame
import sys
import random
import time

pygame.init()


SIZE_BLOCK = 30
WHITE = (255, 255, 255)

SNAKE = (108,73,73)
COUNT_BLOCKS = 20
BLUE = (210, 255, 255)
RED = (224, 0, 0)
GRANICA = 1
HEADER_GRANICA = 60
SKY_BLUE=(181,76,213)
H,W=700,750
screen = pygame.display.set_mode((H,W))
timer = pygame.time.Clock()
text = pygame.font.SysFont('ramona', 50, 1)


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, Block) and self.x == other.x and self.y == other.y



def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + GRANICA * (column),
                                     HEADER_GRANICA + SIZE_BLOCK + row * SIZE_BLOCK + GRANICA * (row),
                                     SIZE_BLOCK, SIZE_BLOCK])


def start_the_game():
    
    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS - 1)
        y = random.randint(0, COUNT_BLOCKS - 1)
        empty_block = Block(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
        return empty_block

    snake_blocks = [Block(9, 9), Block(9, 10), Block(9, 11)]
    apple = get_random_empty_block()
    two_apple=get_random_empty_block()
    two_apple_timer = pygame.time.get_ticks()
    d_row = 0
    d_col = 1
    total = 0
    speed = 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1

        screen.fill("blue")
        

        text_total = text.render(f"Total: {total}", 1, WHITE)
        text_speed = text.render(f"Speed: {speed}", 1, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))

        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):

                if (row + column) % 2 == 0:
                    color = WHITE
                else:
                    color = BLUE

                draw_block(color, row, column)

        head = snake_blocks[-1]
        if not head.inside():
            break

        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE, block.x, block.y)

        if apple == head:
            total += 1
            speed = total // 3 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()
        
        draw_block(SKY_BLUE, two_apple.x, two_apple.y)
        for block in snake_blocks:
            draw_block(SNAKE, block.x, block.y)
        if two_apple == head:
            total += 2   
            snake_blocks.append(two_apple)
            two_apple = get_random_empty_block()
            two_apple_timer = pygame.time.get_ticks()  # Reset the timer

        # Check if the timer for two_apple has expired (6 seconds)
        if pygame.time.get_ticks() - two_apple_timer >= 6000:
            two_apple = get_random_empty_block()
            two_apple_timer = pygame.time.get_ticks()  # Reset the timer

    
        new_head = Block(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            print('crash yourself')
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(4 + speed)
        pygame.display.update()


start_the_game()