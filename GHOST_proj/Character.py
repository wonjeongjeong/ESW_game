import numpy as np
from PIL import Image


class Character:
    def __init__(self, joystick):
        self.appearance = 'circle'
        self.state = None
        self.joystick = joystick
        self.width = self.joystick.width_()
        self.height = self.joystick.height_()
        self.position = np.array([self.width/2 - 20, self.height/2 - 20, self.width/2 + 20, self.height/2 + 20])
        self.loopy = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/loopy1.png")
        self.wall_color = (0, 0, 0)  #검정 색상 코드
        self.goal_color = (154, 107, 75)   # 도착지점 색상 코드
        self.level = 1   #현재 레벨 숫자
        self.score = 0   # 점수
    
    def move(self, command = None, coins=[]):  # 캐릭터 이동 함수
        new_position = self.position.copy()
        if command['move'] == False:
            self.state = None
        
        else:
            self.state = 'move'

            if command['up_pressed']:
                self.position[1] -= 5
                self.position[3] -= 5

            if command['down_pressed']:
                self.position[1] += 5
                self.position[3] += 5

            if command['left_pressed']:
                self.position[0] -= 5
                self.position[2] -= 5
                
            if command['right_pressed']:
                self.position[0] += 5
                self.position[2] += 5
            
        if not self.is_wall(new_position):   # 캐릭터 현재 위치가 벽이 아니라면 그대로 진행
            self.position = new_position
            
        if self.check_coin_collision(coins):        # 코인 먹었을 때
            self.score += 100  
        
        if self.is_scoring_area():            # 도착지점에 도착했을 때
            self.score += 500
            self.joystick.change_level(self.level)
            self.level += 1
             
        

    def display(self):    # 캐릭터 화면에 띄우기
        self.joystick.display(self.loopy,(self.position[0], self.position[1]))
    
    def check_collision(self, other):
        return (
            self.position[0] < other.position[2]
            and self.position[2] > other.position[0]
            and self.position[1] < other.position[3]
            and self.position[3] > other.position[1]
        )
        
    def check_coin_collision(self, coins):
        
        for coin in coins:
            if self.check_collision(coin):
                coins.remove(coin)
                return True
            
        return False
    
    def is_wall(self, position):
        # Check if any corner of the new position is a wall
        for x in range(int(position[0]), int(position[2])):
            for y in range(int(position[1]), int(position[3])):
                pixel = self.loopy.getpixel((x, y))
                if pixel == self.wall_color:
                    return True
        return False
    
    def is_scoring_area(self):
        # Check if the current position is in the scoring area (check the center of the character)
        center_x = int((self.position[0] + self.position[2]) / 2)
        center_y = int((self.position[1] + self.position[3]) / 2)
        pixel = self.loopy.getpixel((center_x, center_y))
        return pixel == self.goal_color