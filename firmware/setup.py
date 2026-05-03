from machine import Pin,SPI, I2S, I2C
import mcp23017
import st7789py as st7789
from machine import SDCard
import network
import asyncio
import time
from acamera import Camera, FrameSize, PixelFormat 

import machine, network



WIFI_SSID = ""
WIFI_PASS = ""
KEEP_API_KEY = ""
    
class defineAllComp:
    def __init__(self):
        pass
    
    def defineSPI(self,id,baudrate,SCK,MOSI, MISO):
         spi = SPI(id,
        baudrate=baudrate,
        polarity=1,
        phase=0,
        sck=SCK,
        mosi=MOSI,
        miso=MISO)
         print(f"SPI is initialized with baudrate {baudrate}")
         return spi

    def defineTFT(self,spi, mcp,TFT_DC, TFT_CS, rotation):
        mcp.porta.mode &= ~(1 << 2)
        # Reset Sequence: Low -> Wait -> High
        mcp.porta.gpio &= ~(1 << 2)  # Pull Reset LOW
        time.sleep_ms(100)
        mcp.porta.gpio |= (1 << 2)   # Pull Reset HIGH
        time.sleep_ms(100)
        
        
        tft = st7789.ST7789(
        spi,
        240,
        240,
        reset=None,
        cs=Pin(TFT_CS, Pin.OUT),
        dc=Pin(TFT_DC, Pin.OUT),
        rotation=rotation)
        print(f"TFT is initialized with rotation {rotation}")
        return tft
    def defineI2S(self,BCK, WS):
        I2S = I2S(I2S.NUM0,                                  # create I2S peripheral to write audio
                bck=BCK, ws=WS,   # sample data to an Adafruit I2S Amplifier
                standard=I2S.PHILIPS, mode=I2S.MASTER_TX,  # breakout board, 
                dataformat=I2S.B16,                        # based on MAX98357A device
                channelformat=I2S.ONLY_RIGHT,
                samplerate=16000, 
                dmacount=16,dmalen=512)
        print("I2S has been initialized.")
        return I2S
    
    def defineSdcard(self, spi_bus, CS):
        try:
            sd = SDCard(spi_bus, Pin(CS))
            # Mount the filesystem
            import os
            os.mount(sd, '/sd')
            print("SD Card mounted at /sd")
            return sd
        except Exception as e:
            print(f"Failed to mount SD: {e}")
        
    def defineCamera(self, vsync, href, i2c, pclk, xclk, freq, powerd, reset):
        # cam = Camera(FrameSize.VGA, pixel_format = PixelFormat.JPEG, jpeg_qualiy=85, init=False)
        cam = Camera(data_pins=[0,1,2,3,4,5,6,7],
                     vsync_pin =vsync,
                     href_pin=href, 
                     i2c = i2c,
                     pclk_pin=pclk,
                     xclk_pin=xclk, 
                     xclk_freq=freq, powerdown_pin=powerd,reset_pin=reset)
        print("Camera has been iniitalized")
        return cam
        
    def defineSpeaker(self, bck,ws, sdout, sampleRate):
        speaker = I2S(I2S.NUM1, bck=bck, ws=ws, sdout=sdout, standard=I2S.PHILIPS, mode=I2S.MASTER_TX, datafromat=I2S.B16,
                      channelformat=I2S.ONLY_LEFT,
                      samplerate=sampleRate,dmacount=10, dmalen=512)
        print("You speaker is intialized")
        return speaker
    def defineMic(self, bck, ws, sdin, sampleRate, dmalen):
        mic = I2S.NUM1,bck=bck, ws=ws, sdin=sdin,standard=I2S.MASTER_RX, dataformat=I2S.B32, channelformat=I2S.ONLY_LEFT,
        samplerate=sampleRate, dmacount=50, dmalen=dmalen
        print("Mic has been defined")
        return mic
    
    
    def defineExpander(self, scl_pin, sda_pin):
        i2c = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin))
        mcp = mcp23017.MCP23017(i2c, address=0x20) # 0x20 is default for A0,A1,A2 to GND
        
        
        input_mask = (1 << 4) | (1 << 6) | (1 << 7) | (1 << 8)
        mcp.portb.mode |= input_mask
        
        mcp.portb.pullup &= ~input_mask
        
        
        # 3. Interrupts
        mcp.config.mirror = True 
        mcp.portb.er_int |= input_mask
    
        # Configure pins from schematic: GPB4, GPB5 (TTP223) and GPB6, GPB7 (Switches)
        # 0x00 is output, 0xFF is input. Let's set the whole B port as input:
   
        return mcp
    
    def read_expander_port_b(self, mcp):
    # Just returns the raw integer value of the port
        return mcp.portb.intcap
    
    
    
def wifi_connect():
    wlan = network.WLAN()
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            machine.idle()
    print('network config:', wlan.ipconfig('addr4'))