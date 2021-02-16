'''
Project Name : iGemGunmaGameProject
File Name    : rpg_battle.py
Description  : バトルプログラムファイル
'''

#----------------------------
# import
#----------------------------
import rpg_define as idef
import const
import pygame
import pygame.locals
import sys
import random
from typing import List

#----------------------------
# constant value
#----------------------------
TEXT_MARGIN: int = 5

COMMAND_FONT_SIZE: int = 20
MESSAGE_FONT_SIZE: int = 20

#----------------------------
# global value
#----------------------------
fontFile = "ipaexg.ttf"
textboxImg = pygame.image.load("img/textbox.100.png")
commandboxImg = pygame.image.load("img/textbox.150.png")

playerImg = pygame.image.load("img/battle/e_coli100.png")

backgroundImg = pygame.image.load("img/battle/background/btlbg0.png")

enemyA: idef.enemy
enemyImg = pygame.image.load("img/battle/enemy/enemy1.png")
enemyNum: int = 0
enemyPosX: int = 0
enemyPosY: int = 0
enemyStep: int = 0
enemyBlink: int = 0

damageEffect: int = 0
effectImg = pygame.image.load("img/battle/effect/effect_attack.png")

messageText = [""]*3

#--------------------------------------------------
# enemy info read function
#--------------------------------------------------
def EnemyRead(_enemy: int) -> idef.enemy:
    enemyData: idef.enemy = idef.enemy()
    if _enemy == 1:
        enemyData.Num = 1
        enemyData.ImgPath = "img/battle/enemy/enemy1.png"
        enemyData.Name = "first boss"
        enemyData.MaxHP = 100
        enemyData.HP = 100
        enemyData.MaxMP = 100
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 100
        enemyData.DEF = 100
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

    elif _enemy == 2:
        enemyData.Num = 2
        enemyData.ImgPath = "img/battle/enemy/enemy2.png"
        enemyData.Name = "secound boss"
        enemyData.MaxHP = 100
        enemyData.HP = 100
        enemyData.MaxMP = 100
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 100
        enemyData.DEF = 100
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

    elif _enemy == 3:
        enemyData.Num = 3
        enemyData.ImgPath = "img/battle/enemy/enemy3.png"
        enemyData.Name = "third boss"
        enemyData.MaxHP = 100
        enemyData.HP = 100
        enemyData.MaxMP = 100
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 100
        enemyData.DEF = 100
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

    else:
        enemyData.ImgPath = "img/battle/enemy/enemy4.png"
        enemyData.Num = 4
        enemyData.Name = "last boss"
        enemyData.MaxHP = 100
        enemyData.HP = 100
        enemyData.MaxMP = 100
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 100
        enemyData.DEF = 100
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

    return enemyData

#--------------------------------------------------
# battle initialize function
#--------------------------------------------------
def BattleInit(emy:int):
    global enemyA, enemyImg
    enemyA = EnemyRead(emy)
    enemyImg = pygame.image.load(enemyA.ImgPath)

#--------------------------------------------------
# battle screen draw function
#--------------------------------------------------
def BattleDraw(bg, fnt):
    global enemyBlink, damageEffect
    
    bx = 0
    by = 0

    # damage effect process
    if damageEffect > 0:
        damageEffect = damageEffect - 1
        bx = random.randint(-20,20)
        by = random.randint(-10,10)
    bg.blit(backgroundImg, [bx,by])

    # enemy atack scene
    if enemyBlink % 2 == 0:
        bg.blit(enemyImg, [enemyPosX, enemyPosY - enemyStep])

    if enemyBlink > 0:
        enemyBlink = enemyBlink - 1

#--------------------------------------------------
# battle command draw function
#--------------------------------------------------
def BattleCommand(user: idef.player, bg, fnt):
    # command box show
    bg.blit(commandboxImg,[0,idef.WINDOW_HEIGHT - commandboxImg.get_height()])

    # player image show
    bg.blit(playerImg, [25,idef.WINDOW_HEIGHT - commandboxImg.get_height() + 25])

    # HP MP show
    TextDraw(bg, "HP：" + str(user.HP) + "/" + str(user.MaxHP), playerImg.get_width() + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 25, fnt, idef.COLOR_WHITE)
    TextDraw(bg, "MP：" + str(user.MP) + "/" + str(user.MaxMP), playerImg.get_width() + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 50, fnt, idef.COLOR_WHITE)

    # command show
    for i in range(len(user.Command)):
        TextDraw(bg, user.Command[i], idef.WINDOW_WIDTH/2, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 18 + i*30, fnt, idef.COLOR_WHITE)

#--------------------------------------------------
# message initialize function
#--------------------------------------------------
def MessageInit():
    for i in range(10):
        messageText[i] = ""

#--------------------------------------------------
# message set function
#--------------------------------------------------
def MessageSet(msg: str):
    # すべてのメッセージが埋まっていない場合は後ろに挿入
    for i in range(len(messageText)):
        if messageText[i] == "":
            messageText[i] = msg
            return

    # メッセージが埋まっている場合には1つずつずらす
    for i in range(len(messageText) - 1):
        messageText[i]= messageText[i+1]

    messageText[len(messageText) - 1] = msg

#--------------------------------------------------
# message draw function
#--------------------------------------------------
def MessageDraw(bg, fnt):
    # messagebox show
    bg.blit(textboxImg,[0,idef.WINDOW_HEIGHT - textboxImg.get_height()])

    # message show
    for i in range(len(messageText)):
        TextDraw(bg, messageText[i], 20, idef.WINDOW_HEIGHT - textboxImg.get_height() + 10 + i*30, fnt, idef.COLOR_WHITE)

#--------------------------------------------------
# text draw function
#--------------------------------------------------
def TextDraw(bg, txt, x, y, fnt, col):
    sur = fnt.render(txt, True, idef.COLOR_BLACK)
    bg.blit(sur, [x+1, y+2])
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])
    
#--------------------------------------------------
# battle main function
#--------------------------------------------------
def BattleMain(scr, clk, user: idef.player, emyNum: int):
    # enable change global value 
    global enemyA, enemyImg
    global enemyPosX, enemyPosY
    
    # local value
    timer: int = 0
    scene: int = 0

    # font set
    commandFont = pygame.font.Font("ipaexg.ttf", COMMAND_FONT_SIZE)
    messageFont = pygame.font.Font("ipaexg.ttf", MESSAGE_FONT_SIZE)

    # read enemy data
    enemyA = EnemyRead(emyNum)
    enemyImg = pygame.image.load(enemyA.ImgPath)
    enemyPosX = idef.WINDOW_WIDTH/2 - enemyImg.get_width()/2
    enemyPosY = idef.WINDOW_HEIGHT/2 - enemyImg.get_height()

    while scene >= 0:
        # event skip
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # game state update
        BattleDraw(scr, messageFont)
        key = pygame.key.get_pressed()
        timer = timer + 1

        # battle start
        if scene == 0:
            MessageSet(enemyA.Name + "があらわれた．");
            scene = 1

        elif scene == 1:
            # Messagebox show
            MessageDraw(scr, messageFont)

            # wait space input
            if key[pygame.locals.K_SPACE] == 1:
                # user input state scene
                scene = 11

        # user input state
        elif scene == 11:
            # command show
            BattleCommand(user, scr, commandFont)

            if(key[pygame.locals.K_a] == 1):
                scene = -1

        pygame.display.update()
        clk.tick(10)
        
#--------------------------------------------------
# end of file
#--------------------------------------------------
