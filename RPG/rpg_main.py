'''
Project Name : iGemGunmaGameProject
File Name    : rpg_main.py
Description  : メインファイル
'''

#----------------------------
# import
#----------------------------
import os
import sys
import pygame
import pygame.locals
import random

#----------------------------
# main program
#----------------------------
def main():
    # debug mode select
    DEBUG_MODE: int = 2
    
    # pygame init
    pygame.init()

    # game system import
    import rpg_define as idef
    import rpg_battle as ibattle
    import rpg_map as imap
    import rpg_staffroll as istaff

    # window init
    pygame.display.set_caption(idef.WINDOW_NAME);
    screen = pygame.display.set_mode(idef.WINDOW_SIZE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,80)
    tmr: int = 0
    
    if DEBUG_MODE == 1:
        print("debug battle")
        user = idef.player()
        user.Name = "まどか"
        user.Command.append("プラスミド1")
        user.Command.append("プラスミド2")
        user.Command.append("プラスミド3")
        ibattle.BattleMain(screen, clock, user, 5)
        
    elif DEBUG_MODE == 2:
        print('debug map')
        imap.MapMain(screen, clock)

    elif DEBUG_MODE == 3:
        print("staff roll check")
        istaff.StaffrollMain(screen, clock)

    scene: int = 0
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


# メインプログラム実行
if __name__  == '__main__':
    main()

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------