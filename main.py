import pygame
import sys, random

from pygame.locals import *

#初期化
pygame.init()
screen = pygame.display.set_mode((1000, 500))
white = (255, 255, 255)
black = (0, 0, 0)
FontPath = "JNRfont_s.ttf"

refreshRate = 60 #リフレッシュレート 
font1 = pygame.font.Font(FontPath, 150)



def main():
    #ループ内
    Time = 0
    TimeText = ""
    while True:
        Time += 1/refreshRate
        TimeText = str(int(Time)) + "秒"
        screen.fill(black)
        text1 = font1.render(TimeText, True, (255, 255, 255))
        screen.blit(text1, (0, 0))
        # 画面を更新 --- (*4)
        pygame.display.update()
        # 終了イベントを確認 --- (*5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.time.delay(int(1000/refreshRate))

if __name__=="__main__":
    main()