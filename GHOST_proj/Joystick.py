from digitalio import DigitalInOut, Direction
from adafruit_rgb_display import st7789
import board
from PIL import Image, ImageDraw

class Joystick:
    def __init__(self):
        self.cs_pin = DigitalInOut(board.CE0)
        self.dc_pin = DigitalInOut(board.D25)
        self.reset_pin = DigitalInOut(board.D24)
        self.BAUDRATE = 24000000

        self.spi = board.SPI()
        self.disp = st7789.ST7789(
                    self.spi,
                    height=240,
                    y_offset=80,
                    rotation=180,
                    cs=self.cs_pin,
                    dc=self.dc_pin,
                    rst=self.reset_pin,
                    baudrate=self.BAUDRATE,
                    )

        # Input pins:
        self.button_A = DigitalInOut(board.D5)
        self.button_A.direction = Direction.INPUT

        self.button_B = DigitalInOut(board.D6)
        self.button_B.direction = Direction.INPUT

        self.button_L = DigitalInOut(board.D27)
        self.button_L.direction = Direction.INPUT

        self.button_R = DigitalInOut(board.D23)
        self.button_R.direction = Direction.INPUT

        self.button_U = DigitalInOut(board.D17)
        self.button_U.direction = Direction.INPUT

        self.button_D = DigitalInOut(board.D22)
        self.button_D.direction = Direction.INPUT

        self.button_C = DigitalInOut(board.D4)
        self.button_C.direction = Direction.INPUT

        self.backlight = DigitalInOut(board.D26)
        self.backlight.switch_to_output()
        self.backlight.value = True

        
        self.width = self.disp.width
        self.height = self.disp.height

    def width_(self):
        return int(self.width)
    
    def height_(self):
        return int(self.height)
        
    def display(self, image, position=(0,0)):
        draw = ImageDraw.Draw(image)
        img_width, img_height = image.size
        x, y = position
        x=int(x)
        y=int(y)
        self.disp.image(image, x=x, y=y)   
    
    
    def change_level(self, level):
        if level == 0:
            level1 = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/level1.png")
            self.background = level1.resize((self.width, self.height))
        elif level == 1:
            level2 = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/level2.png")
            self.background = level2.resize((self.width, self.height))
        elif level == 2:
            level3 = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/level3.png")
            self.background = level3.resize((self.width, self.height))
        else:
            level4 = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/level4.png")
            self.background = level4.resize((self.width, self.height))
            
        self.disp.image(self.background)