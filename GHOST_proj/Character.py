
from PIL import Image

class Character:
    def __init__(self, width, height):
        self.appearance = 'rectangle'
        self.state = 'alive'
        self.position = [width/2 - 100, height/2 - 58, width/2 + 20, height/2 + 40]
        self.outline = None
        self.image = Image.open("/home/kau-esw/esw/GHOST_proj/loopy.png")
        
        #my_image = Image.new("RGB", (self.width, self.height))
        #my_image.paste(self.image, (0, 0))
    def move(self, command = None):
        #if command == None:
        #    self.state = None
        
        #else:
        #    self.state = 'move'

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
        draw.bitmap((int(self.position[0]), int(self.position[1])), self.image, fill=None)            
        