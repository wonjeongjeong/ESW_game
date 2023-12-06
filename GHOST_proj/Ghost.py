import numpy as np
from PIL import Image
import time

class Ghost:
    def __init__(self, joystick, spawn_position):
        self.appearance = 'circle'
        self.state = 'right'
        self.joystick = joystick
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.image = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/ghost_left.png")
        
        
    def move(self):
        i = 0
        while True:
            self.state = 'right' if self.state == 'left' else 'left'
            i = 0
            while i <= 20:
                if self.state == 'left':
                    self.position[0] -= 5
                    self.position[2] -= 5
                    i += 5
                else:
                    self.position[0] += 5
                    self.position[2] += 5
                    i += 5
            time.sleep(0.1)
    
    def display(self):
        self.joystick.display(self.image, (self.position[0], self.position[1]))
    