import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([1000,300])
screen.fill([0,0,255])
player = pygame.image.load("10544.png")
player = pygame.transform.scale(player, (80, 100))
y = 150
screen.blit(player, [100, y])
pg = pygame.draw.rect(screen, (0,255,0),(0, 250, 1000,50))

is_jump = True
running = True
jumpCount = 10
while running:

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if is_jump:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False


    isJump = True

    screen.fill([0, 0, 255])
    pg = pygame.draw.rect(screen, (0, 255, 0), (0, 250, 1000, 50))
    screen.blit(player, [100, y])
    pygame.display.update()