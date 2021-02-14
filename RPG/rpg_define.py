'''
Project Name : iGemGunmaGameProject
File Name    : rpg_define.py
Description  : 定数定義ファイル
'''

# import
import const
import pygame 
from pygame.locals import *

# ウインドウ関連
WINDOW_WIDTH: tuple = 640
WINDOW_HEIGHT: tuple = 480
WINDOW_SIZE: tuple = (WINDOW_WIDTH,WINDOW_HEIGHT)
WINDOW_NAME: str = 'iGEM RPG GAME'

# 色定義
COLOR_BLACK: tuple = (0,0,0)
COLOR_WHITE: tuple = (255,255,255)
COLOR_RED: tuple = (255,0,0)
COLOR_GREEN: tuple = (0,255,0)
COLOR_BLUE: tuple = (0,0,255)

# 画像ファイルパス


# 進行イベント定義
EVENT_OPENING: int = 1

# playerクラス
class player():
    Name: str = "name"
    HP: int = 0
    MaxHP: int = 0
    MP: int = 0
    MaxMP: int = 0
    LV: int = 0
    ATK: int = 0
    DEF: int = 0
    INT: int = 0
    AGI: int = 0
    LUK: int = 0
    EXP: int = 0



#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------