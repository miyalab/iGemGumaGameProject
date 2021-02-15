
import pygame
from pygame.locals import*
import sys

(w,h)=(640,480)

pygame.init()				#初期化
screen=pygame.display.set_mode((w,h))		#スクリーンの設定
pygame.display.set_caption("サウンド")

Img=pygame.image.load("C-13.PNG").convert_alpha()	#画像のロード
rect=Img.get_rect()		

sound=pygame.mixer.Sound("ashioto.ogg")		#効果音の設定

pygame.mixer.music.load("op2.ogg")	#BGMの設定
pygame.mixer.music.play(-1)			#BGMの出力



while(1):

 screen.fill((0,0,255))
 screen.blit(Img,rect)
 pygame.display.update()
 
 for event in pygame.event.get():
  if event.type==QUIT:
   sys.exit()
   
  if event.type==KEYDOWN:
   if event.key==K_LEFT:
    rect.move_ip(-10,0)
    sound.play()		#効果音の出力
   if event.key==K_RIGHT:
    rect.move_ip(10,0)
    sound.play()		#効果音の出力
   if event.key==K_UP:
    rect.move_ip(0,-10)
    sound.play()		#効果音の出力
   if event.key==K_DOWN:
    rect.move_ip(0,10)
    sound.play()		#効果音の出力