'''
Project Name : iGemGunmaGameProject
File Name    : rpg_main.py
Description  : メインファイル
'''

# import
import sys
import pygame 
import rpg_define as idef
import rpg_battle as ibattle
import rpg_map as imap


# メインプログラム
def main():
    # debug mode select
    DEBUG_MODE = 0

    # pygame and window init
    pygame.init()
    pygame.display.set_caption(idef.const.WINDOW_NAME);
    screen = pygame.display.set_mode(idef.const.WINDOW_SIZE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,80)
    
    tmr = 0
    if DEBUG_MODE == 1:
        print('Debug battle')
        while True:
            tmr = tmr + 1
        
    elif DEBUG_MODE == 2:
        print('Debug map')
        while True:
           tmr = tmr + 1

    else:
        while True:
            tmr = tmr + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            txt = font.render(str(tmr), True, idef.const.COLOR_WHITE)

            screen.fill(idef.const.COLOR_BLACK)
            screen.blit(txt, [300,200])
            pygame.display.update()
            clock.tick(10)


# メインプログラム実行
if __name__  == '__main__':
    main()

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------