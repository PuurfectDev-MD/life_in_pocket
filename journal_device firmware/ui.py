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
        self.tft.text("HOME", 50, 100, 0xFFFFF)
        
        
    def handle_input(self, buttons):
        if buttons['SW4']:
            return "camera"
        return None
    
    
class CameraPage(Page):
    def draw(self):
        self.tft.fill(0xF800)
        self.tft.text("CAMERA PAGE", 50,100, 0xFFFF)