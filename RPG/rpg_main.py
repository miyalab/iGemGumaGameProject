#
# Project Name : iGemGunmaGameProject
# File Name    : rpg_main.py
# Description  : メインファイル
#

# import
import pygame 
import sys
import rpg_define as idef
import rpg_battle as ibattle
import rpg_map as imap

# メインプログラム
def main():
    pygame.init()
    pygame.display.set_caption(idef.const.WINDOW_NAME);
    screen = pygame.display.set_mode(idef.const.WINDOW_SIZE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,80)
    tmr = 0

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