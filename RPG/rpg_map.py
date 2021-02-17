'''
Project Name : iGemGunmaGameProject
File Name    : rpg_battle.py
Description  : バトルプログラムファイル
'''

#----------------------------
# import
#----------------------------
import pygame
import pygame.locals
import sys
import rpg_define as idef

DIR_L: int = -1
DIR_R: int = -2
DIR_U: int = 1
DIR_D: int = 2

soundWalk = pygame.mixer.Sound("sound/ashioto.ogg")
bgmMAP = pygame.mixer.music.load("sound/op2.ogg")

charImg = pygame.image.load("img/player/front/C-13.PNG")

frontImg = [pygame.image.load("img/player/front/C-13.PNG"),
            pygame.image.load("img/player/front/C-2.PNG"),
            pygame.image.load("img/player/front/C-13.PNG"),
            pygame.image.load("img/player/front/C-4.PNG"),
            pygame.image.load("img/player/front/C-13.PNG"),
            pygame.image.load("img/player/front/C-2.PNG")]

sideImg = [pygame.image.load("img/player/side/Cs-1.PNG"),
           pygame.image.load("img/player/side/Cs-2.PNG"),
           pygame.image.load("img/player/side/Cs-3.PNG"),
           pygame.image.load("img/player/side/Cs-4.PNG"),
           pygame.image.load("img/player/side/Cs-3.PNG"),
           pygame.image.load("img/player/side/Cs-2.PNG")]

posX: int = 0
posY: int = 0

dir: int = 0

def MapDraw(bg):
    a=0

#--------------------------------------------------
# player direction image read function
#--------------------------------------------------
def CharDraw(bg, _dir: int):
    # enable change global value
    global dir
    global charImg

    if _dir == DIR_L:
        if int(dir/10) == 0:
            dir = dir + 1
            if(dir >= 6):
                dir = 0
        else:
            dir = 0
        charImg = sideImg[dir]

    if _dir == DIR_R:
        if int(dir/10) == 1:
            dir = dir + 1
            if(dir >= 16):
                dir = 10
        else:
            dir = 10
        charImg = sideImg[5-dir+10]

    if _dir == DIR_D:
        if int(dir/10) == 2:
            dir = dir + 1
            if(dir >= 26):
                dir = 20
        else:
            dir = 20
        charImg = frontImg[dir-20]

    if _dir == DIR_U:
        if int(dir/10) == 3:
            dir = dir + 1
            if(dir >= 36):
                dir = 30
        else:
            dir = 30
        charImg = frontImg[5-dir+30]

#--------------------------------------------------
# Map Main function
#--------------------------------------------------
def MapMain(bg, clk):
    # enable change global value
    global posX, posY

    # local value
    timer: int = 0
    scene: int = 0

    # font set
    font = pygame.font.Font(idef.FONT_FILE_PATH, 20)
    
    # key input setup
    pygame.key.set_repeat(1,10000000)

    while True:
        # event skip
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # game state update
        key = pygame.key.get_pressed()
        timer = timer + 1
        
        bg.fill(idef.COLOR_WHITE)

        # 左キー入力
        if key[pygame.locals.K_LEFT] == 1:
            if(pygame.mixer.get_busy() == False):
                print("left")
                posX = posX - 1
                CharDraw(bg, DIR_L)
                print(str(posX) + ", " + str(posY))
                soundWalk.play()
            else:
                pygame.event.clear()
        
        # 右キー入力
        if key[pygame.locals.K_RIGHT] == 1:
            if(pygame.mixer.get_busy() == False):
                print("right")
                posX = posX + 1
                CharDraw(bg, DIR_R)
                print(str(posX) + ", " + str(posY))
                soundWalk.play()
            else:
                pygame.event.clear()

        # 上キー入力
        if key[pygame.locals.K_UP] == 1:
            if(pygame.mixer.get_busy() == False):
                print("up")
                posY = posY - 1
                CharDraw(bg, DIR_U)
                print(str(posX) + ", " + str(posY))
                soundWalk.play()
            else:
                pygame.event.clear()

        # 下キー入力
        if key[pygame.locals.K_DOWN] == 1:
            if(pygame.mixer.get_busy() == False):
                print("down")
                posY = posY + 1
                CharDraw(bg, DIR_D)
                print(str(posX) + ", " + str(posY))
                soundWalk.play()
            else:
                pygame.event.clear()

        bg.blit(charImg,[idef.WINDOW_WIDTH/2 -32, idef.WINDOW_HEIGHT/2 -32])
        pygame.display.update()
        clk.tick(20)

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------