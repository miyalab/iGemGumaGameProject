'''
Project Name : iGemGunmaGameProject
File Name    : rpg_define.py
Description  : 定数定義ファイル
'''

#----------------------------
# import
#----------------------------
import const
import pygame 

#----------------------------
# window
#----------------------------
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE: tuple = (WINDOW_WIDTH,WINDOW_HEIGHT)
WINDOW_NAME: str = 'iGEM RPG GAME'

#----------------------------
# color
#----------------------------
COLOR_BLACK: tuple = (0,0,0)
COLOR_WHITE: tuple = (255,255,255)
COLOR_RED: tuple = (255,0,0)
COLOR_GREEN: tuple = (0,255,0)
COLOR_BLUE: tuple = (0,0,255)

#----------------------------
# file path
#----------------------------
FONT_FILE_PATH = "ipaexg.ttf"

#----------------------------
# event define 
#----------------------------
EVENT_OPENING: int = 1

class GameSetting():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(idef.WINDOW_NAME);
        screen = pygame.display.set_mode(idef.WINDOW_SIZE)
        clock = pygame.time.Clock()

#----------------------------
# player class
#----------------------------
class player():
    Name: str = "name"
    HP: int = 500
    MaxHP: int = 500
    MP: int = 100
    MaxMP: int = 100
    LV: int = 10
    ATK: int = 150
    DEF: int = 50
    INT: int = 10
    AGI: int = 10
    LUK: int = 10
    EXP: int = 10
    Command = ["攻撃"]

#----------------------------
# enemy class
#----------------------------
class enemy():
    def __init__(self):
        Num: int = 0
        ImgPath = "path"
        Name: str = "name"
        HP: int = 1000
        MaxHP: int = 1000
        MP: int = 0
        MaxMP: int = 0
        LV: int = 0
        ATK: int = 1000
        DEF: int = 1000
        INT: int = 0
        AGI: int = 0
        LUK: int = 0
        EXP: int = 0

#--------------------------------------------------
# text draw function
#--------------------------------------------------
def TextDraw(bg, txt, x, y, fnt, col):
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------