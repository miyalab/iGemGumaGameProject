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

#----------------------------
# constant value
#----------------------------
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
mapImg = [pygame.image.load("img/map/clear.PNG"),
          pygame.image.load("img/map/t01.PNG"),
          pygame.image.load("img/map/t02.PNG"),
          pygame.image.load("img/map/t03.PNG"),
          pygame.image.load("img/map/t04.PNG"),
          pygame.image.load("img/map/t05.PNG"),
          pygame.image.load("img/map/t06.PNG"),
          pygame.image.load("img/map/t07.PNG"),
          pygame.image.load("img/map/t08.PNG"),
          pygame.image.load("img/map/t09.PNG"),
          pygame.image.load("img/map/t10.PNG"),
          pygame.image.load("img/map/t11.PNG"),
          pygame.image.load("img/map/t12.PNG"),
          pygame.image.load("img/map/t13.PNG"),
          pygame.image.load("img/map/t14.PNG"),
          pygame.image.load("img/map/t15.PNG"),
          pygame.image.load("img/map/t16.PNG"),
          pygame.image.load("img/map/t17.PNG"),
          pygame.image.load("img/map/t18.PNG"),
          pygame.image.load("img/map/t19.PNG"),
          pygame.image.load("img/map/t20.PNG"),
          pygame.image.load("img/map/t21.PNG"),
          pygame.image.load("img/map/t22.PNG"),
          pygame.image.load("img/map/t23.PNG"),
          pygame.image.load("img/map/t24.PNG"),
          pygame.image.load("img/map/t25.PNG"),
          pygame.image.load("img/map/t26.PNG"),
          pygame.image.load("img/map/t27.PNG"),
          pygame.image.load("img/map/t28.PNG"),
          pygame.image.load("img/map/t29.PNG"),
          pygame.image.load("img/map/t30.PNG"),
          pygame.image.load("img/map/t31.PNG"),
          pygame.image.load("img/map/t32.PNG"),
          pygame.image.load("img/map/t33.PNG"),
          pygame.image.load("img/map/t34.PNG"),
          pygame.image.load("img/map/t35.PNG"),
          pygame.image.load("img/map/t36.PNG"),
          pygame.image.load("img/map/t37.PNG"),
          pygame.image.load("img/map/t38.PNG"),
          pygame.image.load("img/map/t39.PNG"),
          pygame.image.load("img/map/t40.PNG"),
          pygame.image.load("img/map/t41.PNG"),
          pygame.image.load("img/map/t42.PNG"),
          pygame.image.load("img/map/t43.PNG"),
          pygame.image.load("img/map/t44.PNG"),
          pygame.image.load("img/map/t45.PNG"),
          pygame.image.load("img/map/t46.PNG"),
          pygame.image.load("img/map/t47.PNG"),
          pygame.image.load("img/map/t48.PNG"),
          pygame.image.load("img/map/t49.PNG"),
          pygame.image.load("img/map/t50.PNG"),
          pygame.image.load("img/map/t51.PNG"),
          pygame.image.load("img/map/t52.PNG"),
          pygame.image.load("img/map/t53.PNG"),
          pygame.image.load("img/map/t54.PNG"),
          pygame.image.load("img/map/t55.PNG"),
          pygame.image.load("img/map/t56.PNG"),
          pygame.image.load("img/map/t57.PNG"),
          pygame.image.load("img/map/t58.PNG"),
          pygame.image.load("img/map/t59.PNG"),
          pygame.image.load("img/map/t60.PNG")]
overMapImg = [pygame.image.load("img/map/clear.PNG"),
              pygame.image.load("img/map/a01.PNG"),
              pygame.image.load("img/map/a02.PNG"),
              pygame.image.load("img/map/a03.PNG"),
              pygame.image.load("img/map/a04.PNG"),
              pygame.image.load("img/map/a05.PNG"),
              pygame.image.load("img/map/a06.PNG"),
              pygame.image.load("img/map/a07.PNG"),
              pygame.image.load("img/map/a08.PNG"),
              pygame.image.load("img/map/a09.PNG"),
              pygame.image.load("img/map/a10.PNG"),
              pygame.image.load("img/map/a11.PNG"),
              pygame.image.load("img/map/a12.PNG"),
              pygame.image.load("img/map/a13.PNG"),
              pygame.image.load("img/map/a14.PNG"),
              pygame.image.load("img/map/a15.PNG"),
              pygame.image.load("img/map/a16.PNG"),
              pygame.image.load("img/map/a17.PNG"),
              pygame.image.load("img/map/a18.PNG"),
              pygame.image.load("img/map/a19.PNG"),
              pygame.image.load("img/map/a20.PNG"),
              pygame.image.load("img/map/a21.PNG"),
              pygame.image.load("img/map/a22.PNG"),
              pygame.image.load("img/map/a23.PNG"),
              pygame.image.load("img/map/a24.PNG"),
              pygame.image.load("img/map/a25.PNG"),
              pygame.image.load("img/map/a26.PNG"),
              pygame.image.load("img/map/a27.PNG"),
              pygame.image.load("img/map/a28.PNG"),
              pygame.image.load("img/map/a29.PNG"),
              pygame.image.load("img/map/a30.PNG"),
              pygame.image.load("img/map/a31.PNG"),
              pygame.image.load("img/map/a32.PNG"),
              pygame.image.load("img/map/a33.PNG"),
              pygame.image.load("img/map/a34.PNG"),
              pygame.image.load("img/map/a35.PNG"),
              pygame.image.load("img/map/a36.PNG"),
              pygame.image.load("img/map/a37.PNG"),
              pygame.image.load("img/map/a38.PNG"),
              pygame.image.load("img/map/a39.PNG"),
              pygame.image.load("img/map/a40.PNG"),
              pygame.image.load("img/map/a41.PNG"),
              pygame.image.load("img/map/a42.PNG"),
              pygame.image.load("img/map/a43.PNG"),
              pygame.image.load("img/map/a44.PNG"),
              pygame.image.load("img/map/a45.PNG"),
              pygame.image.load("img/map/a46.PNG"),
              pygame.image.load("img/map/a47.PNG"),
              pygame.image.load("img/map/a48.PNG"),
              pygame.image.load("img/map/a49.PNG"),
              pygame.image.load("img/map/a50.PNG"),
              pygame.image.load("img/map/a51.PNG"),
              pygame.image.load("img/map/a52.PNG"),
              pygame.image.load("img/map/a53.PNG"),
              pygame.image.load("img/map/a54.PNG"),
              pygame.image.load("img/map/a55.PNG"),
              pygame.image.load("img/map/a56.PNG"),
              pygame.image.load("img/map/a57.PNG"),
              pygame.image.load("img/map/a58.PNG"),
              pygame.image.load("img/map/a59.PNG"),
              pygame.image.load("img/map/a60.PNG"),
              pygame.image.load("img/map/a61.PNG"),
              pygame.image.load("img/map/a62.PNG"),
              pygame.image.load("img/map/a63.PNG"),
              pygame.image.load("img/map/a64.PNG")]



nowMap = [[]]

posX: int = 0
posY: int = 0

dir: int = 0

#--------------------------------------------------
# Map Draw function
#--------------------------------------------------
def MapDraw(bg, _x: int, _y: int):
    x = _x - 6
    y = _y - 5
    selectIndex: int = 0

    bg.fill(idef.COLOR_WHITE)
    for j in range(9):
        if y + j < 0 or y + j >= len(nowMap) :
           continue

        for i in range(11):
            if x + i < 0 or x + i >= len(nowMap[y+j]):
               continue
            
            #print(str(len(nowMap[y+j])) + "," + str(len(nowMap)) + "," + str(x+i) + "," + str(y+j) + "," + str(nowMap[y+j][x+i]))
            selectIndex = nowMap[y+j][x+i]
            bg.blit(mapImg[selectIndex % 100], [64 * i - 32, 64 * j - 32])
            selectIndex = int(selectIndex / 100)
            bg.blit(overMapImg[selectIndex % 100], [64 * i - 32, 64 * j - 32])

#--------------------------------------------------
# Map Data Load function
#--------------------------------------------------
def MapLoad(_map: int):
    ret = [[]]
    ret.clear()

    # map 
    if _map == 0:
        ret.append([1230,30,1130,2430,1230,0,0,0,4730,1130,4230,1330,430,30,0])
        ret.append([54,54,54,54,54,0,0,0,54,54,54,54,54,54,0])
        ret.append([54,54,54,54,54,0,0,0,2154,1854,1754,54,10154,54,0])
        ret.append([54,20254,54,54,54,0,0,0,54,2954,2054,54,54,30354,0])
        ret.append([54,1754,54,54,54,0,0,0,54,1754,1854,54,54,54,0,0,0,0,30,4730,30,30,30,30])
        ret.append([54,54,54,54,54,0,0,0,54,2954,2954,2154,54,54,0,0,0,0,54,5801754,54,1754,54,1454])
        ret.append([0,0,0,54,0,0,0,0,0,0,54,0,0,0,0,0,0,0,54,1754,54,1754,54,54])
        ret.append([54,54,54,54,54,54,54,54,4854,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54])
        ret.append([54,54,54,54,54,54,54,54,54,54,54,3254,4654,54,54,54,54,54,4554,1754,54,1754,54,54])
        ret.append([0,0,0,0,0,0,0,0,0,0,6436,6336,0,0,0,0,0,0,54,1854,54,1754,54,54])
        ret.append([0,0,0,0,0,0,0,0,0,0,36,3636,0,0,0,0,0,0,54,1754,54,1754,54,54])
        ret.append([0,0,0,0,0,0,0,0,0,0,60,59,0,0,0,0,0,0,0,0,0,0,0,0])

    elif _map == 1:
        ret.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,3])
        ret.append([1,2,2,2,2,2,2,2,2,2,3,0,0,0,4,5,5,5,5,5,5,5,6])
        ret.append([4,5,5,5,5,5,5,5,5,5,6,0,0,0,4,5,5,5,5,5,5,5,6])
        ret.append([7,8,8,8,8,8,8,8,8,8,9,0,0,0,7,8,8,8,8,8,8,8,9])
        ret.append([31,31,31,31,31,31,31,31,31,31,31,44,39,43,16,17,16,17,16,17,19])
        ret.append([31,31,31,31,31,31,31,31,31,31,31,44,39,43,18,16,16,16,16,16,19])
        ret.append([31,31,31,31,31,31,31,31,31,31,31,44,39,43,18,17,16,17,16,17,19])
        ret.append([30,30,30,30,30,30,30,30,30,30,30,44,39,43,18,16,16,16,16,16,19])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,44,39,43,18,16,16,20,16,16,19])
        ret.append([47,47,47,47,47,47,47,47,47,47,47,44,39,43,47,47,47,47,47,47,47])
        ret.append([39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39])
        ret.append([39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])

    elif _map == 2:
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])
        ret.append([0,0,0,0,0,0,0,0])

    return ret

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
    global nowMap

    # local value
    timer: int = 0
    scene: int = 0

    # font set
    font = pygame.font.Font(idef.FONT_FILE_PATH, 20)
    
    # key input setup
    pygame.key.set_repeat(1,10000000)

    nowMap = MapLoad(0)
    #print(nowMap)

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
            if pygame.mixer.get_busy() == False:
                #print("left")
                posX = posX - 1
                CharDraw(bg, DIR_L)
                print(str(posX) + ", " + str(posY))
                soundWalk.play()
            else:
                pygame.event.clear()
        
        # 右キー入力
        if key[pygame.locals.K_RIGHT] == 1:
            if pygame.mixer.get_busy() == False:
                #print("right")
                posX = posX + 1
                CharDraw(bg, DIR_R)
                print(str(posX) + ", " + str(posY))
                soundWalk.play()
            else:
                pygame.event.clear()

        # 上キー入力
        if key[pygame.locals.K_UP] == 1:
            if pygame.mixer.get_busy() == False:
                #print("up")
                posY = posY - 1
                CharDraw(bg, DIR_U)
                print(str(posX) + ", " + str(posY))
                soundWalk.play()
            else:
                pygame.event.clear()

        # 下キー入力
        if key[pygame.locals.K_DOWN] == 1:
            if pygame.mixer.get_busy() == False:
                #print("down")
                posY = posY + 1
                CharDraw(bg, DIR_D)
                print(str(posX) + ", " + str(posY))
                soundWalk.play()
            else:
                pygame.event.clear()
        
        MapDraw(bg, posX, posY)
        bg.blit(charImg,[idef.WINDOW_WIDTH/2 -32, idef.WINDOW_HEIGHT/2 -32])
        pygame.display.update()
        clk.tick(20)

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------