import numpy as np
from PIL import Image


class Character:
    def __init__(self, joystick):
        self.appearance = 'circle'
        self.state = None
        #self.position = np.array([self.joystick.width_()/2 - 100, self.joystick.height_()/2 - 58, self.joystick.width_()/2 + 20, self.joystick.height_()/2 + 40])
        self.joystick = joystick
        self.width = self.joystick.width_()
        self.height = self.joystick.height_()
        self.position = np.array([self.width/2 - 20, self.height/2 - 20, self.width/2 + 20, self.height/2 + 20])
        self.loopy = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/loopy1.png")
        self.wall_color = (0, 0, 0)
        self.goal_color = (154, 107, 75)
        self.level = 1
    
    def move(self, command = None, coins=[]):
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
            
        if not self.is_wall(new_position):
            self.position = new_position
            
        if self.check_coin_collision(coins):
            self.score += 100  
        
        if self.is_scoring_area():
            self.score += 500
            self.joystick.change_level(self.level)
            self.level += 1
             
        

    def display(self):
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