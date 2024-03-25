import pygame
import os

pygame.init()
H=500
W=300
screen = pygame.display.set_mode((H, W))
pygame.display.set_caption("musicPlayer")
path = [
    "musics//mus1.mp3",
    "musics//mus2.mp3",
    "musics//mus3.mp3",
    "musics//mus4.mp3",
    "musics//mus5.mp3",
]

current_index = 0
pygame.mixer.music.load(path[current_index])


def play_music():
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    pygame.mixer.music.unpause()


def play_next():
    global current_index
    current_index = (current_index + 1) % len(path)
    pygame.mixer.music.load(path[current_index])
    play_music()


def play_previous():
    global current_index
    current_index = (current_index - 1) % len(path)
    pygame.mixer.music.load(path[current_index])
    play_music()


running = True
while running:
    
    pygame.draw.circle(screen, "black", (240, 150), 50)
    pygame.draw.circle(screen,"white",(240,150),25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pause_music()
                else:
                    unpause_music()
            elif event.key == pygame.K_RIGHT:
                play_next()
            elif event.key == pygame.K_LEFT:
                play_previous()

    screen.fill((255, 255, 255))
    pygame.display.flip()
    

pygame.quit()