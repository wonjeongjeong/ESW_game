import numpy as np
from PIL import Image
import time

class Ghost:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = 'right'
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
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
    
    def display(self, draw):
        draw.bitmap((int(self.position[0]), int(self.position[1])), self.image, fill=None)