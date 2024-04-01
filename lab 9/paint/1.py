import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Program")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define shapes
RECTANGLE = 'rectangle'
CIRCLE = 'circle'
ERASER = 'eraser'

# Default shape and color
current_shape = RECTANGLE
current_color = BLACK

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_shape = RECTANGLE
            elif event.key == pygame.K_c:
                current_shape = CIRCLE
            elif event.key == pygame.K_e:
                current_shape = ERASER
            elif event.key == pygame.K_b:
                current_color = BLACK
            elif event.key == pygame.K_w:
                current_color = WHITE
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_shape == RECTANGLE:
                pygame.draw.rect(screen, current_color, (event.pos[0], event.pos[1], 50, 50))
            elif current_shape == CIRCLE:
                pygame.draw.circle(screen, current_color, event.pos, 25)
            elif current_shape == ERASER:
                pygame.draw.circle(screen, WHITE, event.pos, 25)
        
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
