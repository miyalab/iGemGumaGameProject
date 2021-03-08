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
          pygame.image.load("img/map/t106.PNG")]

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
              pygame.image.load("img/map/a196.PNG")]
nowMap = [[]]

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
        if y + j < 0 or y + j >= len(nowMap):
           continue

        for i in range(21):
            if x + i < 0 or x + i >= len(nowMap[y+j]):
               continue
            
            #print(str(len(nowMap[y+j])) + "," + str(len(nowMap)) + "," + str(x+i) + "," + str(y+j) + "," + str(nowMap[y+j][x+i]))
            selectIndex = nowMap[y+j][x+i]
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

    # map 
    if _map == 0:
        ret.append([30,54030,11030,30,12030,0,0,0,102030,11030,42030,13030,4030,30,0])
        ret.append([54,54,9073054,90112054,54,0,0,0,54,54,54,61054,54,54,0])
        ret.append([54,54,113054,111054,43054,0,0,0,54,9072054,90112054,54,1001054,54,0])
        ret.append([54,90144054,90146054,54,54,0,0,0,54,111054,113054,20054,54,3003054,0])
        ret.append([54,145054,147054,54,54,0,0,0,54,54,54,54,90144054,90146054,0,0,0,0,30,56030,174030,30,90150030,90151030])
        ret.append([54,29054,54,54,54,0,0,0,54,54,54,54,145054,147054,0,0,0,0,54,9041054,2002054,54,152054,153054])
        ret.append([0,0,0,54,0,0,0,0,0,0,54,0,0,0,0,0,0,0,9045054,78054,69054,54,77054,71054])
        ret.append([54,54,54,54,54,54,54,54,9048054,54,54,54,54,54,54,54,54,54,54,111054,113054,54,111054,113054])
        ret.append([54,54,54,54,54,54,54,54,54,54,54,32054,46054,54,54,54,54,54,54,54,54,54,61054,9055054])
        ret.append([0,0,0,0,0,0,0,0,0,0,64036,103036,63036,0,0,0,0,0,54,79054,71054,54,80054,66054])
        ret.append([0,0,0,0,0,0,0,0,0,0,36,36036,0,0,0,0,0,0,54,90111054,90113054,54,90111054,90113054])
        ret.append([0,0,0,0,0,0,0,0,0,0,60,59,0,0,0,0,0,0,0,0,0,0,0,0])

    elif _map == 1:

        ret.append([58,58,58,57,58,58,58,57,58,58,58,57,58,58,58,57,58,58,1,2,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,4,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        ret.append([38,38,39,39,127038,38,38,38,38,38,38,38,38,38,38,38,38,38,4,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        ret.append([38,38,38,39,39,38,127038,38,38,38,38,38,38,38,38,38,38,38,4,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        ret.append([38,38,38,38,39,39,39,38,38,38,38,38,38,38,38,38,38,38,4,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        ret.append([38,38,38,38,38,127038,39,39,38,38,129038,129038,129038,129038,129038,129038,129038,129038,4,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        ret.append([38,38,98,61,63,98,38,39,39,39,39,39,39,39,39,39,39,39,7,8,8,8,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,3])
        ret.append([38,38,126038,62,64,127038,38,39,39,39,39,39,39,39,39,39,39,39,30,30,30,30,30,30,39,39,38,1,2,2,2,2,2,2,2,2,3,0,0,0,4,5,5,5,5,5,6])
        ret.append([38,38,38,38,98,38,39,39,38,38,129038,129038,129038,39,39,129038,90193038,129038,30,30,30,30,30,30,39,39,38,4,5,5,5,5,5,5,5,5,6,0,0,0,4,5,5,5,5,5,6])
        ret.append([38,128038,38,38,38,128038,39,39,38,38,38,38,38,39,39,38,90194038,38,30,30,30,30,9037030,30,39,39,38,7,8,8,8,8,8,8,8,8,9,0,0,0,7,8,8,8,8,8,9])
        ret.append([38,38,38,9028038,90130038,90132038,38,39,39,38,38,38,38,39,39,38,9028038,38,38,38,38,9039038,38038,38,39,39,38,31,31,31,31,31,31,31,31,31,31,44,39,43,16,17,16,17,16,17,19])
        ret.append([38,38,38,38,131038,133038,129038,39,39,39,38,38,38,39,39,38,38,38,38,38,9028038,38,38,38,39,39,38,31,195031,195031,31,31,31,195031,196031,31,31,44,39,43,18,16,16,16,16,16,19])
        ret.append([38,38,38,38,38,38,38,38,39,39,39,38,38,39,39,38,38,9028038,38,38,38,38,38,38,39,39,38,31,195031,196031,31,31,31,195031,196031,31,31,44,39,43,18,17,16,17,16,17,19])
        ret.append([38,38,38,38,38,38,38,38,38,39,39,39,39,39,39,38,38,38,38,38,38,38,38,38,39,39,38,30,30,30,30,105,106,30,30,30,30,44,39,43,18,16,16,16,16,16,19])
        ret.append([38,38,1,2,2,2,2,2,2,2,2,2,3,38,39,39,39,39,39,39,39,39,39,39,39,39,38,38,38,38,38,38,38,27038,38,27038,38,39,39,43,18,16,16,20,16,16,19])
        ret.append([38,38,4,5,5,5,5,5,5,5,5,5,6,38,38,39,39,38,38,38,38,38,38,38,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,47,47,47,47,47,47,47])
        ret.append([38,38,7,8,8,8,8,8,8,8,8,8,9,38,38,39,39,38,38,38,1,2,2,2,3,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39])
        ret.append([38,38,31,31,31,31,31,31,31,31,31,31,31,38,38,39,39,38,38,38,4,5,5,5,6,39,39,1,2,2,2,2,2,2,3,39,39,39,39,39,39,39,39])
        ret.append([38,38,31,31,31,31,31,31,31,31,31,31,31,38,38,39,39,38,38,38,4,5,5,5,6,38,38,4,5,5,5,5,5,5,6,38,38,38,38,38,38,38,38])
        ret.append([38,38,31,31,31,31,31,31,31,31,31,31,31,38,38,39,39,38,38,38,7,8,8,8,9,38,38,4,5,5,5,5,5,5,6,38,38,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,38,38,38,34,34,34,34,34,38,38,7,8,8,8,8,8,8,9,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,39,39,38,38,34,34,34,34,34,38,38,31,31,31,31,31,31,31,31,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,39,39,38,38,34,34,34,34,34,38,38,31,195031,196031,31,31,31,195031,196031,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,39,39,38,38,34,34,34,34,34,38,38,31,31,31,31,31,31,31,31,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,39,39,38,38,34,34,34,34,34,38,38,31,195031,196031,31,31,31,195031,196031,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,39,39,38,38,34,34,34,34,34,38,38,31,31,31,105,106,31,31,31,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38])



    elif _map == 2:
        ret.append([154100,156100,0,0,0,0,0,0])     #ここに最初あらわれて動けなくなるからいったん９外しとく
        ret.append([90155100,90157100,0,0,0,0,0,0])
        ret.append([100,100,60,59,0,0,0,0])
        ret.append([100,100,100,100,100,100])
        ret.append([100,100,100,100,100,100])
        ret.append([100,100,100,100,178100,180100])
        ret.append([100,100,107100,109100,90179100,90181100])
       
    elif _map == 3:
        ret.append([30,30,98030,30,56030,57030,0,0,0,0,0,0,0,0,0,0])
        ret.append([9082100,9085100,9067100,9091100,9094100,100,0,0,0,0,0,0,0,0,0,0])
        ret.append([9083100,9086100,9099100,92100,95100,100,0,0,0,0,100,100,0,0,0,0])
        ret.append([84100,87100,90100,93100,96100,100,67,72,72,69,9081100,90191100,0,0,0,0])
        ret.append([100,100,100,100,100,100,71,75,75,74,100,90192100,0,0,0,0])
        ret.append([100,90161100,90163100,100,100,169100,71,75,75,74,100,100,0,0,0,0])
        ret.append([100,90162100,90164100,100,90175100,90170100,71,75,75,74,100,100,0,0,0,0])
        ret.append([100,90161100,90163100,100,90176100,90171100,71,75,75,74,100,100,0,0,0,0])
        ret.append([90167100,90162100,90164100,100,90177100,90172100,68,73,73,70,100,100,0,0,0,0])
        ret.append([90168100,100,100,100,100,100,30,30,30,30,100,100,30,90102030,174030,30])
        ret.append([0,67,72,69,100,100,100,100,100,100,100,100,100,9074100,100,100])
        ret.append([0,71,75,74,30,54030,30,97030,30,100,100,100,100,9075100,173100,100])
        ret.append([0,71,75,74,100,100,100,100,100,100,100,100,100,9068100,100,100])
        ret.append([0,71,75,74,100,100,100,100,100,9166100,100,100,100,9065100,173100,100])
        ret.append([0,71,75,74,100,100,100,100,100,9165100,100,100,100,90190100,100,100])
        ret.append([0,68,73,70,21,21,21,21,21,0,107100,109100,0,0,0,0])

    elif _map == 4:
        ret.append([66,66,66,66,66,66,101,102,66,66,66,66,66,66])
        ret.append([100,100,100,100,100,100,100,100,100,100,100,100,100,100])
        ret.append([100,100,100,100,100,100,100,100,9134100,9136100,100,100,100,100])
        ret.append([0,0,0,0,175100,100,100,100,135100,137100])
        ret.append([0,0,0,0,176100,100,100,100,9104100,9104100])
        ret.append([0,0,0,0,176100,100,100,100,9140100,9141100])
        ret.append([0,0,0,0,177100,100,100,100,142100,143100])
        ret.append([0,0,0,0,0,0,100,100,0,0,0])
        ret.append([0,0,0,0,0,0,107100,109100,0,0,0])
        

    elif _map == 5:
        ret.append([21,101,102,21,30,42030,103,30,104,30])
        ret.append([100100,107100,109100,100,100,100,100,100,100,100])
        ret.append([9104100,9104100,100,100,100,100,100,100,158100,100])
        ret.append([101100,100,100,100,100,100,100,100,159100,160100])
        ret.append([100,100,100,100,100,100,100,100,100,100])

        #イベントが起こらない、ただの物とかは9で通れなくする

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
    if y < 0 or len(nowMap) <= y:
        return 1
    elif x < 0 or len(nowMap[y]) <= x:
        return 1
    elif int(nowMap[y][x] / (MAP_IMG_ITEM*MAP_IMG_ITEM)) == 0:
       return 0
    else:
       return 1

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
    pygame.key.set_repeat(1,1)

    nowMap = MapLoad(0)
    
    while True:
        KEY = 0

        # event process
        for event in pygame.event.get():
            # program exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # key down event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.locals.K_UP:
                    KEY = 1
                elif event.key == pygame.locals.K_DOWN:
                    KEY = 2
                elif event.key == pygame.locals.K_LEFT:
                    KEY = 3
                elif event.key == pygame.locals.K_RIGHT:
                    KEY = 4
                
                # 連射後のご入力防止
                pygame.event.clear()

        # game state update
        # key = pygame.key.get_pressed()
        timer = timer + 1
        bg.fill(idef.COLOR_WHITE)
        
        # 上キー入力
        if KEY == 1:
            #if pygame.mixer.get_busy() == False:
                #print("up")
                if MoveCheck(posX, posY - 1) == 0:
                    posY = posY - 1
                CharDraw(bg, DIR_U)
                print(str(posX) + ", " + str(posY))
                #soundWalk.play()

        # 下キー入力
        if KEY == 2:
          #if pygame.mixer.get_busy() == False:
                #print("down")
                if MoveCheck(posX, posY + 1) == 0:
                    posY = posY + 1
                CharDraw(bg, DIR_D)
                print(str(posX) + ", " + str(posY))
                #soundWalk.play()

        # 左キー入力
        if KEY == 3:
            #if pygame.mixer.get_busy() == False:
                #print("left")
                if MoveCheck(posX - 1, posY) == 0:
                    posX = posX - 1
                CharDraw(bg, DIR_L)
                print(str(posX) + ", " + str(posY))
                #soundWalk.play()
        
        # 右キー入力
        if KEY == 4:
            #if pygame.mixer.get_busy() == False:
                #print("right")
                if MoveCheck(posX + 1, posY) == 0:
                    posX = posX + 1
                CharDraw(bg, DIR_R)
                print(str(posX) + ", " + str(posY))
                #soundWalk.play()
        
        MapDraw(bg, posX, posY)
        pygame.display.update()
        clk.tick(20)

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------