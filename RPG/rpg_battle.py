'''
Project Name : iGemGunmaGameProject
File Name    : rpg_battle.py
Description  : バトルプログラムファイル
'''

# import
import rpg_define as idef
import pygame
import sys
import random
from pygame.locals import *

imgBtlBG = pygame.image.load("img/battle/background/btlbg0.png")
imgEffect = pygame.image.load("img/battle/effect/effect_attack.png")
imgEnemy = pygame.image.load("img/battle/enemy/enemy4.png")
emy_x = idef.WINDOW_WIDTH/2-imgEnemy.get_width()/2
emy_y = idef.WINDOW_HEIGHT/2-imgEnemy.get_height()
emy_step = 0
emy_blink = 0
dmg_eff = 0
COMMAND = ["[A]ttack", "[P]otion", "[B]laze gem", "[R]un"]
message = [""]*10

def init_battle():
    global imgEnemy, emy_num, emy_x, emy_y
    emy_num = emy_num + 1
    if emy_num == 5:
        emy_num = 1
    imgEnemy = pygame.image.load("img/battle/enemy/enemy"+str(emy_num)+".png")
    emy_x = 440-imgEnemy.get_width()/2
    emy_y = 560-imgEnemy.get_height()

def draw_battle(bg, fnt):
    bg.blit(imgBtlBG, [0, 0])
    bg.blit(imgEnemy, [emy_x, emy_y])
    sur = fnt.render("img/battle/enemy/enemy"+str(emy_num)+".png", True, idef.COLOR_WHITE)
    bg.blit(sur, [360, 580])

def init_message():
    for i in range(10):
        message[i] = ""

def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(9):
        message[i] = message[i+1]
    message[9] = msg

def draw_text(bg, txt, x, y, fnt, col):
    sur = fnt.render(txt, True, idef.COLOR_BLACK)
    bg.blit(sur, [x+1, y+2])
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])

def draw_battle(bg, fnt):
    global emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    bg.blit(imgBtlBG, [bx, by])
    if emy_blink%2 == 0:
        bg.blit(imgEnemy, [emy_x, emy_y+emy_step])
    if emy_blink > 0:
        emy_blink = emy_blink - 1
    for i in range(10):
        draw_text(bg, message[i], 450, 50+i*30, fnt, idef.COLOR_WHITE)

def battle_command(bg, fnt):
    for i in range(4):
        draw_text(bg, COMMAND[i], 20, 120+30*i, fnt, idef.COLOR_WHITE)

def battle_main():
    global emy_step, emy_blink, dmg_eff
    idx = 10
    tmr = 0

    pygame.init()
    pygame.display.set_caption("ターン制の処理")
    screen = pygame.display.set_mode(idef.WINDOW_SIZE)
    clock = pygame.time.Clock()
    command_font = pygame.font.Font(None, 30)
    message_font = pygame.font.Font(None, 25)

    init_message()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        draw_battle(screen, message_font)
        tmr = tmr + 1
        key = pygame.key.get_pressed()

        if idx == 10: # 戦闘開始
            if tmr == 1: set_message("Encounter!")
            if tmr == 6:
                idx = 11
                tmr = 0

        elif idx == 11: # プレイヤー入力待ち
            if tmr == 1: set_message("Your turn.")
            battle_command(screen, command_font)

            # key入力分岐
            if key[K_a] == 1 or key[K_SPACE] == 1:
                idx = 12
                tmr = 0

        elif idx == 12: # プレイヤーの攻撃
            if tmr == 1: set_message("You attack!")
            if 2 <= tmr and tmr <= 4:
                screen.blit(imgEffect, [400-tmr*60, -100+tmr*60])
            if tmr == 5:
                emy_blink = 5
                set_message("***pts of damage!")
            if tmr == 16:
                idx = 13
                tmr = 0

        elif idx == 13: # 敵のターン、敵の攻撃
            if tmr == 1: set_message("Enemy turn.")
            if tmr == 5:
                set_message("Enemy attack!")
                emy_step = 30
            if tmr == 9:
                set_message("***pts of damage!")
                dmg_eff = 5
                emy_step = 0
            if tmr == 20:
                idx = 11
                tmr = 0

        pygame.display.update()
        clock.tick(5)