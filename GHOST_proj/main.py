from PIL import Image, ImageDraw
from Character import Character
from Joystick import Joystick
from Ghost import Ghost
from Start import Start
from Coin import Coin
import time

def main():
    start = Start()
    try:
        start.show_initial_screen()
        start.wait_for_button_press()
    
    except KeyboardInterrupt:
        pass

    joystick = Joystick()
        
        # 이미지 위에 그림을 그리기 위해 ImageDraw 객체 생성
    
    
    # 잔상이 남지 않는 코드
    
    my_loopy = Character(joystick)
    my_loopy.display()

        # 캐릭터를 현재 위치에 그리기
    
    
    enemy1 = Ghost(joystick, (50, 50))
    enemy2 = Ghost(joystick, (120, 120))
    enemies = [enemy1, enemy2]
    
    
    coin1 = Coin(joystick, (100, 50))
    coin2 = Coin(joystick, (100, 150))
    # 여러 개의 코인을 추가할 수 있습니다.

    coins = [coin1, coin2]

        
    while True:
        for coin in coins:
            coin.display()
            print("display")    
            
        for enemy in enemies:
            enemy.display()
            enemy.move()
        
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
    
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

          
        my_loopy.move(command, coins)
        my_loopy.display()  
        
            
        time.sleep(0.1)
        


if __name__ == '__main__':
    
    main()