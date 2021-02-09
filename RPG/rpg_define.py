'''
Project Name : iGemGunmaGameProject
File Name    : rpg_define.py
Description  : 定数定義ファイル
'''

# import
import pygame
import const

# ウインドウ関連
const.WINDOW_SIZE = (640,480)
const.WINDOW_NAME = 'iGEM RPG GAME'

# 色定義
const.COLOR_BLACK = (0,0,0)
const.COLOR_WHITE = (255,255,255)
const.COLOR_RED = (255,0,0)
const.COLOR_GREEN = (0,255,0)
const.COLOR_BLUE = (0,0,255)

# 画像ファイルパス


# 進行イベント定義
const.EVENT_OPENING = 1

# playerクラス
class player():
    Name = 'Name'
    HP = 0
    MaxHP = 0
    MP = 0
    MaxMP = 0
    LV = 0
    ATK = 0
    DEF = 0
    INT = 0
    AGI = 0
    LUK = 0
    EXP = 0


#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------