import random
import math
from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
import pygame
from pygame.locals import *
import sys

import generate_field_map


def main():

    pygame.init()       # pygame初期化
    pygame.display.set_mode((800, 600), 0, 32)  # 画面設定
    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()




    field_map , px , py = generate_field_map.generate_field_map()


    while True:

        pygame.display.update()     # 画面更新
        clock.tick(60)


        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            pass


        screen.fill((0, 0, 0, 0))   # 画面の背景色

        
        for i in range(20):
            for j in range(20):

                if (i,j) == (px,py):
                    pygame.draw.rect(screen,(0,45,85),Rect(i*30+1,j*30+1,28,28))
                    continue

                if field_map[i][j] == 0:
                    pygame.draw.rect(screen,(25,25,25),Rect(i*30+1,j*30+1,28,28))

                if field_map[i][j] == 1:
                    pygame.draw.rect(screen,(85,85,85),Rect(i*30+1,j*30+1,28,28))

                if field_map[i][j] == 2:
                    pygame.draw.rect(screen,(0,45,85),Rect(i*30+1,j*30+1,28,28))

        

        # イベント処理
        for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーを押したとき
            if event.type == KEYDOWN:
                if event.key == K_r:
                    field_map , px , py = generate_field_map.generate_field_map()

                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()