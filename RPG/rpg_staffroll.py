'''
Project Name : iGemGunmaGameProject
File Name    : rpg_staffroll.py
Description  : スタッフロールファイル
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

#----------------------------
# constant value
#----------------------------
ROLL_FONT_SIZE: int = 20

#--------------------------------------------------
# battle main function
#--------------------------------------------------
def StaffrollMain(bg, clk):
    # font set 
    font = pygame.font.Font(idef.FONT_FILE_PATH, ROLL_FONT_SIZE)

    # timer
    timer = 0

    # staff roll set
    roll = ["STAFF"]
    roll.append("")
    roll.append("SCENARIO")
    roll.append("    Tomo Kanzaki")
    roll.append("")
    roll.append("CHARACTER DESIGN")
    roll.append("    Tomo Kanzaki")
    roll.append("")
    roll.append("MAP DESIGN")
    roll.append("    Tomo Kanzaki")
    roll.append("")
    roll.append("MAP EDITOR")
    roll.append("    Mizuki Kita")
    roll.append("")
    roll.append("MAP SYSTEM")
    roll.append("    Mizuki Kita")
    roll.append("    Koshiro Miyauchi")
    roll.append("")
    roll.append("BATTLE SYSTEM")
    roll.append("    Koshiro Miyauchi")
    roll.append("")
    roll.append("BATTLE DESING")
    roll.append("    Koshiro Miyauchi")
    roll.append("")
    roll.append("PROGRAMMER")
    roll.append("    Koshiro Miyauchi")
    roll.append("    Mizuki Kita")
    roll.append("    Madoka Nakai")
    roll.append("")
    roll.append("SOUND")
    roll.append("    Tomo Kanzaki")
    roll.append("")
    roll.append("SPECIAL THANKS")
    roll.append("    Datsukan")
    roll.append("    Kazuko Kawamura")
    roll.append("    ShiganaiDaigakuinsei")
    roll.append("    Nami Harada")
    roll.append("    Tsubaty")
    roll.append("    Ryu Watanabe")
    roll.append("    Andy Minamishima")
    roll.append("    Secretary General of Gunma University in Showa")
    roll.append("    k-kubota")
    roll.append("    Cherry Berry")
    roll.append("    Keiichi Yamada")
    roll.append("    Junko Kanou")
    roll.append("    Yusuke Shoji")
    roll.append("    Kei Nishioka")
    roll.append("    Yuya_Wako")
    roll.append("    herikoputan")
    roll.append("    mi")
    roll.append("    Kazuya Masuda")
    roll.append("    Yasuki Ishizaki")
    roll.append("    Tamami Fujima")
    roll.append("    Hideyuki Onodera")
    roll.append("    Yumishonshon")
    roll.append("    Ikuko Suzuki")
    roll.append("    rintaro")
    roll.append("    Hikaru Goto")
    roll.append("    ebara")
    roll.append("    yama")
    roll.append("    Shinichi Yoshihiro")
    roll.append("    Goro Hangai")
    roll.append("    Hirosh Takahashi")
    roll.append("    Sumiko")
    roll.append("    Gunma University")
    roll.append("")
    roll.append("DIRECTOR")
    roll.append("    Mizuki Kita")
    roll.append("    Koshiro Miyauchi")
    roll.append("")
    roll.append("iGEM Gunma Project Leader (2019)")
    roll.append("    Mizuki Kita")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("iGEM Gunma")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bg.fill(idef.COLOR_BLACK)
        for i in range(len(roll)):
            posY = idef.WINDOW_HEIGHT - timer + i*30
            if posY < -30 or posY > idef.WINDOW_HEIGHT:
                continue
            idef.TextDraw(bg, roll[i], 50, posY, font, idef.COLOR_WHITE)
        timer = timer + 5
        if timer > (len(roll)+8)*30:
            timer = (len(roll)+8)*30
        pygame.display.update()
        clk.tick(20)
        
#--------------------------------------------------
# end of file
#--------------------------------------------------
