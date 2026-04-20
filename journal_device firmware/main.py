import machine
import setup
import asyncio
import ui
from setup import defineAllComp


TFT_SDA = 40
TFT_SCL =39
TFT_CS = 1
SD_D0 =12 #spi miso pin
SD_CMD =11 #spi mosi
SD_CLK= 10#clck signal
SD_D3 =17 #spi cs pin

class Device:
    def __init__(self):
        setup = defineAllComp()
        
        self.spi_tft = setup.defineSPI(id=1,baudrate=4000000, SCK=TFT_SCL,MOSI=TFT_SDA, MISO=None)
        
        self.spi_sd = setup.defineSPI(id=2,baudrate=2000000, SCK=SD_CLK,MOSI=SD_CMD, MISO=SD_D0)
        
        self.tft = setup.defineTFT(self.spi_tft, TFT_CS=TFT_CS, TFT_RST=TFT, rotation=0)
        self.sd = setup.defineSdcard(self.spi_sd, CS=SD_D3)