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
KEY_MOVE: int = 0x0f
KEY_UP: int = 0x01
KEY_DOWN: int = 0x02
KEY_LEFT: int = 0x04
KEY_RIGHT: int = 0x08
KEY_SELECT: int = 0x10 

MAP_IMG_ITEM: int = 1000

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
          pygame.image.load("img/map/t60.PNG"),
          pygame.image.load("img/map/t61.PNG"),
          pygame.image.load("img/map/t62.PNG"),
          pygame.image.load("img/map/t63.PNG"),
          pygame.image.load("img/map/t64.PNG"),
          pygame.image.load("img/map/t65.PNG"),
          pygame.image.load("img/map/t66.PNG"),
          pygame.image.load("img/map/t67.PNG"),
          pygame.image.load("img/map/t68.PNG"),
          pygame.image.load("img/map/t69.PNG"),
          pygame.image.load("img/map/t70.PNG"),
          pygame.image.load("img/map/t71.PNG"),
          pygame.image.load("img/map/t72.PNG"),
          pygame.image.load("img/map/t73.PNG"),
          pygame.image.load("img/map/t74.PNG"),
          pygame.image.load("img/map/t75.PNG"),
          pygame.image.load("img/map/t76.PNG"),
          pygame.image.load("img/map/t77.PNG"),
          pygame.image.load("img/map/t78.PNG"),
          pygame.image.load("img/map/t79.PNG"),
          pygame.image.load("img/map/t80.PNG"),
          pygame.image.load("img/map/t81.PNG"),
          pygame.image.load("img/map/t82.PNG"),
          pygame.image.load("img/map/t83.PNG"),
          pygame.image.load("img/map/t84.PNG"),
          pygame.image.load("img/map/t85.PNG"),
          pygame.image.load("img/map/t86.PNG"),
          pygame.image.load("img/map/t87.PNG"),
          pygame.image.load("img/map/t88.PNG"),
          pygame.image.load("img/map/t89.PNG"),
          pygame.image.load("img/map/t90.PNG"),
          pygame.image.load("img/map/t91.PNG"),
          pygame.image.load("img/map/t92.PNG"),
          pygame.image.load("img/map/t93.PNG"),
          pygame.image.load("img/map/t94.PNG"),
          pygame.image.load("img/map/t95.PNG"),
          pygame.image.load("img/map/t96.PNG"),
          pygame.image.load("img/map/t97.PNG"),
          pygame.image.load("img/map/t98.PNG"),
          pygame.image.load("img/map/t99.PNG"),
          pygame.image.load("img/map/t100.PNG"),
          pygame.image.load("img/map/t101.PNG"),
          pygame.image.load("img/map/t102.PNG"),
          pygame.image.load("img/map/t103.PNG"),
          pygame.image.load("img/map/t104.PNG"),
          pygame.image.load("img/map/t105.PNG"),
          pygame.image.load("img/map/t106.PNG"),
          pygame.image.load("img/map/t107.PNG"),
          pygame.image.load("img/map/t108.PNG"),
          pygame.image.load("img/map/t109.PNG"),
          pygame.image.load("img/map/t110.PNG"),
          pygame.image.load("img/map/t111.PNG"),
          pygame.image.load("img/map/t112.PNG"),
          pygame.image.load("img/map/t113.PNG"),
          pygame.image.load("img/map/t114.PNG"),
          pygame.image.load("img/map/t115.PNG")]

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
              pygame.image.load("img/map/a64.PNG"),
              pygame.image.load("img/map/a65.PNG"),
              pygame.image.load("img/map/a66.PNG"),
              pygame.image.load("img/map/a67.PNG"),
              pygame.image.load("img/map/a68.PNG"),
              pygame.image.load("img/map/a69.PNG"),
              pygame.image.load("img/map/a70.PNG"),
              pygame.image.load("img/map/a71.PNG"),
              pygame.image.load("img/map/a72.PNG"),
              pygame.image.load("img/map/a73.PNG"),
              pygame.image.load("img/map/a74.PNG"),
              pygame.image.load("img/map/a75.PNG"),
              pygame.image.load("img/map/a76.PNG"),
              pygame.image.load("img/map/a77.PNG"),
              pygame.image.load("img/map/a78.PNG"),
              pygame.image.load("img/map/a79.PNG"),
              pygame.image.load("img/map/a80.PNG"),
              pygame.image.load("img/map/a81.PNG"),
              pygame.image.load("img/map/a82.PNG"),
              pygame.image.load("img/map/a83.PNG"),
              pygame.image.load("img/map/a84.PNG"),
              pygame.image.load("img/map/a85.PNG"),
              pygame.image.load("img/map/a86.PNG"),
              pygame.image.load("img/map/a87.PNG"),
              pygame.image.load("img/map/a88.PNG"),
              pygame.image.load("img/map/a89.PNG"),
              pygame.image.load("img/map/a90.PNG"),
              pygame.image.load("img/map/a91.PNG"),
              pygame.image.load("img/map/a92.PNG"),
              pygame.image.load("img/map/a93.PNG"),
              pygame.image.load("img/map/a94.PNG"),
              pygame.image.load("img/map/a95.PNG"),
              pygame.image.load("img/map/a96.PNG"),
              pygame.image.load("img/map/a97.PNG"),
              pygame.image.load("img/map/a98.PNG"),
              pygame.image.load("img/map/a99.PNG"),
              pygame.image.load("img/map/a100.PNG"),
              pygame.image.load("img/map/a101.PNG"),
              pygame.image.load("img/map/a102.PNG"),
              pygame.image.load("img/map/a103.PNG"),
              pygame.image.load("img/map/a104.PNG"),
              pygame.image.load("img/map/a105.PNG"),
              pygame.image.load("img/map/a106.PNG"),
              pygame.image.load("img/map/a107.PNG"),
              pygame.image.load("img/map/a108.PNG"),
              pygame.image.load("img/map/a109.PNG"),
              pygame.image.load("img/map/a110.PNG"),
              pygame.image.load("img/map/a111.PNG"),
              pygame.image.load("img/map/a112.PNG"),
              pygame.image.load("img/map/a113.PNG"),
              pygame.image.load("img/map/a114.PNG"),
              pygame.image.load("img/map/a115.PNG"),
              pygame.image.load("img/map/a116.PNG"),
              pygame.image.load("img/map/a117.PNG"),
              pygame.image.load("img/map/a118.PNG"),
              pygame.image.load("img/map/a119.PNG"),
              pygame.image.load("img/map/a120.PNG"),
              pygame.image.load("img/map/a121.PNG"),
              pygame.image.load("img/map/a122.PNG"),
              pygame.image.load("img/map/a123.PNG"),
              pygame.image.load("img/map/a124.PNG"),
              pygame.image.load("img/map/a125.PNG"),
              pygame.image.load("img/map/a126.PNG"),
              pygame.image.load("img/map/a127.PNG"),
              pygame.image.load("img/map/a128.PNG"),
              pygame.image.load("img/map/a129.PNG"),
              pygame.image.load("img/map/a130.PNG"),
              pygame.image.load("img/map/a131.PNG"),
              pygame.image.load("img/map/a132.PNG"),
              pygame.image.load("img/map/a133.PNG"),
              pygame.image.load("img/map/a134.PNG"),
              pygame.image.load("img/map/a135.PNG"),
              pygame.image.load("img/map/a136.PNG"),
              pygame.image.load("img/map/a137.PNG"),
              pygame.image.load("img/map/a138.PNG"),
              pygame.image.load("img/map/a139.PNG"),
              pygame.image.load("img/map/a140.PNG"),
              pygame.image.load("img/map/a141.PNG"),
              pygame.image.load("img/map/a142.PNG"),
              pygame.image.load("img/map/a143.PNG"),
              pygame.image.load("img/map/a144.PNG"),
              pygame.image.load("img/map/a145.PNG"),
              pygame.image.load("img/map/a146.PNG"),
              pygame.image.load("img/map/a147.PNG"),
              pygame.image.load("img/map/a148.PNG"),
              pygame.image.load("img/map/a149.PNG"),
              pygame.image.load("img/map/a150.PNG"),
              pygame.image.load("img/map/a151.PNG"),
              pygame.image.load("img/map/a152.PNG"),
              pygame.image.load("img/map/a153.PNG"),
              pygame.image.load("img/map/a154.PNG"),
              pygame.image.load("img/map/a155.PNG"),
              pygame.image.load("img/map/a156.PNG"),
              pygame.image.load("img/map/a157.PNG"),
              pygame.image.load("img/map/a158.PNG"),
              pygame.image.load("img/map/a159.PNG"),
              pygame.image.load("img/map/a160.PNG"),
              pygame.image.load("img/map/a161.PNG"),
              pygame.image.load("img/map/a162.PNG"),
              pygame.image.load("img/map/a163.PNG"),
              pygame.image.load("img/map/a164.PNG"),
              pygame.image.load("img/map/a165.PNG"),
              pygame.image.load("img/map/a166.PNG"),
              pygame.image.load("img/map/a167.PNG"),
              pygame.image.load("img/map/a168.PNG"),
              pygame.image.load("img/map/a169.PNG"),
              pygame.image.load("img/map/a170.PNG"),
              pygame.image.load("img/map/a171.PNG"),
              pygame.image.load("img/map/a172.PNG"),
              pygame.image.load("img/map/a173.PNG"),
              pygame.image.load("img/map/a174.PNG"),
              pygame.image.load("img/map/a175.PNG"),
              pygame.image.load("img/map/a176.PNG"),
              pygame.image.load("img/map/a177.PNG"),
              pygame.image.load("img/map/a178.PNG"),
              pygame.image.load("img/map/a179.PNG"),
              pygame.image.load("img/map/a180.PNG"),
              pygame.image.load("img/map/a181.PNG"),
              pygame.image.load("img/map/a182.PNG"),
              pygame.image.load("img/map/a183.PNG"),
              pygame.image.load("img/map/a184.PNG"),
              pygame.image.load("img/map/a185.PNG"),
              pygame.image.load("img/map/a186.PNG"),
              pygame.image.load("img/map/a187.PNG"),
              pygame.image.load("img/map/a188.PNG"),
              pygame.image.load("img/map/a189.PNG"),
              pygame.image.load("img/map/a190.PNG"),
              pygame.image.load("img/map/a191.PNG"),
              pygame.image.load("img/map/a192.PNG"),
              pygame.image.load("img/map/a193.PNG"),
              pygame.image.load("img/map/a194.PNG"),
              pygame.image.load("img/map/a195.PNG"),
              pygame.image.load("img/map/a196.PNG"),
              pygame.image.load("img/map/a197.PNG"),
              pygame.image.load("img/map/a198.PNG"),
              pygame.image.load("img/map/a199.PNG"),
              pygame.image.load("img/map/a200.PNG"),
              pygame.image.load("img/map/a201.PNG"),
              pygame.image.load("img/map/a202.PNG"),
              pygame.image.load("img/map/a203.PNG"),
              pygame.image.load("img/map/a204.PNG"),
              pygame.image.load("img/map/a205.PNG"),
              pygame.image.load("img/map/a206.PNG"),
              pygame.image.load("img/map/a207.PNG"),
              pygame.image.load("img/map/a208.PNG"),
              pygame.image.load("img/map/a209.PNG"),
              pygame.image.load("img/map/a210.PNG"),
              pygame.image.load("img/map/a211.PNG"),
              pygame.image.load("img/map/a212.PNG"),
              pygame.image.load("img/map/a213.PNG")]

mapNum = -1
mapNow = [[]]

posX: int = 0
posY: int = 0
dir: int = 0

#--------------------------------------------------
# Map Draw function
#--------------------------------------------------
def MapDraw(bg, x: int, y: int):
    x = x - 10
    y = y - 7
    selectIndex: int = 0

    # map draw
    bg.fill(idef.COLOR_BLACK)
    for j in range(15):
        if y + j < 0 or y + j >= len(mapNow):
           continue

        for i in range(21):
            if x + i < 0 or x + i >= len(mapNow[y+j]):
               continue

            selectIndex = mapNow[y+j][x+i]
            bg.blit(mapImg[selectIndex % MAP_IMG_ITEM], [32 * i - 16, 32 * j])
            selectIndex = int(selectIndex / MAP_IMG_ITEM)
            bg.blit(overMapImg[selectIndex % MAP_IMG_ITEM], [32 * i - 16, 32 * j])

    # character draw
    bg.blit(charImg,[idef.WINDOW_WIDTH/2 - 16, idef.WINDOW_HEIGHT/2 - 16])

#--------------------------------------------------
# Map Data Load function
#--------------------------------------------------
def MapLoad(_map: int):
    ret = [[]]
    ret.clear()

         #1,2,3は人
        #4は図書館の看板　　「このさき　かいそうちゅう　とおれません」　と　かいてある。
        #5　「じっけんきぐ　は　たいせつに　あつかおう」とかいてある。
        #6　「オートクレーブ」　と　かいてある……。もう　あっちへ　いこう。
        #7は70%エタノール　「7エタ」　と　かいてある。なんだか　いやな　かんじが　する。
        #8はあひる　かわいい　あひるが　ある。
        #9はイベントが起こらない、ただの物とかを通れなくする

    # map 
    if _map == 0:
        ret.append([9000030,9054030,9201030,9000030,90102030,9000000,9000000,9000000,9000030,9201030,9042030,9201030,9004030,9000030,9000000,9000000,9000000,9000000,9212030,9056030,90174030,9201030,9000030,5004030,9000030,9201030,9000030,9206030])
        ret.append([54,54,9073054,90112054,54,9000000,9000000,9000000,54,9072054,90210054,61054,54,54,9000000,9000000,9000000,9000000,213054,54,61054,54,2002054,54,54,54,6014054,9207054])
        ret.append([54,54,111054,113054,43054,9000000,9000000,9000000,54,111054,113054,54,1001054,54,9000000,9000000,9000000,9000000,54,9078054,9069054,54,9077054,9146054,54,9080054,7071054,54])
        ret.append([54,90144054,90146054,54,54,9000000,9000000,9000000,54,54,29054,54,90144054,90146054,9000000,9000000,9000000,9000000,9045054,111054,113054,54,111054,147054,54,111054,113054,9204054])
        ret.append([54,145054,147054,54,54,9000000,9000000,9000000,54,3003054,54,54,145054,147054,9000000,9000000,9000000,9000000,9041054,61054,43054,54,54,54,54,43054,54,205054])
        ret.append([54,29054,54,54,54,9000000,9000000,9000000,54,54,54,54,43054,54,9000000,9000000,000000,9000000,54,9073054,9208054,54,9144054,9146054,54,9077054,9211054,54])
        ret.append([9000000,9000000,9000000,54,9000000,9000000,9000000,9000000,9000000,9000000,54,9000000,9000000,9000000,9000000,9000000,9000000,9000000,54,111054,113054,54,145054,147054,54,111054,113054,9204054])
        ret.append([54,54,54,54,54,54,54,54,9048054,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,61054,205054])
        ret.append([54,54,54,54,54,54,54,54,54,54,54,32054,46054,54,54,54,54,54,54,54,54,54,54,54,54,54,54,9055054])
        ret.append([9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,64036,103036,63036,9000000,9000000,9000000,9000000,9000000,54,9079054,7071054,54,9080054,9209054,54,9076054,9112054,54])
        ret.append([0,0,0,0,0,0,0,0,0,9000000,36,36036,9000000,0,0,0,0,9000000,54,111054,113054,54,111054,113054,54,111054,113054,54])
        ret.append([0,0,0,0,0,0,0,0,0,9000000,60,59,9000000,0,0,0,0,9000000,54,54,54,54,54,54,54,54,43054,54])
        ret.append([0,0,0,0,0,0,0,0,0,9000000,9000000,9000000,9000000,0,0,0,0,9000000,9000000,9000000,9000000,9000000,9000000,9000000])

    elif _map == 1:
        ret.append([115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,9000107,9000109,9000109,9000109,9000109,9000111,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,51038,51038,51038,38,51038,38,51038,38,9000004,5,5,5,5,9000006,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,39,38,38])
        ret.append([38,38,39,39,127038,38,38,38,38,38,51038,38,38,38,51038,38,51038,38,9000004,5,5,5,5,9000006,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,38,38])
        ret.append([38,38,38,39,39,38,127038,38,38,38,51038,38,51038,38,51038,38,51038,38,9000004,5,5,5,5,9000006,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,38,38])
        ret.append([38,38,38,38,39,39,39,38,38,38,51038,51038,51038,38,51038,51038,51038,38,9000004,5,5,5,5,9000006,39,39,38,38,38,38,38,38,38,38,38,38,38,39,39,39,38,38,38,39,39,39,38,38])
        ret.append([38,38,38,38,38,127038,39,39,38,38,129038,129038,129038,129038,129038,129038,129038,129038,9000004,9000005,5,5,5,9000006,39,39,38,38,38,38,38,38,38,38,38,38,38,39,39,39,38,38,38,38,38,38,38,38])
        ret.append([38,38,98,9000061,9000063,98,38,39,39,39,39,39,39,39,39,39,39,39,7,9000008,8,8,8,9000009,39,39,38,38,38,38,38,38,38,38,38,38,38,39,39,43,9000107,9000109,9000109,9000109,9000109,9000109,9000111,38])
        ret.append([38,38,126038,9000062,9000064,127038,38,39,39,39,39,39,39,39,39,39,39,39,30,9000030,30,30,30,9000030,39,39,38,9000107,9000109,9000109,9000109,9000109,9000109,9000109,9000109,9000109,9000111,44,39,43,9000004,5,5,5,5,5,9000006,38])
        ret.append([38,38,38,38,98,38,39,39,38,38,129038,129038,129038,39,39,129038,90193038,129038,30,30,30,30,30,9000030,39,39,38,9000004,5,5,5,5,5,5,5,5,9000006,44,39,43,9000004,5,5,5,5,5,9000006,38])
        ret.append([38,9128038,38,38,38,9128038,39,39,38,38,38,38,38,39,39,38,9194038,38,9000030,9000030,9000030,9000030,9037030,9000030,39,39,38,9000007,8,8,8,8,8,8,8,8,9000009,44,39,43,9000007,8,8,8,8,8,9000009,38])
        ret.append([38,38,38,9128038,9130038,9132038,38,39,39,38,38,38,38,39,39,38,9028038,38,38,38,38,9039038,38038,38,39,39,38,9000031,31,31,31,31,31,31,31,31,9000031,44,39,43,9000018,17,16,17,16,17,9000019,38])
        ret.append([38,38,38,38,131038,133038,129038,39,39,39,38,38,38,39,39,38,38,38,38,38,9028038,38,38,38,39,39,38,9000031,9195031,195031,9000031,9000031,9000031,195031,196031,9000031,9000031,44,39,43,9000018,9000016,9000016,9000016,9000016,9000016,9000019,38])
        ret.append([38,38,38,38,38,38,38,38,39,39,39,38,38,39,39,38,38,9028038,38,38,38,38,38,38,39,39,38,9000031,9195031,9196031,9000031,9000031,9000031,9195031,9196031,9000031,9000031,44,39,43,9000018,9000017,9000016,9000017,9000016,9000017,9000019,38])
        ret.append([38,38,38,38,38,38,38,38,38,39,39,39,39,39,39,38,38,38,38,38,38,38,38,38,39,39,38,9000030,9000030,9000030,9000030,105,106,9000030,9000030,9000030,9000030,44,39,43,9000018,9000016,9000016,9000016,9000016,9000016,9000019,38])
        ret.append([38,38,9000107,9000109,9000109,9000109,9000109,9000109,9000109,9000110,9000110,9000110,9000112,39,39,39,39,39,39,39,39,39,39,39,39,39,38,38,9005038,38,9005038,38,38,9027038,38,9027038,38,39,39,43,9000018,9000016,9000016,20,9000016,9000016,9000019,38])
        ret.append([38,38,9000004,5,5,5,5,5,5,5,5,5,9000006,38,38,39,39,38,38,38,38,38,38,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,47,47,47,47,47,47,47,38])
        ret.append([38,38,9000007,8,8,8,8,8,8,8,8,8,9000009,38,38,39,39,38,38,38,9000107,9000109,9000109,9000109,9000111,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,38])
        ret.append([38,38,9000031,31,31,31,31,31,31,31,31,31,9000031,38,38,39,39,38,38,38,9000004,9000005,9000005,5,9000006,38,39,9000108,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000112,39,39,39,38])
        ret.append([38,38,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,38,38,39,39,38,38,38,9000004,9000005,9000005,9000005,9000006,38,38,9000004,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,9000006,38,38,38,38])
        ret.append([38,38,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,38,38,39,39,38,38,38,9000007,8,8,8,9000009,38,38,9000004,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,9000006,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,38,38,38,9000034,9000034,9000034,34,9000034,38,38,9000007,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9000009,38,38,38,38])
        ret.append([38,51038,38,51038,51038,51038,38,51038,51038,51038,38,51038,38,51038,38,39,39,38,38,38,9000034,34,34,34,9000034,38,38,9000031,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,9000031,38,38,38,38])
        ret.append([38,38,38,51038,38,38,38,51038,51038,38,38,51038,51038,51038,38,39,39,38,38,38,9000034,34,34,34,9000034,38,38,9000031,195031,196031,31,31,31,195031,9196031,9000031,9195031,9196031,31,31,31,9195031,9196031,9000031,38,38,38,38])
        ret.append([38,51038,38,51038,38,51038,38,51038,51038,38,38,51038,38,51038,38,39,39,38,38,38,9000034,34,34,34,9000034,38,38,9000031,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,9000031,38,38,38,38])
        ret.append([38,51038,38,51038,51038,51038,38,51038,51038,51038,38,51038,38,51038,38,39,39,38,38,38,9000034,9000034,9000034,9000034,9000034,38,38,9000031,9195031,9196031,9000031,9000031,9000031,9195031,9196031,9000031,9195031,9196031,9000031,9000031,9000031,9195031,9196031,9000031,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,38,38,38,9000034,9000034,106,9000034,9000034,38,38,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,105,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,9022038,38,9022038,38,38,38,38,38,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38])

    elif _map == 2:
        ret.append([9154100,9156100,9000000,0,0,0,0,0])   
        ret.append([155100,157100,9000000,9000000,0,0,0,0])
        ret.append([100,100,60,59,9000000,9000000,9000000,9000000])
        ret.append([100,100,100,100,100,100])
        ret.append([100,100,100,100,100,100])
        ret.append([100,100,100,100,178100,180100])
        ret.append([100,100,107100,109100,90179100,90181100])
       
    elif _map == 3:
        ret.append([9000030,9000030,9098030,9000030,9056030,9057030,9000000,0,0,0,0,0,0,0,0,0])
        ret.append([100,100,100,100,100,100])
        ret.append([9082100,9085100,9067100,9091100,9094100,100,9000000,0,0,0,0,0,0,0,0,0])
        ret.append([9083100,9086100,9099100,92100,95100,100,9000000,0,0,0,100,100,0,0,0,0])
        ret.append([84100,87100,90100,93100,96100,100,9000067,9000072,9000072,9000069,9081100,40191100,0,0,0,0])
        ret.append([100,100,100,100,100,100,9000071,75,75,9000074,100,192100,9000000,0,0,0])
        ret.append([90161100,90163100,9184100,100,100,9169100,90000071,75,75,9000074,100,100,9000000,0,0,0])
        ret.append([162100,164100,185100,100,175100,90170100,9000071,75,75,9000074,100,100,9000000,0,0,0])
        ret.append([90161100,90163100,100,100,176100,90171100,9000071,75,75,9000074,100,100,9000000,0,0,0])
        ret.append([162100,164100,61100,100,177100,90172100,9000068,9000073,9000073,9000070,100,100,9000000,9000000,9000000,9000000])
        ret.append([100,100,100,100,100,100,9000030,9000030,9000030,9000030,100,100,9000030,9102030,9174030,9000030])
        ret.append([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100])
        ret.append([9000067,9000072,9000072,9000069,100,100,100,100,100,100,100,100,100,9074100,100,100])
        ret.append([71,75,75,9000074,9037030,9054030,9000030,9097030,9000030,100,100,100,100,9075100,173100,100])
        ret.append([71,75,75,9000074,38100,39100,100,100,100,100,100,100,100,9068100,100,100])
        ret.append([71,75,75,9000074,100,100,100100,9104100,100,9166100,100,100,100,9065100,173100,100])
        ret.append([71,75,75,9000074,90167100,100,9104100,101100,100,9165100,100,100,100,90190100,100,100])
        ret.append([68,73,73,9000070,9000021,9000021,9000021,9000021,9000021,9000000,107100,109100,9000000,9000000,9000000,9000000])
        ret.append([68,73,73,9000070,9000000,9000000,9000000,9000000,9000000,9000000,0,0,9000000,9000000,9000000,9000000])

    elif _map == 4:
        ret.append([9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066])
        ret.append([100,100,100,100,100,100,100,100,100,100,100,100,100,100])
        ret.append([100,100,100,100,100,100,100,100,9134100,9136100,100,100,100,100])
        ret.append([9000000,9000000,9000000,9000000,175100,100,100,100,135100,137100])
        ret.append([0,0,0,9000000,176100,100,100,100,9104100,9104100])
        ret.append([0,0,0,9000000,176100,100,100,100,9140100,9141100])
        ret.append([0,0,0,9000000,177100,100,100,100,142100,143100])
        ret.append([0,0,9000000,9000000,9000000,9000000,100,100,9000000,9000000,9000000])
        ret.append([0,0,0,0,0,9000000,107100,109100,9000000,0,0])
        ret.append([0,0,0,0,0,9000000,0,0,9000000,0,0])
        

    elif _map == 5:
        ret.append([9000021,101,102,9000021,9000030,9042030,9000103,9000030,104,9000030])
        ret.append([100100,107100,109100,100,100,100,100,100,100,100])
        ret.append([9104100,9104100,100,100,100,100,100,100,158100,100])
        ret.append([101100,100,100,100,100,100,100,100,159100,160100])
        ret.append([100,100,100,100,100,100,100,100,100,100])

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
# Move check function
#--------------------------------------------------
def MoveCheck(x: int, y: int):
    if y < 0 or len(mapNow) <= y:
        return 1
    elif x < 0 or len(mapNow[y]) <= x:
        return 1
    elif int(mapNow[y][x] / (MAP_IMG_ITEM*MAP_IMG_ITEM)) == 0:
       return 0
    else:
       return 1

#--------------------------------------------------
# Map Main function
#--------------------------------------------------
def MapMain(bg, clk):
    # enable change global value
    global posX, posY
    global mapNow
    global mapNum

    # local value
    timer: int = 0
    scene: int = 0
    keySelectFlag: int = 0
    key: int = 0

    # font set
    font = pygame.font.Font(idef.FONT_FILE_PATH, 20)
    
    # key input setup
    pygame.key.set_repeat(1,1)

    mapNum = 1
    mapNow = MapLoad(mapNum)
    
    while True:
        key = 0

        # event process
        for event in pygame.event.get():
            # program exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # key down event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.locals.K_UP:
                    key = key | KEY_UP
                elif event.key == pygame.locals.K_DOWN:
                    key = key | KEY_DOWN
                elif event.key == pygame.locals.K_LEFT:
                    key = key | KEY_LEFT
                elif event.key == pygame.locals.K_RIGHT:
                    key = key | KEY_RIGHT
                
                if event.key == pygame.locals.K_SPACE:
                    key = key | KEY_SELECT

                # 連射後のご入力防止
                pygame.event.clear()

        # game state update
        # key = pygame.key.get_pressed()
        timer = timer + 1
        bg.fill(idef.COLOR_WHITE)
        
        # 上キー入力
        if key & KEY_UP == KEY_UP:
            #if pygame.mixer.get_busy() == False:
                #print("up")
                if MoveCheck(posX, posY - 1) == 0:
                    posY = posY - 1
                CharDraw(bg, DIR_U)
                #soundWalk.play()

        # 下キー入力
        if key & KEY_DOWN == KEY_DOWN:
          #if pygame.mixer.get_busy() == False:
                #print("down")
                if MoveCheck(posX, posY + 1) == 0:
                    posY = posY + 1
                CharDraw(bg, DIR_D)
                #soundWalk.play()

        # 左キー入力
        if key & KEY_LEFT == KEY_LEFT:
            #if pygame.mixer.get_busy() == False:
                #print("left")
                if MoveCheck(posX - 1, posY) == 0:
                    posX = posX - 1
                CharDraw(bg, DIR_L)
                #soundWalk.play()
        
        # 右キー入力
        if key & KEY_RIGHT == KEY_RIGHT:
            #if pygame.mixer.get_busy() == False:
                #print("right")
                if MoveCheck(posX + 1, posY) == 0:
                    posX = posX + 1
                CharDraw(bg, DIR_R)
                #soundWalk.play()
        
        # map移動実施
        if key & KEY_MOVE > 0:
            # 座標表示
            print(str(posX) + ", " + str(posY))
            
            # 座標イベント（マップ移動など）
            

            if mapNum == 1:
                if posX == 18 and posY == 7:
                    mapNum = 2
                    posX = 5
                    posY = 5
                    mapNow = MapLoad(mapNum) 
                

            if mapNum == 1:
                if posX == 18 and posY == 8:
                    mapNum = 2
                    posX = 5
                    posY = 5
                    mapNow = MapLoad(mapNum) 


            if mapNum == 2:
                if posX == 5 and posY == 5:
                    mapNum = 1
                    posX = 17
                    posY = 7
                    mapNow = MapLoad(mapNum) 
                

            if mapNum == 2:
                if posX == 5 and posY == 5:
                    mapNum = 1
                    posX = 17
                    posY = 8
                    mapNow = MapLoad(mapNum) 



                     #図書館

            if mapNum == 1:
                if posX == 31 and posY == 14:
                    mapNum = 3
                    posX = 10
                    posY = 17
                    mapNow = MapLoad(mapNum) 
                

            if mapNum == 1:
                if posX == 32 and posY == 14:
                    mapNum = 3
                    posX = 11
                    posY = 17
                    mapNow = MapLoad(mapNum) 


                    
            if mapNum == 3:
                if posX == 11 and posY == 18:
                    mapNum = 1
                    posX = 32
                    posY = 15
                    mapNow = MapLoad(mapNum) 
                
            if mapNum == 3:
                if posX == 10 and posY == 18:
                    mapNum = 1
                    posX = 31
                    posY = 15
                    mapNow = MapLoad(mapNum) 


                    #2号館

            if mapNum == 1:
                if posX == 35 and posY == 26:
                    mapNum = 4
                    posX = 7
                    posY = 8
                    mapNow = MapLoad(mapNum) 


            if mapNum == 4:
                if posX == 7 and posY == 9:
                    mapNum = 1
                    posX = 35
                    posY = 27
                    mapNow = MapLoad(mapNum) 

            if mapNum == 4:
                if posX == 6 and posY == 9:
                    mapNum = 1
                    posX = 35
                    posY = 27
                    mapNow = MapLoad(mapNum) 

                    #総研棟

            if mapNum == 1:
                if posX == 22 and posY == 26:
                    mapNum = 5
                    posX = 2
                    posY = 1
                    mapNow = MapLoad(mapNum) 


            if mapNum == 5:
                if posX == 2 and posY == 0:
                    mapNum = 1
                    posX = 22
                    posY = 27
                    mapNow = MapLoad(mapNum) 
            
            if mapNum == 5:
                if posX == 1 and posY == 0:
                    mapNum = 1
                    posX = 22
                    posY = 27
                    mapNow = MapLoad(mapNum) 



        # 決定キー入力
        if key & KEY_SELECT == KEY_SELECT:
            if keySelectFlag == 0:
                keySelectFlag = 1
                print("select push")
        else:
            keySelectFlag = 0

        MapDraw(bg, posX, posY)
        pygame.display.update()
        clk.tick(33)

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------