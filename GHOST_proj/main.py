from PIL import Image, ImageDraw
from Character import Character
from Joystick import Joystick
from Ghost import Ghost
from Start import Start
from Coin import Coin
import time

def main():
    start = Start()  # 시작화면
    try:
        start.show_initial_screen()
        start.wait_for_button_press()
    
    except KeyboardInterrupt:
        pass

    joystick = Joystick()  # joystick 초기화
    
    
    
    my_loopy = Character(joystick)  # 캐릭터 객체 생성
    my_loopy.display()  # 캐릭터 띄우기


    
    
    enemy1 = Ghost(joystick, (50, 50))
    enemy2 = Ghost(joystick, (120, 120))   # 유령 생성
    enemies = [enemy1, enemy2]
    
    
    coin1 = Coin(joystick, (100, 50))
    coin2 = Coin(joystick, (100, 150))    # 호박 생성
    

    coins = [coin1, coin2]

        
    while True:
        for coin in coins:   # 코인 화면에 띄우기 
            coin.display()
            print("display")    
            
        for enemy in enemies:   # 유령 화면에 띄워서 움직이게
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

          
        my_loopy.move(command, coins)  # 캐릭터 이동
        my_loopy.display()  # 캐릭터 띄우기
        
            
        time.sleep(0.1)
        


if __name__ == '__main__':
    
    main()