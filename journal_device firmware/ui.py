import actions

class Page:
    def __int__(self, tft, device):
        self.tft = tft
        self.device = device
    def draw(self):
        pass
    def handle_input(self, button_states):
        pass


class HomePage(Page):
    def draw(self):
        self.tft.fill(0x0000)
        self.tft.text("HOME", 175, 20, 0xFFFFF)
        self.tft.text("Memory", 10, 150, 0xFFFFF)
        self.tft.text("Voice", 295, 150, 0xFFFFF)
        
        
    def handle_input(self, button_states):
        if "LEFT" in button_states:
            return "memory"
        
        if 'Right' in button_states:
            return "voice"
       
    
    
class CameraPage(Page):
    def draw(self):
        self.tft.fill(0xF800)
        self.tft.text("CAMERA PAGE", 50,100, 0xFFFF)
        
        
        
    def handle_input(self, button_states):
        if "LEFT" in button_states:
            actions.takePicture(self.device.cam, self.device.sd)
            return None
        if "RIGHT" in button_states:
            return "Home"