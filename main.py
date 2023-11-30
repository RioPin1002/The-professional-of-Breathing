import pygame
import sys, random
import numpy as np

from pygame.locals import *

#初期化
pygame.init()
screen = pygame.display.set_mode((1000, 500))
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
lightGray = (100, 100, 100)
FontPath = "JNRfont_s.ttf"

refreshRate = 60 #リフレッシュレート 
font1 = pygame.font.Font(FontPath, 40)
inhaleText = font1.render("吸", True, (255, 255, 255)) 
exhaleText = font1.render("吐", True, (255, 255, 255))

spawnSum = 10


#ランダムマッピング



def main():
    #ループ内
    Time = 0
    TimeText = ""
    hale = np.empty((spawnSum, 3))
    wKey = False
    sKey = False
    score = 0

    #初期スポーン
    for num in range(spawnSum):
        hale[num, 0] = random.randint(10, 15) * 100 #画面外にランダムでx座標を獲得
        hale[num, 1] = 230
        hale[num, 2] = random.randint(1, 2) #1は吸 2は吐
    
    hale_op = hale
        
    print(hale)

    while True:
        Time += 1/refreshRate
        TimeText = str(int(Time)) + "秒"

        #背景設定
        screen.fill(black) #背景
        pygame.draw.circle(screen, gray, (150, 250), 40)
        pygame.draw.circle(screen, lightGray, (150, 250), 20)

        text1 = font1.render(TimeText, True, (255, 255, 255)) #時間描写
        scoreText = font1.render("score" + str(score), True, (255, 255, 255))
        screen.blit(text1, (0, 0)) 
        screen.blit(scoreText, (0, 40))


        #最もヒットスポットと近いhaleを計算
        filtered_values = hale_op[hale[:, 0] >= 150, 0]
        closest_to_150_value = filtered_values[np.argmin(np.abs(filtered_values - 150))]
        row_number = np.where(hale[:, 0] == closest_to_150_value)[0][0]

        #当たり判定
        if 135 <= closest_to_150_value <= 155:
            if (wKey == True & int(hale[row_number, 2]) == 1) | (sKey == True & int(hale[row_number, 2]) == 0):
                score += 100
        if 125 <= closest_to_150_value <= 165:
            if (wKey == True & int(hale[row_number, 2]) == 1) | (sKey == True & int(hale[row_number, 2]) == 0):
                score += 50
                    
        for num in range(spawnSum):
            if hale[num, 2] == 1:
                screen.blit(inhaleText, (hale[num, 0], hale[num, 1]))
            if hale[num, 2] == 2:
                screen.blit(exhaleText, (hale[num, 0], hale[num, 1]))



        #haleの速度調整
        for num in range(spawnSum):
            hale[num, 0] -= 2
            if hale[num, 0] < -50:
                hale[num, 0] = random.randint(20, 30) * 50 #画面外にランダムでx座標を獲得
                hale[num, 1] = 230
                hale[num, 2] = random.randint(1, 2) #1は吸 2は吐

    


        # 画面を更新 --- (*4)
        pygame.display.update()

        
        # 終了イベントを確認 --- (*5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                # ESCキーならスクリプトを終了
                if event.key == K_w:
                    wKey = True
                if event.key == K_s:
                    sKey = True
                    

        pygame.time.delay(int(1000/refreshRate))

if __name__=="__main__":
    main()