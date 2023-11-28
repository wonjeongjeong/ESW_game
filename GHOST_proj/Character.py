import numpy as np
from PIL import Image


class Character:
    def __init__(self, width, height, image_path):
        self.appearance = 'circle'
        self.state = None
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        self.outline = "#FFFFFF"
        self.image = Image.open(image_path)

    def move(self, command = None):
        if command == None:
            self.state = None
            self.outline = "#FFFFFF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if command == 'up_pressed':
                self.position[1] -= 5
                self.position[3] -= 5

            elif command == 'down_pressed':
                self.position[1] += 5
                self.position[3] += 5

            elif command == 'left_pressed':
                self.position[0] -= 5
                self.position[2] -= 5
                
            elif command == 'right_pressed':
                self.position[0] += 5
                self.position[2] += 5
                
    def display(self, draw):
        draw.rectangle(tuple(self.position), outline=self.outline, fill=(0, 0, 0))
        draw.bitmap((int(self.position[0]), int(self.position[1])), self.image, fill=(255, 255, 255))