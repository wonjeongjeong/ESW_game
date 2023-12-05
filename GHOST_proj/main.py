from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb

from Character import Character
from Joystick import Joystick
from Ghost import Ghost
from Start import Start

def main():
    """start = Start()
    try:
        start.show_initial_screen()
        start.wait_for_button_press()
    
    except KeyboardInterrupt:
        pass"""

    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_image.paste(joystick.background, (0, 0))
    # 잔상이 남지 않는 코드
    my_circle = Character(joystick.width, joystick.height)
    my_circle.display(my_draw)
    
    enemy = Ghost(joystick.width, joystick.height)
    enemy.display(my_draw)
    enemy.move()
    
    while True:
        command = None
        if not joystick.button_U.value:  # up pressed
            command = 'up_pressed'

        elif not joystick.button_D.value:  # down pressed
            command = 'down_pressed'

        elif not joystick.button_L.value:  # left pressed
            command = 'left_pressed'

        elif not joystick.button_R.value:  # right pressed
            command = 'right_pressed'
            
        else:
            command = None
            
        enemy.move()
        my_circle.move(command)
        
        #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        my_image.paste(joystick.background, (0, 0))
        my_circle.display(my_draw)
        enemy.display(my_draw)
        #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        joystick.disp.image(my_image)


if __name__ == '__main__':
    
    main()