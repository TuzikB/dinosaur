import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([1000,300])
screen.fill([0,0,255])
player = pygame.image.load("10544.png")
player = pygame.transform.scale(player, (80, 100))
screen.blit(player, [100, 150])

pg = pygame.draw.rect(screen, (0,255,0),(0, 250, 1000,50))


running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False