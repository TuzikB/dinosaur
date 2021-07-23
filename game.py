import pygame
import random
import time
import os
import pathlib
# from button import InputBox
leader1_name = ""
leader1_score = ""
leader2_name = ""
leader2_score = ""
leader3_name = ""
leader3_score = ""
def rek():
    global leader1_name, leader1_score, leader2_name, leader2_score, leader3_name, leader3_score
    rekordy1 = dict()
    rekord_name = []
    path = pathlib.Path().resolve()
    files = os.listdir(path)
    record_score = []
    f = open("rekordy.txt", "r")
    for i in f:
        record_score.append(int(i.split()[1]))
        leader1_score = max(record_score)
        rekord_name.append(i.split()[0])
    f.close()
    index = record_score.index(leader1_score)
    leader1_name = rekord_name[index]
    record_score.pop(index)
    rekord_name.pop(index)
    leader2_score = max(record_score)
    index2 = record_score.index(leader2_score)
    leader2_name = rekord_name[index2]
    record_score.pop(index2)
    rekord_name.pop(index2)
    leader3_score = max(record_score)
    index3 = record_score.index(leader3_score)
    leader3_name = rekord_name[index3]
    record_score.pop(index3)
    rekord_name.pop(index3)
    print(leader1_name, leader1_score)
    print(leader2_name, leader2_score)
    print(leader3_name, leader3_score)
    # for name, score in rekordy:
    #     print(f"{name}: {score}")
    #     rekordy1[score] = name
    print(rekordy1)
running = True
name = ""
deaths = {"bird": " был унесён в гнездо птеродактиля.",
          "hole": " упал в яму и разбился.",
          "cact": " напоролся на ядовитый кактус.",
          "bul": " был застрелен из пистолета анонимусом."}
badness = pygame.image.load("badnotgood-removebg-preview.png")
badness = pygame.transform.scale(badness, (80, 100))
lc = 0
infotext = "Нажмите пробел чтобы прыгнуть, стрелки вверх и вниз "
infotext2 = "чтобы лечь и встать, shift чтобы выстрелить."
running = True
pygame.init()
screen = pygame.display.set_mode([1000, 300])
screen.fill([255, 255, 255])
start = False
player = pygame.image.load("10544.png")
player = pygame.transform.scale(player, (80, 100))
bulx = 800
buly = 180
gbulx = 240
gbuly = 200
speed = 25
y = 155
xh = 1000
b1_x = 1000
xb = 1000
run = True
bird = pygame.image.load("bird.xcf")
bird = pygame.transform.scale(bird, (300, 200))
# bird = pygame.transform.rotate(bird, -90)

screen.blit(player, [100, y])
pg = pygame.draw.rect(screen, (0, 0, 0), (0, 250, 1000, 50))
space = False
x2 = 0
hl = pygame.image.load("drawing-1.svg")
hl = pygame.transform.scale(hl, (100, 100))
myfont = pygame.font.SysFont('Comic Sans MS', 50)
yk = 0
wk = 0
sltime = random.randint(0, 3)
lives = 3
score = 0
is_jump_up = True
bad = False
fdelay = 0
pos = 0
press = False
info = False
buttonexit = pygame.draw.rect(screen, (255, 0, 0), (800, 200, 200, 100))
buttonhexit = pygame.Rect((800, 200), (200, 100))
buttonstart = pygame.draw.rect(screen, (0, 0, 255), (100, 100, 200, 100))
buttonhstart = pygame.Rect((100, 100), (200, 100))
buttoninfo = pygame.draw.rect(screen, (255, 0, 0), (400, 100, 200, 100))
buttonhinfo = pygame.Rect((400, 100), (200, 100))
# input_box1 = InputBox(100, 100, 140, 32)
input_rect = pygame.draw.rect(screen, (255, 255, 255), (100, 100, 200, 100))
active = False
user_text = ""
is_jump = True
jumpCount = 10
bl_running = False
b_running = False
hl_running = True
bul_running = False
gbul_running = False
clock = pygame.time.Clock()
buttonr = pygame.draw.rect(screen, (0, 0, 250), (100, 100, 200, 100))
buttonhr = pygame.Rect((100, 100), (200, 100))
reiting = False
def startg():
    global screen, start, running, info, infotext, infotext2, buttonexit, buttonhexit, buttonstart, buttonhstart, buttoninfo, buttonhinfo
    global speed, score, lives, run, input_rect, active, user_text, name, bl_running, bul_running, b_running, hl_running, gbul_runningб, bad
    global buttonhr, buttonr, gbul_running, reiting, leader1_name, leader1_score, leader2_name, leader2_score, leader3_score, leader3_name
    bl_running = False
    b_running = False
    hl_running = True
    bul_running = False
    gbul_running = False
    bad = False
    while not start:
        if not info and not reiting:
            speed = 25
            score = 0
            lives = 3
            # input_box1 = InputBox(100, 100, 140, 32)
            pg = pygame.draw.rect(screen, (0, 100, 0), (0, 0, 1000, 300))
            input_rect = pygame.draw.rect(screen, (255, 255, 255), (400, 220, 500, 50))
            name_text = myfont.render("Type your name here:", False, (0, 0, 0))
            screen.blit(name_text, (10, 230))
            buttonstart = pygame.draw.rect(screen, (0, 0, 250), (100, 100, 200, 100))
            buttonhstart = pygame.Rect((100, 100), (200, 100))
            buttonr = pygame.draw.rect(screen, (0, 255, 0), (700, 100, 200, 100))
            buttonhr = pygame.Rect((700, 100), (200, 100))
            buttonrtext = myfont.render("РЕЙТИНГ", False, (0, 0, 0))
            screen.blit(buttonrtext, (720, 140))
            text = myfont.render("START", False, (0, 0, 0))
            screen.blit(text, (150, 140))
            buttoninfo = pygame.draw.rect(screen, (250, 0, 0), (400, 100, 200, 100))
            buttonhinfo = pygame.Rect((400, 100), (200, 100))
            text = myfont.render("INFO", False, (0, 0, 0))
            screen.blit(text, (450, 140))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            active = False
        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()
            press = pygame.mouse.get_pressed()
            if e.type == pygame.QUIT:
                # print(e)
                pygame.quit()
                # run = False
                # start = True
                # running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(e.pos):
                    active = True
                    user_text = ""
                    # print(active)
            if buttonhstart.collidepoint(pos) and press[0] == True:
                if user_text != "":
                    name = user_text[:-1]
                    start = True
            if buttonhr.collidepoint(pos) and press[0] == True:
                print("ghjk")
                reiting = True
                ekr = pygame.draw.rect(screen, (0, 100, 0), (0, 0, 1000, 300))
                pg = pygame.draw.rect(screen, (255, 255, 255), (100, 100, 500, 150))
                rekord1 = myfont.render(f"{leader1_name}: {leader1_score}", False, (0, 0, 0))
                rekord2 = myfont.render(f"{leader2_name}: {leader2_score}", False, (0, 0, 0))
                rekord3 = myfont.render(f"{leader3_name}: {leader3_score}", False, (0, 0, 0))
                buttonexit = pygame.draw.rect(screen, (255, 0, 0), (800, 200, 180, 100))
                buttonhexit = pygame.Rect((800, 200), (200, 100))
                text = myfont.render("EXIT", False, (0, 0, 0))
                screen.blit(text, (820, 240))
                screen.blit(rekord1, (110, 110))
                screen.blit(rekord2, (110, 150))
                screen.blit(rekord3, (110, 190))
            if e.type == pygame.KEYDOWN:

                # Check for backspace
                if e.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += e.unicode
            if buttonhinfo.collidepoint(pos) and press[0] == True:
                info = True
                pg = pygame.draw.rect(screen, (0, 100, 0), (0, 0, 1000, 300))
                infotxt = myfont.render(infotext, False, (0, 0, 0))
                infotxt2 = myfont.render(infotext2, False, (0, 0, 0))
                buttonexit = pygame.draw.rect(screen, (255, 0, 0), (800, 200, 180, 100))
                buttonhexit = pygame.Rect((800, 200), (200, 100))
                text = myfont.render("EXIT", False, (0, 0, 0))
                screen.blit(text, (820, 240))
                screen.blit(infotxt, (10, 10))
                screen.blit(infotxt2, (10, 50))
            if buttonhexit.collidepoint(pos) and press[0] == True:
                info = False
                reiting = False
        if active and not info and not reiting:
            nametext = myfont.render(user_text, True, (0, 0, 0))
            screen.blit(nametext, (input_rect.x + 5, input_rect.y + 5))
        pygame.display.update()


def death(ob):
    global b1_x, y, lives, score, running, xb, xh, deaths, speed
    b1_x = 1050
    xb = 1000
    xh = 1000
    if ob == "bird":
        lives -= 3
        score -= 100
        speed -= 5
    if ob == "hole":
        lives -= 2
        score -= 100
        speed -= 1
    if ob == "cact":
        lives -= 1
        score -= 100
        speed -= 1
    if ob == "bul":
        lives -= 1
        score -= 100
        speed -= 1
    if lives <= 0:
        f = open("rekordy.txt", "a", encoding="utf-8")
        rekordy = f.write(f"{name} {score}" + '\n')
        f.close()
        myfont1 = pygame.font.SysFont('Comic Sans MS', 100)
        myfont2 = pygame.font.SysFont('Comic Sans MS', 40)
        pg = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 1000, 300))
        textsurface = myfont1.render("GAME OVER", False, (0, 0, 0))
        screen.blit(textsurface, (300, 100))
        textsurface2 = myfont2.render(f"{name}{deaths[ob]}", False, (0, 0, 0))
        screen.blit(textsurface2, (300, 180))
        textsurface3 = myfont2.render(f"Счёт: {score}", False, (0, 0, 0))
        screen.blit(textsurface3, (300, 210))
        pygame.display.update()
        time.sleep(5)
        running = False


def bullet():
    global bulx, buly
    b = 0
    if bad:
        b = pygame.draw.rect(screen, (0, 0, 0), (bulx, buly, 10, 10))
    return b


def goodbullet():
    global gbulx, gbuly
    gb = 0
    gb = pygame.draw.rect(screen, (0, 0, 0), (gbulx, gbuly, 10, 10))
    return gb


def cact():
    global bl_running
    global yk
    global wk
    bl = pygame.image.load("images.xcf")
    bl1 = pygame.transform.scale(bl, (wk, 300))
    screen.blit(bl1, [b1_x, yk])
    return bl1


def hole():
    global hl_running
    global xh
    global hl
    screen.blit(hl, [xh, 250])
    return hl


def fly():
    global xb
    global bird
    screen.blit(bird, [xb, 30])
    return bird


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = myfont.render(fps, 1, pygame.Color("coral"))
    return fps_text





def play():
    global running, gbul_running, bul_running, b_running, bl_running, hl_running, y, yk, gbuly, buly, hl, xh, xb, x2, score, speed, b1_x, wk, bulx, gbulx, bad, space
    global player, is_jump, jumpCount, is_jump_up, fdelay, lcб, run, lc
    while running:

        textsurface_s = myfont.render(f"Score: {score} ", False, (0, 0, 0))
        textsurface_l = myfont.render(f" Lives: {lives}", False, (0, 0, 0))
        textsurface_n = myfont.render(f"Name: {name} ", False, (0, 0, 0))
        clock.tick(speed)
        screen.fill([255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        a = pygame.Rect((200, y), (8, 100))
        b = pygame.Rect((b1_x, yk), (wk, 300))
        c = pygame.Rect((0, 250), (1000, 50))
        d = pygame.Rect((xh, 250), (50, 200))
        e = pygame.Rect((xb, 30), (100, 150))
        f = pygame.Rect((-100, 0), (1, 300))
        bu = pygame.Rect((bulx, buly), (10, 10))
        gbu = pygame.Rect((gbulx, gbuly), (5, 5))
        an = pygame.Rect((800, 150), (80, 100))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            # print("space")
            space = True
        if keys[pygame.K_RSHIFT]:
            # print("space")
            gbul_running = True
        if keys[pygame.K_DOWN]:
            # print("down")
            if lc == 0:
                player = pygame.transform.rotate(player, -90)
                y += 50
                a = pygame.Rect((200, y), (100, 8))

                lc = 1
        if keys[pygame.K_UP]:
            # print("up")
            if lc:
                player = pygame.transform.rotate(player, 90)
                y -= 50
                a = pygame.Rect((200, y), (8, 100))
                lc = 0
        if a.colliderect(b):
            death("cact")
            run = True
            # print('краш')
        if a.colliderect(d):
            death("hole")
            run = True
            # print('краш')
        if a.colliderect(e):
            death("bird")
            # print('краш')
            run = True
        if b.colliderect(f):
            score += 50
            speed += 0.30
        if d.colliderect(f):
            score += 50
            speed += 0.35
        if e.colliderect(f):
            score += 50
            speed += 0.30

        if a.colliderect(bu):
            death("bul")
            run = True
        if gbu.colliderect(an):
            print("edrftghj")
            bad = False
            score += 100

        if bad == False and random.randint(1, 1000) == 1:
            bad = True

        if is_jump and space:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            elif a.colliderect(c):
                jumpCount = 10
                isJump = False
                space = False
        if bl_running:
            if b1_x > -100:
                cact()
                b1_x -= 15
            else:
                b1_x = 1100
                yk = random.randint(90, 120)
                wk = random.randint(80, 120)
                pygame.draw.rect(screen, (0, 255, 0), (0, 250, 1000, 50))
                # score += 50
                b_running = True
                bl_running = False

        if hl_running:
            if xh > -100:
                hole()
                xh -= 15
            else:
                xh = 1000
                pygame.draw.rect(screen, (0, 255, 0), (0, 250, 1000, 50))
                # score += 50
                # print("ghjk")

                hl_running = False
                bl_running = True
        if b_running:
            if xb > -100:
                fly()
                xb -= 15
            else:
                xb = 1000
                pygame.draw.rect(screen, (0, 255, 0), (0, 250, 1000, 50))
                # score += 50
                hl_running = True
                b_running = False
        if bul_running:
            if bulx > -100:
                bullet()
                bulx -= 25
            else:
                bulx = 800
                pygame.draw.rect(screen, (0, 255, 0), (0, 250, 1000, 50))
                # score += 50
                bul_running = False
                if speed < 30:
                    fdelay = 20
                else:
                    fdelay = 35
        if gbul_running:
            if gbulx < 1000:
                goodbullet()
                gbulx += 30
            else:
                gbulx = 240
                pygame.draw.rect(screen, (0, 255, 0), (0, 250, 1000, 50))
                # score += 50
                gbul_running = False
        isJump = True
        if speed > 39:
            speed = 25
        pg = pygame.draw.rect(screen, (0, 255, 0), (0, 250, 1000, 50))

        screen.blit(player, [200, y])
        screen.blit(textsurface_s, (0, 0))
        screen.blit(textsurface_l, (300, 0))
        screen.blit(textsurface_n, (600, 0))
        screen.blit(hl, [xh, 250])
        bullet()
        if bad:
            if bul_running == False and fdelay == 0:
                bul_running = True
            if fdelay != 0:
                fdelay -= 1
            screen.blit(badness, (800, 150))
        # screen.blit(update_fps(), (100, 100))
        pygame.display.update()


while run:
    # print(start, running)
    rek()
    bulx = 800
    buly = 180
    startg()
    play()
    start = False
    running = True
    name = ""
    user_text = ""
