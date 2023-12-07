from PIL import Image
import numpy as np

class Coin:
    def __init__(self, joystick, spawn_position):
        self.appearance = 'circle'
        self.joystick = joystick
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.image = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/pumkin.png")
    
    def display(self):  # 호박 화면에 띄우기
        self.joystick.display(self.image, (self.position[0], self.position[1]))
        