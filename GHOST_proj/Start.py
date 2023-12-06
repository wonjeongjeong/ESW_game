from Joystick import Joystick
from PIL import Image

class Start:
    def __init__(self):
        self.joystick = Joystick()
        self.background = Image.new("RGB", (self.joystick.width, self.joystick.height))
        
    def show_initial_screen(self):
        background = Image.open("/home/kau-esw/ESW/.git/ESW_game/GHOST_proj/Start.png")
        intro_image = background.resize((self.joystick.width, self.joystick.height))
        self.joystick.disp.image(intro_image)
        print("Avoid the Ghost")
    
    def wait_for_button_press(self):
        print("Press any button to start")
        while all([self.joystick.button_A.value, self.joystick.button_B.value, self.joystick.button_C.value, self.joystick.button_D.value, self.joystick.button_L.value, self.joystick.button_R.value, self.joystick.button_U.value]):
            pass
        print("Button pressed! Starting the game ...")
        
        self.joystick.change_level(0)
        
        
    
    