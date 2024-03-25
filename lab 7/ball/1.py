import pygame
import time
pygame.init()

H,W=600,600
screen=pygame.display.set_mode((H,W))
pygame.display.set_caption("Ball")
clock=pygame.time.Clock()
x=W//2
y=H//2
r=35
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill("green")
    pygame.draw.circle(screen,"blue",(x,y),35)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y-=20
    if keys[pygame.K_DOWN]:
        y+=20
    if keys[pygame.K_LEFT]:
        x-=20
    if keys[pygame.K_RIGHT]:
        x+=20
    
    if x<r:
        x=r
    if x>W-r:
        x=W-r
    if y<r:
        y=r
    if y>H-r:
        y=H-r
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
