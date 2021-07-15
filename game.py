import pygame
import random
pygame.init()
screen = pygame.display.set_mode([1000, 300])
screen.fill([255, 255, 255])
player = pygame.image.load("10544.png")
player = pygame.transform.scale(player, (80, 100))
y = 150
b1_x = 1000
screen.blit(player, [100, y])
pg = pygame.draw.rect(screen, (0, 0, 0), (0, 250, 1000, 50))
space = False
yk = 0
wk = 0
sltime = random.randint(0, 3)


def blocs():
    global bl_running
    global yk
    global wk
    bl = pygame.image.load("images.xcf")
    bl1 = pygame.transform.scale(bl, (wk, 300))
    screen.blit(bl1, [b1_x, yk])
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
    a = pygame.Rect((100, y), (8, 100))
    b = pygame.Rect((b1_x, yk), (wk, 300))
    if a.colliderect(b):
        print('краш')

    if is_jump and space:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
            space = False
    if bl_running:
        if b1_x > -100:
            blocs()
            b1_x -= 15
        else:
            b1_x = 1100
            yk = random.randint(80, 120)
            wk = random.randint(70, 140)
            blocs()
    isJump = True

    pg = pygame.draw.rect(screen, (0, 255, 0), (0, 250, 1000, 50))
    screen.blit(player, [100, y])
    pygame.display.update()
