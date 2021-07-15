import time
import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode([1000,300])
screen.fill([255, 255, 255])
player = pygame.image.load("10544.png")
player = pygame.transform.scale(player, (80, 100))
y = 150
b1_x = 1000
screen.blit(player, [100, y])
pg = pygame.draw.rect(screen, (230, 230 ,230),(0, 250, 1000,50))
space = False

def blocs():
    global bl_running
    bl_h = random.randint(80, 120)
    bl_w = random.randint(80,120)
    bl1 = pygame.draw.rect(screen, (225, 0, 0), (b1_x, 200, bl_h, bl_w))
    return bl1


    


is_jump = True
running = True
jumpCount = 10
bl_running = True
clock = pygame.time.Clock()
while running:
    clock.tick(20)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("space")
        space = True
    if is_jump and space:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
            space = False
    if bl_running:
        blocs()
        b1_x -= 10
    isJump = True


    pg = pygame.draw.rect(screen, (230, 230, 230), (0, 250, 1000, 50))
    screen.blit(player, [100, y])
    pygame.display.update()