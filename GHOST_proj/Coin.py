from PIL import Image
import numpy as np

class Coin:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.position = None
        self.image = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/pumkin.png")
    
    def display(self, draw):
        draw.bitmap((int(self.position[0])), int(self.position[1]), self.image, fill=None)    
        