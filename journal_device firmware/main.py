import machine
import setup
import asyncio
import ui
from setup import defineAllComp
import time

TFT_SDA = 40
TFT_SCL =39
TFT_CS = 1
TFT_DC =15

SD_D0 =12 #spi miso pin
SD_CMD =11 #spi mosi
SD_CLK= 10#clck signal
SD_D3 =17 #spi cs pin

CAM_SDA= 9
CAM_SCL =8


INT_B = 18

class Device:
    def __init__(self):
        setup = defineAllComp()
        
        self.spi_tft = setup.defineSPI(id=1,baudrate=4000000, SCK=TFT_SCL,MOSI=TFT_SDA, MISO=None)
        self.spi_sd = setup.defineSPI(id=2,baudrate=2000000, SCK=SD_CLK,MOSI=SD_CMD, MISO=SD_D0)
        self.mcp = setup.defineExpander(scl_pin=8, sda_pin=9)
        
        self.btn_state = False
        self.int_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP) # Check if it's 18 or 19
        self.int_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.isr)
        
        self.tft = setup.defineTFT(self.spi_tft, mcp=self.mcp, TFT_DC= TFT_DC,TFT_CS=TFT_CS, rotation=0)
        self.sd = setup.defineSdcard(self.spi_sd, CS=SD_D3)
        
        self.pages = {
            "home": ui.HomePage(self.tft, self),
            "camera": ui.CameraPage(self.tft, self)
        }
        
    def isr(self, pin):
        self.btn_state = True
        
        
    def get_ui_event(self):
        if not self.btn_state:
            return None
        
        # Read raw data from the setup tool
        raw = self.mcp.portb.intcap 
        self.btn_state = False # Clear the interrupt flag
        
        # Mapping logic stays here in the main app
        events = []
        if bool(raw & (1 << 4)): events.append("UP")
        if bool(raw & (1 << 6)): events.append("DOWN")
        if not bool(raw & (1 << 7)): events.append("LEFT")
        if not bool(raw & (1 << 8)): events.append("RIGHT")
        
        return events # e.g., ["LEFT", "UP"]
    
    
    

device = Device()
current_page = device.pages["home"]
current_page.draw()


while True:
    events = device.get_ui_event()
    
    if events:
        new_page_key = current_page.handle_input(events)
        if new_page_key and new_page_key in device.pages:
            current_page = device.pages[new_page_key]
            current_page.draw()
            
    time.sleep_ms(50)
                                        