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
import random
import rpg_define as idef

#----------------------------
# constant value
#----------------------------
TEXT_MARGIN: int = 5

COMMAND_FONT_SIZE: int = 20
MESSAGE_FONT_SIZE: int = 20   

#定数は全部大文字で書く文化がある！→大文字だからアンダーバーつかう
#全角スペースはエラーになる！！！！！！！気をつけて！！！！

#変数の名前も順序がある、画像名前番号→ポジションが先とか自分のお気に入り順番にする、人と開発するときは合わせる。宮内君はenemy先に書くと予測変換で出てくるし揃って綺麗！

#----------------------------
# global value
#----------------------------
# text data
textboxImg = pygame.image.load("img/textbox.100.png")
commandboxImg = pygame.image.load("img/textbox.150.png")
messageText = [""]*3

# player data
playerImg = pygame.image.load("img/battle/e_coli100.png")

# background image data
backgroundImg = pygame.image.load("img/battle/background/btlbg0.png")

# enemy data
enemyA: idef.enemy
enemyImg = pygame.image.load("img/battle/enemy/enemy1.png")
enemyNum: int = 0
enemyPosX: int = 0
enemyPosY: int = 0
enemyStep: int = 0
enemyBlink: int = 0

# attack effect data
damageEffect: int = 0
effectImg = pygame.image.load("img/battle/effect/effect_attack.png")

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
        enemyData.Name = "みずき"
        enemyData.MaxHP = 100
        enemyData.HP = 100
        enemyData.MaxMP = 100
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 20
        enemyData.DEF = -10000
        enemyData.INT = 10
        enemyData.AGI = 10
        enemyData.LUK = 10
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
    global enemyBlink, damageEffect      #関数は大文字にして、変数は小文字にしてる。宮内流。アンダーバーは打つのめんどいから使わない
    
    bx = 0
    by = 0

    # damage effect process
    if damageEffect > 0:
        damageEffect = damageEffect - 1
        bx = random.randint(-20,20)
        by = random.randint(-10,10)
    bg.blit(backgroundImg, [bx,by])

    # enemy atack scene
    if enemyBlink % 2 == 0 and enemyA.HP > 0:
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

    # Name and HP, MP show
    idef.TextDraw(bg, user.Name, playerImg.get_width() + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 25, fnt, idef.COLOR_WHITE)
    idef.TextDraw(bg, "HP：" + str(user.HP) + "/" + str(user.MaxHP), playerImg.get_width() + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 50, fnt, idef.COLOR_WHITE)
    idef.TextDraw(bg, "MP：" + str(user.MP) + "/" + str(user.MaxMP), playerImg.get_width() + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 75, fnt, idef.COLOR_WHITE)

    # command show
    for i in range(len(user.Command)):
        idef.TextDraw(bg, "[" + str(i+1) + "] " + user.Command[i], idef.WINDOW_WIDTH/2 + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 18 + i*30, fnt, idef.COLOR_WHITE)

#--------------------------------------------------
# message initialize function
#--------------------------------------------------
def MessageInit():
    for i in range(len(messageText)):
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
        idef.TextDraw(bg, messageText[i], 20, idef.WINDOW_HEIGHT - textboxImg.get_height() + 10 + i*30, fnt, idef.COLOR_WHITE)
    
#--------------------------------------------------
# battle main function
#--------------------------------------------------
def BattleMain(scr, clk, user: idef.player, emyNum: int):
    # enable change global value 
    global enemyA, enemyImg
    global enemyPosX, enemyPosY
    global enemyStep, damageEffect
    
    # local value
    timer: int = 0
    scene: int = 0
    damage: int = 0

    # font set
    commandFont = pygame.font.Font(idef.FONT_FILE_PATH, COMMAND_FONT_SIZE)
    messageFont = pygame.font.Font(idef.FONT_FILE_PATH, MESSAGE_FONT_SIZE)

    # key input setup
    pygame.key.set_repeat()

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
            MessageInit()
            scene = 12

        # wait player input
        elif scene == 12:
            # command show
            BattleCommand(user, scr, commandFont)

            # wait command secelt
            if(key[pygame.locals.K_1] == 1):
                MessageSet(str(user.Name) + "の攻撃")
                damage = user.ATK - enemyA.DEF + random.randint(0, 5)
                if damage < 0: damage = 0
                if damage > 9999: damage = 9999
                scene = 21
                timer = 0
            elif(key[pygame.locals.K_2] == 1 and len(user.Command)>=2):
                MessageSet(str(user.Name) + "の" + user.Command[1] + "による攻撃")
                damage = user.ATK - enemyA.DEF + random.randint(0, 5)
                if damage < 0: damage = 0
                scene = 22
                timer = 0
            elif(key[pygame.locals.K_3] == 1 and len(user.Command)>=3):
                MessageSet(str(user.Name) + "の" + user.Command[2] + "による攻撃")
                damage = user.ATK - enemyA.DEF + random.randint(0, 5)
                if damage < 0: damage = 0
                scene = 23
                timer = 0
            elif(key[pygame.locals.K_4] == 1 and len(user.Command)>=4):
                MessageSet(str(user.Name) + "の" + user.Command[3] + "による攻撃")
                damage = user.ATK - enemyA.DEF + random.randint(0, 5)
                if damage < 0: damage = 0
                scene = 24
                timer = 0

        # [1] 攻撃エフェクト
        elif scene == 21:
            MessageDraw(scr, messageFont)
            if 2 <= timer and timer <= 4:
                scr.blit(effectImg, [400-timer*60, -100+timer*60])

            if timer == 5:
                enemyBlink = 5
                MessageSet(enemyA.Name + "は" + str(damage) + "のダメージ")
                enemyA.HP = enemyA.HP - damage
                if(enemyA.HP <= 0):
                    scene = 51

            if timer >= 16 and key[pygame.locals.K_SPACE] == 1:
                scene = 31
                timer = 0

        # [2] コマンドエフェクト
        elif scene == 22:
            MessageDraw(scr, messageFont)
            if 2 <= timer and timer <= 4:
                scr.blit(effectImg, [400-timer*60, -100+timer*60])

            if timer == 5:
                enemyBlink = 5
                MessageSet(enemyA.Name + "は" + str(damage) + "のダメージ")
                enemyA.HP = enemyA.HP - damage
                if(enemyA.HP <= 0):
                    scene = 51

            if timer >= 16 and key[pygame.locals.K_SPACE] == 1:
                scene = 31
                timer = 0

        # [3] コマンドエフェクト
        elif scene == 23:
            MessageDraw(scr, messageFont)
            if 2 <= timer and timer <= 4:
                scr.blit(effectImg, [400-timer*60, -100+timer*60])

            if timer == 5:
                enemyBlink = 5
                MessageSet(enemyA.Name + "は" + str(damage) + "のダメージ")
                enemyA.HP = enemyA.HP - damage
                if(enemyA.HP <= 0):
                    scene = 51

            if timer >= 16 and key[pygame.locals.K_SPACE] == 1:
                scene = 31
                timer = 0

        # [4] コマンドエフェクト
        elif scene == 24:
            MessageDraw(scr, messageFont)
            if 2 <= timer and timer <= 4:
                scr.blit(effectImg, [400-timer*60, -100+timer*60])

            if timer == 5:
                enemyBlink = 5
                MessageSet(enemyA.Name + "は" + str(damage) + "のダメージ")
                enemyA.HP = enemyA.HP - damage
                if(enemyA.HP <= 0):
                    scene = 51

            if timer >= 16 and key[pygame.locals.K_SPACE] == 1:
                scene = 31
                timer = 0

        # エネミーからの攻撃
        elif scene == 31:
            MessageInit()
            MessageSet(enemyA.Name + "からの攻撃")
            damage = enemyA.ATK - user.DEF + random.randint(0,5)
            if damage < 0: damage = 0
            scene = 32

        # エネミーから攻撃エフェクト
        elif scene == 32:
            MessageDraw(scr, messageFont)
            if timer == 5:
                enemyStep = 30
            if timer == 9:
                MessageSet(user.Name + "は" + str(damage) + "のダメージ")
                user.HP = user.HP - damage
                if(user.HP <= 0):
                    scene = 101
                damageEffect = 5
                enemyStep = 0
            if timer >= 20 and key[pygame.locals.K_SPACE] == 1:
                scene = 11
                timer = 0

        # エネミーを撃破
        elif scene == 51:
            MessageDraw(scr, messageFont)
            MessageSet(user.Name + "は" + enemyA.Name + "を撃破した．")
            scene = 52

        # エネミー撃破後のキー入力待ち
        elif scene ==52:
            MessageDraw(scr, messageFont)

        # プレイヤー敗北
        elif scene == 101:
            MessageDraw(scr, messageFont)
            MessageSet(user.Name + "は敗北した．")
            scene = 102

        # プレイヤー敗北後のキー入力待ち
        elif scene == 102:
            MessageDraw(scr, messageFont)

        pygame.display.update()
        clk.tick(10)
        
#--------------------------------------------------
# end of file
#--------------------------------------------------
