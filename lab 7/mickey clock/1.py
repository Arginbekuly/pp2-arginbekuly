import pygame, math, time
pygame.init()

def curr_time(): 
    global m, s
    m, s = time.localtime().tm_min, time.localtime().tm_sec

weith = 900
height = 675
screen= pygame.display.set_mode((weith, height))
pygame.display.set_caption('MickeyClock')

img_main = pygame.image.load('images//micbody.png')
img_main = pygame.transform.scale(img_main, (weith, height))

img_hand1 = pygame.image.load('images//left.png')
img_hand1 = pygame.transform.scale(img_hand1, (230, 350))

img_hand2 = pygame.image.load('images//right.png')
img_hand2 = pygame.transform.scale(img_hand2, (150, 280))
radius = 60 # necassary radius

def print_hand(img, degree):
    img = pygame.transform.rotate(img, degree)
    rect = img.get_rect()
    rect.center = screen.get_rect().center
    # add (x, y) to shift it to radius
    rect.centerx += radius * math.sin(math.radians(-degree)) 
    rect.centery -= radius * math.cos(math.radians(-degree))

    screen.blit(img, rect)

clock = pygame.time.Clock()
run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = 0
    
    curr_time()
    screen.blit(img_main, (0,0))
    print_hand(img_hand1, s * (-6))
    print_hand(img_hand2, m * (-6))
    
    pygame.display.update()
    clock.tick(60)