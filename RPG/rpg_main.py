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
    DEBUG_MODE: int = 1
    
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
        ibattle.BattleMain(screen, clock, user, 1)
        
    elif DEBUG_MODE == 2:
        print('debug map')
        imap.MapMain(screen, clock)

    elif DEBUG_MODE == 3:
        print("staff roll check")
        istaff.StaffrollMain(screen, clock)

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        txt = font.render(str(tmr), True, idef.COLOR_WHITE)
        
        screen.fill(idef.COLOR_BLACK)
        screen.blit(txt, [idef.WINDOW_WIDTH/2,idef.WINDOW_HEIGHT/2])
        
        pygame.display.update()
        clock.tick(10)


# メインプログラム実行
if __name__  == '__main__':
    main()

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------