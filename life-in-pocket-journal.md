# Life in pocket — Journal Export

- Exported at: 2026-05-10T09:25:49Z
- Project ID: 775
- Entries: 45

## Entry 1
- ID: 400
- Author: Manish
- Created At: 2026-03-24T05:41:12Z

### Content

Today all I'm going to do is form a basic idea of what it's going to look like and solidify my idea. And assemble the things/resources I will need to build this project.


The idea:
I want an ultimate journaling device, A device that lets me take pictures, even videos, and record audio (voice memo) for me to reminisce about in the future. For this device to work, I need it to be very portable, or else it will be like your bag instead of your pocket. I want it to be compact, interesting, and portable, so I can carry it around wherever and whenever. 


The main idea of the project comes from me being fond of recording and saving my daily life. And the Adafruit memento - 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTE3LCJwdXIiOiJibG9iX2lkIn19--b409c9ed275f07e940195436f1195b78c11ac75d/image.png)
https://learn.adafruit.com/memento-3d-case

This really made the idea click and made me pursue this project. It will be very similar to the memento but with audio capabilities and even api endpoints in the software side of things. Im thinking of making a SvelteKit-based website with db so that users can connect to their esp32 (thats the MCU I have decided upon - because I just have a lot of experience with it) and upload it to the internet. By doing that, the user can access the vids, photos, and recordings anywhere, anytime. Now that's very ambitious, I'll probably keep it for later when everything is all assembled and ready to go.

Now, let's list the parts and begin the project: 
1- The MCU - ESP32 S3 Wroom 1 - (this has psram aswl and internet, blutooth - basically it fits the project.) I need something compact and pwoerful and this seems right.

2- Sd card module. - (For v1 Im making it me oriented and then later for everyone else as in - supports users. So lets just begin by storing the content in the sd card and then later use api, web requests for the internet upload stuff)

3-  A small but big screen.
https://thepihut.com/products/adafruit-2-0-320x240-color-ips-tft-display-with-microsd-card-breakout?srsltid=AfmBOopbSg56YCUEnnCTbiO-TJ4eLOSOaCXRWPdJsdKlX3xsoJeE6DI2


This is a nice form factor. I will go with this, To make it cheaper here is the aliexpress link:
https://ar.aliexpress.com/item/1005007404892390.html?gatewayAdapt=glo2ara



4- A speaker -  (A really small one)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTE5LCJwdXIiOiJibG9iX2lkIn19--9e82eaa18d85252b18f1eec7fb731f85a1e4bc63/image.png)

5. A mic for voice memo. I have used this one in my other projects too so ill go with the same.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTIwLCJwdXIiOiJibG9iX2lkIn19--d99568b8aa607aa48104f87d0ab358ee2142fc6b/image.png)

6. Small momentary push buttons.
7. A shutter/record self-latching switch - 10mm (as small as possible)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTIxLCJwdXIiOiJibG9iX2lkIn19--db9b41b519b84e0b616f1613d4d04d08ccee8bfe/image.png)
The 10mm should be fine.

7. An amp - 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTIyLCJwdXIiOiJibG9iX2lkIn19--30090bb840919e4396d42789a27fad001bc50e16/image.png)
This shall do!


And that's pretty much it for the parts. Though I have not included the small parts like resistors, LEDs, caps , usb and all that. Its not gonna be very expensive, but might get complicated.


Let's get to kicad now.
I cant find the footprint and schematic diagram for the display Im using so I will have to make a custom one. I have the assets for the mic, amp, and the chip. So Its alright.


### Recording Links

- https://lookout.hackclub.com/api/media/8b565e3a-7895-47c8-8bab-705fc3f7a785/video.mp4

## Entry 2
- ID: 494
- Author: Manish
- Created At: 2026-03-26T12:30:45Z

### Content

Now lets search for a camera module that we can work with. I think i should go with an already assembled camera board instead of complicating my schmatic with the camera stuff.
I could use a 24 pin connecter for the ov2640 camera but then i would need to handle the signals, the power which im not very confident about for the camera.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExMywicHVyIjoiYmxvYl9pZCJ9fQ==--6ee3979a43f1710b059db745b5714161d93b85f7/image.png)

All these general components I have to hook and cautiously manage signals is a task that can just be resolved by using a packaged ESP32 board with a camera on it.
Like this:

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExNCwicHVyIjoiYmxvYl9pZCJ9fQ==--6645f5d15e445117185203fba5b7466bfd5933f7/image.png)
BUt if im to choose this then itll make the whole project plug and play. I dont have to solder the esp32 chip anymore  if im using this dev board. And just solder each modules and itll be done. 
Hmmm. Let me ask help from claude.


So the connection is not that very complicated. What I figured is -there needs to be 2-3 different power voltages which is not that tough to manage with the asm chips. 
I stumbled upon this:
https://docs.cirkitdesigner.com/component/55a86ec4-928d-474d-b6d5-7a61590da79a/ov2640-camera-module

I can use a camera setup which only require a few pins.. that way its much more simpler and i can still work with the chip.



Okay i found it !
https://learn.adafruit.com/ttl-serial-camera/overview


This will be the camera Ill be using. NO more 24 pin connections.
BUt these are so so expensive. In adafruit's wesbite its around 40$. 
In aliexpress aswell they go for around the same. There is this cheaper module:
https://ar.aliexpress.com/item/1005008472883703.html?gatewayAdapt=glo2ara
BUt i dont want to spend 24$ on just the camera module.


So I think I should go with this datasheet and work with the 24 pin connecter. no other option.



Okay change of plans. I got a cheap assmebld pcb fora camera module wihch fits my project.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExNiwicHVyIjoiYmxvYl9pZCJ9fQ==--19d9a3ab04b0c06dbe14954b156734dccea9f745/image.png)
This was what I was going for but then I stumbled upon this:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExNywicHVyIjoiYmxvYl9pZCJ9fQ==--0f77634cd7b3142351a5f2fd8acb7ac76b2ef437/image.png)

So I wont need to do more soldering and worry about the camera connecter side of things and the 3 different power aswl with this. and they are the same price. So Ill go with this! **(FINAL!)**
https://ar.aliexpress.com/item/1005004471654205.html?spm=a2g0o.productlist.main.3.2aeb0uOf0uOfba&algo_pvid=89c5adb3-60d1-44cf-ba85-5f3eab1174db&algo_exp_id=89c5adb3-60d1-44cf-ba85-5f3eab1174db-2&pdp_ext_f=%7B"order"%3A"72"%2C"eval"%3A"1"%2C"fromPage"%3A"search"%7D&pdp_npi=6%40dis%21USD%219.95%219.95%21%21%219.95%219.95%21%40212a70c117745103471605831e5878%2112000029283148367%21sea%21AE%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A6924c055%3Bm03_new_user%3A-29895&curPageLogUid=Nq2pZIp5P0Cb&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005004471654205%7C_p_origin_prod%3A


Now lets make a custom footprint for the module.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTExOSwicHVyIjoiYmxvYl9pZCJ9fQ==--050ad49cf04c0ae235cab9ca9472d8b83d652c13/image.png)
Now thats done. I need the footprint. Actually I dont. what Im planning is -i ll handwire the pads from the cmaera module to the pin headers of the pcb. This way I dont need to worry about getting my dimensions wrong for the footprint becasue its not there in the product listing. For the case I think Ill have to contact the supplier but for now its not problem!


This is the esp Ill be using.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEyMCwicHVyIjoiYmxvYl9pZCJ9fQ==--f40203a384d0f49bbd67c3de6bf5674d8638ee91/image.png)
www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf

It has eveything this project needs:
40mhz oscillator - (even though the module has its own osscillator for the camera)
wifi, bluetooth, psram, 3.3v power, audio capabilities, image processing and allthat.


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEyMiwicHVyIjoiYmxvYl9pZCJ9fQ==--48f21223e45aea37848cc0c5a8a18c9ba79c6a55/image.png)
I imported the mic module ill be using and the amp i have in mind.



now for the programming and power I ll use a breakout board (easier to solder :) ) lIke this :
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEyNCwicHVyIjoiYmxvYl9pZCJ9fQ==--8ef3e874308328ec37cef8764f0970568c49fbb0/image.png)
https://ar.aliexpress.com/item/1005007756231944.html?spm=a2g0o.productlist.main.1.249bwqfEwqfEiH&algo_pvid=a1b6b42b-d620-4118-8b68-202495ac0dae&algo_exp_id=a1b6b42b-d620-4118-8b68-202495ac0dae-0&pdp_ext_f=%7B"order"%3A"4"%2C"eval"%3A"1"%2C"fromPage"%3A"search"%7D&pdp_npi=6%40dis%21USD%212.47%211.21%21%21%2116.95%218.31%21%402101584917745132426208505e3348%2112000042100172927%21sea%21AE%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A6924c055%3Bm03_new_user%3A-29895&curPageLogUid=IbnylBw7d78S&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007756231944%7C_p_origin_prod%3A

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEyNSwicHVyIjoiYmxvYl9pZCJ9fQ==--0db61dee1116eb27e5950f64e35cc09877ac1735/image.png)

And a charging module board with protecting for the lipo battery

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEyNiwicHVyIjoiYmxvYl9pZCJ9fQ==--a917a6f6d2b2ec39c35b1b5d5cabdea9756a4a1c/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEyNywicHVyIjoiYmxvYl9pZCJ9fQ==--c209255a17ad207a91498bf81bdca877b0d1665e/image.png)
Like these. And thats pretty much it! Oh ... the 3.3v regualtor awl.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEyOCwicHVyIjoiYmxvYl9pZCJ9fQ==--09478c9fd712295916da3b51451b50cf23ce610b/image.png)

Okay the diagram imports are done! (Just without the general components)

### Recording Links

- https://public.lapse-hackclub.link/timelapses/q3tvP5u3tGeN/timelapse-q3tvP5u3tGeN.mp4

## Entry 3
- ID: 498
- Author: Manish
- Created At: 2026-03-26T13:42:47Z

### Content

First Ill do the power side of things.
The power is going to come from the battery for the whole device. But keeping is a big battery is not possible due to the form factor. Maybe I /whoever is using the device could use the usb for power instead of taking power from the battery. This way we can preserve the valuable pwoer which is required when going out or something.


Ill use a p-channel MOSFET with the charging module and the usb breakout board and make it so that when usb is connected, it switches from battery to USB power.

And to save space, im thinking of designing a custom charging and protecting ciruit. Shouldn't be very complicated - I think there are packaged chips for all the features.

I found this video and Ill go with this. This was really helpful.
https://www.youtube.com/watch?v=TyaW8ZKumno&t=331s

This is the chip that is going to be the heart of the charging stuff.
 - MCP73831/2
https://ww1.microchip.com/downloads/en/DeviceDoc/20001984g.pdf


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE2MiwicHVyIjoiYmxvYl9pZCJ9fQ==--704f6c468af4abfd79c7fb313efed9be3bb64722/image.png)

There is the complete setup of the charging stuff. 

But I have a bigger problem.
The USB breakout board i picked supplies only 1.5 Amp max - ( 

"The two 5.1K resistors on the CC1 pin indicate that the upstream port provides 5V and up to 1.5A current (whether the upstream can provide this much current depends on what you are connecting to.") Which is alright, but i need headroom. It should be around 2amps. So I'm thinking of ditching the USB power breakout board altogether.

And another problem is the battery voltage. It supplies 3.7, and esp needs 3.3v. And it needs to be well-regulated with a constant supply. So I might have to design a buck converter as well.

Instead of the breakout board:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE2MywicHVyIjoiYmxvYl9pZCJ9fQ==--68b9f285c42f113957582525873bab8cb84e7ac9/image.png)
I'll solder my own USB. This does both - gives data to the esp32 for flashing and supplies power to the battery for charging.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE2NCwicHVyIjoiYmxvYl9pZCJ9fQ==--d619a6231c2ebb7c675c5b237f2f0450cfa32ffe/image.png)
Okay switched to the new 16p usb connecter :)

### Recording Links

- https://public.lapse-hackclub.link/timelapses/eG4eiZ6rmhjr/timelapse-eG4eiZ6rmhjr.mp4

## Entry 4
- ID: 522
- Author: Manish
- Created At: 2026-03-27T08:47:43Z

### Content

Now that the usb is kinda done. Let do the power supply. We need 3.3v power supply (constant). The battery (lipo battery) provides 3.7v. So we need a buck converter. But what if the battery voltage goes below 3.3V during discharge?
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxOCwicHVyIjoiYmxvYl9pZCJ9fQ==--8587859edaa9e31e9230f14f6df3d4cb61d9ebff/image.png)
So, only a buck converter will not work. We need a boost buck converter in the same package.
https://www.ti.com/lit/ds/symlink/tps63020.pdf
This is an excellent choice. It has everything I need. Max 2Amp and 3.3v from (1.8v to 5.5v). Fits the project.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIxOSwicHVyIjoiYmxvYl9pZCJ9fQ==--b8a38a523d06a07aaad9efdde7b7ecea08db97d9/image.png)

Okay lets connect this chip then..
https://www.snapeda.com/parts/TPS63020DSJR/Texas%20Instruments/view-part/

I found the schmatic symbol and the footprint for the package.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyMCwicHVyIjoiYmxvYl9pZCJ9fQ==--8712a230a20cc122fd160e41975637c0112c7e7a/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyMSwicHVyIjoiYmxvYl9pZCJ9fQ==--8a6e4a21e34bdbe2c0f07cd06425ba23dbf47e0f/image.png)

Imported the schmatic and footprint in kicad. (I imported the wrong one first :( ) 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyNSwicHVyIjoiYmxvYl9pZCJ9fQ==--16e56e1646fe31ac192bd29916a749d94b812cf9/image.png)

There it is! Now we have a clean constant 3.3V current. The GPIO X is for later ( I havnt decided yet - wether or not I want to monitor the power singal).

Added a siwtch .. so that when I want i can cut off power from the device.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyNiwicHVyIjoiYmxvYl9pZCJ9fQ==--ec9e6d90450a48a64c173f80cb98b7ca5c5c2db1/image.png)

NOw I have to figure out how to handle the power through usb and battery when the usb is connected. I imported a p channel mosfet earlier for this.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyOSwicHVyIjoiYmxvYl9pZCJ9fQ==--e200c84646e2227a3abdca12744ae2aafca2df85/image.png)


What this does is: - When there is no USB power. the gate is pulled low by the resitor -gnd part which connects the source and drain of the mosfet which connects the battery + and the VIN of the boost buck converter. BUt when the usb power is on via the usb.. the gate is pulled high which turns the MOSFET off (the source and drain disconnect ) so no more current is pulled from the battery instead the VIN is getting current from the VBUS directly. As the chip can handle around 5.5v, connecting via usb will be fine. And another thing is 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIyOCwicHVyIjoiYmxvYl9pZCJ9fQ==--915f2a031265789c3afbf2cf49e60ad3faa0b29f/image.png)
The charging module/ part still works, which means that with usb power - it powers the whole device and also charges the battery. That was exactly what i was going for. One thing to keep in mind is when connecting via usb .. we ll need to connect it to a high current charger to sustain the current requirement, (1 amp to charge the batteyr and around 1.5 amp to power the cicruit under max load ) 


Now the things I have achieved till now:
- USB power to the board
- Charging and protection ciruit for the battery
- Clean, constant 3.3v from anywhere around 2.8v to 5.5v of input ( during discharge  VIN can be <3.0v and during usb power it can >5v)
- Power switching between USB and battery based on wether power is coming from the USB or not.


Now in the next journal I ll  start connecting the components!

### Recording Links

- https://public.lapse-hackclub.link/timelapses/H5NzUc4gRftN/timelapse-H5NzUc4gRftN.mp4

## Entry 5
- ID: 535
- Author: Manish
- Created At: 2026-03-27T16:17:47Z

### Content

Lets now connect the components.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MiwicHVyIjoiYmxvYl9pZCJ9fQ==--9e7336b29468fe15e9981e55c2c7c7e3e8df2251/image.png)
This is for the inmp441 mic module. 
Connections:
SCK - GPIO41
WS- GPIO 42
SD -GPIO2
L/R ; selcted left with gnd


Added a bypass capacitor(0.1uf) as recommended by the datasheet and articles for a clean signal.

<!-- Uploading image.png (29 KB)... Processing... -->
The is for the amp and the DAC module. I have not connected the gain to anything becasue its the default and increasing it might casue some distortion as suggested by Claude. So ill just stay at 9db.

Now i have to wire the camera.
https://ar.aliexpress.com/item/1005004471654205.html?spm=a2g0o.productlist.main.3.2aeb0uOf0uOfba&algo_pvid=89c5adb3-60d1-44cf-ba85-5f3eab1174db&algo_exp_id=89c5adb3-60d1-44cf-ba85-5f3eab1174db-2&pdp_ext_f=%7B"order"%3A"72"%2C"eval"%3A"1"%2C"fromPage"%3A"search"%7D&pdp_npi=6%40dis%21USD%219.95%219.95%21%21%219.95%219.95%21%40212a70c117745103471605831e5878%2112000029283148367%21sea%21AE%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A6924c055%3Bm03_new_user%3A-29895&curPageLogUid=Nq2pZIp5P0Cb&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005004471654205%7C_p_origin_prod%3A
But i cant find any resources for this module at all. 
https://community.element14.com/products/devtools/stm32f4-discovery-expansion-boards/f/forum/29882/ov5640-camera-via-dvp-interface

Found this and this
https://learn.adafruit.com/adafruit-ov5640-camera-breakout/pinouts

And from the element14 page, claude figured out the pinout. So ill go with. There is no crystal oscillator signal needed as the board already has one. One less gpio used!

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0OCwicHVyIjoiYmxvYl9pZCJ9fQ==--dd9f8dd1d2a14ede19a3c79ffc35c91395d9806d/image.png)

I connected the pins to the gpios. Havnt connected any resistors (pull down resistors on SDA and scl) im just hoping the board has those (there are soldered resitors but idk if they are for those pins)

The pinout is as follows:
D0 - GPIO19
D1- GPIO14
D2 - GPIO20
D3-GPIO16
D4-GPIO21
D5-GPIO3
D6-GPIO46
D7-GPIO5
SCL- GPIO8
SDA-GPIO9
PCKL-GPIO13
PWDN-GPIO47
VS-GPIO6
HS- GPIO7
NC - not connected
RST- GPIO48


I am trusting claude with this. :)
I dont have resources to double-check with. And there is no info provided by the retailer in aliexpress.

I need to add a tft sceen now and then thats all there is to do.
Camera is done
Mic is done
Speaker is done
Power is done
Tft needs works. Some leds. Some switches (for controls) and yup itll be done.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/xBs_2awJvuVG/timelapse-xBs_2awJvuVG.mp4

## Entry 6
- ID: 568
- Author: Manish
- Created At: 2026-03-28T08:03:58Z

### Content

What i just remembered is .. i need a sd card module 😭.. i totally forgot about the storage stuff.
The plan is when the user records a video, it stores the information/content in the sd card and later begins the upload to their online account (im gonna build a custom website for this thing :) ). So for the sd card module Ill go with the adafruit one. It comes for like around 3-4bucks.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MiwicHVyIjoiYmxvYl9pZCJ9fQ==--2a7eeedd8eb57aef2f76be9b6b4070ee4e74748f/image.png)

These have a lot of pins requirement though.

But these have just 6 pins 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI5NCwicHVyIjoiYmxvYl9pZCJ9fQ==--17d839001aef18fd23b7f06f930fa32927bc0b96/image.png)
And are much more cheaper.

The difference is on the quality and the speed of transmission. I need faster rate of data transfer so Ill go with the adafruit one.

There is a critical problem right now. I still need GPIOs for sd card and tft with some additional LEDs and buttons for input. And im running low on free gpios. Either i have to use another esp or use a gpio expander like the MCP23017.


Hmm this is tough. never used a gpio expander.

For the sd card I found the schamtic and the footprint.
https://www.snapeda.com/parts/MicroSD%20SPI%20or%20SDIO%20Card/Adafruit%20Industries/view-part/

For the tft screen.. I found the resources for the adafruit model but not my clone. Ill just go with what i have. Its 2inch anyways so shouldnt be an issue. (lets hope)
https://www.snapeda.com/parts/4311/Adafruit%20Industries%20LLC/view-part/?ref=dk&t=2inch%20tft%20spi%20display&con_ref=None&ab_test_case=a
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMwMCwicHVyIjoiYmxvYl9pZCJ9fQ==--c14c97a7f71f02eba9d4d384e129ace87db91d64/image.png)
This is the tft screen im going for. 

Imported in kicad:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMwMSwicHVyIjoiYmxvYl9pZCJ9fQ==--9b74484becb0bfdb91e1938ff8fcbf2c51523e06/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMwMiwicHVyIjoiYmxvYl9pZCJ9fQ==--b3cc90e74974e041bcc6f9fc190d2f7bec31d48c/image.png)
There they are:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMwMywicHVyIjoiYmxvYl9pZCJ9fQ==--0f0de143020e81dea2184e3d85a8e9f18c2a2d95/image.png)

now i need figure out the gpio problem.

I read this article from instrcutable:
https://www.instructables.com/IO-Expander-for-ESP32-ESP8266-and-Arduino/
And other articles. BUt they all seem to be using modules from different companines. One popular is the Adafruit PCF8575 . And i asked claude and it suggests me to just go with the chip. The setup is not that complex. With a few genral components required only.

I added the diagram:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMwNiwicHVyIjoiYmxvYl9pZCJ9fQ==--55d95ebe7e9b8b844ee0007ad4b8fb3460794b31/image.png)
It was in the kicad default libarary. I choose the IC socket type where you can pull it out if needed.  (DIP socket type)

<!-- Uploading image.png (22 KB)... -->

I have shared the clock signals from the cam to the expander chip. And added one interrupt at GPIO 18 for the capture buttons and record buttons (and who knows what ) for later. now we have a lot of gpios for leds and buttons :)

There are a lot more pins int the Adafruit model than in the TFT I'm using so i need to edit the symbol.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMwOCwicHVyIjoiYmxvYl9pZCJ9fQ==--39fd1b81ff31eca359be5e96a19b565361ce2f3f/image.png)

I edited the symbol, and now it matches the one im going to order. The larger number of pins is prbably due to the sd card on the screen for the adafuit one. Mine doesn't need one and doesn't have one.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMxMiwicHVyIjoiYmxvYl9pZCJ9fQ==--34c388948b1b0719a8497a18d636a448a0d89aec/image.png)


So here is the plan. By going back and forth with cluade. We managed to make the GPIO exactly enough for the setup. The tft and the sd will not share the clock because I don't want them interfering at all under whatever circumstances. If lets say the sd card doesnt work. then the tft will not have any issues because of that and i can just make the content upliad directly through wifi. Just making the design foolproof.

Im leaving out the 2 data pins on the SD card.. so there is that. I dont have enough gpio pins to connect them to. So 2 data pins should work decently ig.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMxMCwicHVyIjoiYmxvYl9pZCJ9fQ==--b6e2cbe47d1b133bb7f9cf299c332d440353d766/image.png)


now that all the other componenets are done. LEts do some work on the leds and input switches.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMxMywicHVyIjoiYmxvYl9pZCJ9fQ==--3da236ad7ecfd34d15e25d735da727399b5c89b2/image.png)

I added three leds or three different colors. Gods know what im going to using them for . But definetely going to use them. For example - when the uplaod to the website  is done the green led lights up and turns off when the user presses the okay dialog prompt. Something like that for all of them,
Im thinking of using these capacitance input buttons - ttp223. Theyll give a whole new feel to the device. And iknow excatly where ill use them. For going through a list - lets i want to see all my photos/memories.. then ill press on one tpp223 for forward and other for backward. And there no button at all. It jsut underneath the case!

These ones:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMxNCwicHVyIjoiYmxvYl9pZCJ9fQ==--e4537c07afaf465555e3404e279c4e7ab591751d/image.png)
They are not that expensive as well. And they dont require extra gpios too. So ill go one for a latching switch to begin recording/take a pic and whatnot (itll bemetal so it gives a premium feel) And the rest two input will be the ttp223 modules.

There it is:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMxNSwicHVyIjoiYmxvYl9pZCJ9fQ==--2a8188fd00df603cb70547b4072295e8c912ce48/image.png)

The first 3  pins of the gpio expander will be output for the led and the bottom 3 will input from the switch.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMxNiwicHVyIjoiYmxvYl9pZCJ9fQ==--9f28213b4771b31913afb8d439e788212f4c77e9/image.png)
3.3k is too high... i got ahead of myself. 330 is alright and normal.


I think  we are done?

Actually the reset and the boot needs work.
The reset and boot both needs to be pulled low for dowload mode. Normally they are high.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMxNywicHVyIjoiYmxvYl9pZCJ9fQ==--f336a0d425b0f8d7179af879b3e5910776a46bab/image.png)

And thats done. When the button is pressed the gpio is pulled low.


This is our shcmatic as of now.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMxOCwicHVyIjoiYmxvYl9pZCJ9fQ==--a5fea559b074150d095da55587466334ea22d16b/image.png)

I now need to assign footprints to the rest of the components.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMyMSwicHVyIjoiYmxvYl9pZCJ9fQ==--43251820428ff2700e23ee6ee27c0adc72509f08/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMyMywicHVyIjoiYmxvYl9pZCJ9fQ==--e2f7b848d2632783f6a9c02843d0e301bb81715a/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/Ur4gUrlVHd5w/timelapse-Ur4gUrlVHd5w.mp4

## Entry 7
- ID: 595
- Author: Manish
- Created At: 2026-03-28T17:09:06Z

### Content

Now I need to assign the footprints to the components and get it all setup for tracing.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM2NywicHVyIjoiYmxvYl9pZCJ9fQ==--edd166a212725dc942ff43cec08b8928e5e25985/image.png)
The pin order was messed up so i fixed it.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM2OCwicHVyIjoiYmxvYl9pZCJ9fQ==--abaf02addaa92a50c68bec6e7e84a0dfb4f83962/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM2OSwicHVyIjoiYmxvYl9pZCJ9fQ==--28396e397f8181a5eac9b945b2dd5539ece65eef/image.png)
Fixed the footprint for the tft screen aswell. (reduced the extra pins we had)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM3MSwicHVyIjoiYmxvYl9pZCJ9fQ==--581cfd6585d0441821a4446b0f2d5fa059e51867/image.png)

All the footprints are assigned.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM3MiwicHVyIjoiYmxvYl9pZCJ9fQ==--81eb24870c98e45be6214be5279aa84bedc11e75/image.png)
No error :)

Updated the 4 pin footprint for the switch to 2 pin momentary switch one:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM3MywicHVyIjoiYmxvYl9pZCJ9fQ==--4bb24136f0f832b4ed10832e2b7c40de2c3e55dd/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM3NCwicHVyIjoiYmxvYl9pZCJ9fQ==--d942802ce4b915dd0fff87e97d48b7208c278785/image.png)

To get an idea and the dimensions of the device.. i arranged the components wherever I see them fit. And this is how they turned out
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTM3NSwicHVyIjoiYmxvYl9pZCJ9fQ==--0e82c9b8cb5aa3a148eab737e4f4100c3848d908/image.png)
I dont have the ov5604 camera module's 3d modle though. Its alrihgt. Next journal.. ill properly order the componenets and begin routing power.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/G_R5L1GAg4XB/timelapse-G_R5L1GAg4XB.mp4

## Entry 8
- ID: 705
- Author: Manish
- Created At: 2026-03-30T13:00:44Z

### Content

Looking at the schematic, I figured there should be some decoupling capacitors for power near the 3.3v pins of the esp. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU3OSwicHVyIjoiYmxvYl9pZCJ9fQ==--077011bfd2005f8d652f07ad84d7b735a42aec21/image.png)
Even though there are multiple capacitors in the vout of the boost buck converter. I asked claude and it's necessary as I guessed.

So i added two. One for low frequency and the other for high frequecny noise.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4MCwicHVyIjoiYmxvYl9pZCJ9fQ==--6f2c92d73269805fc2fe533f54d8766cfaf6e9de/image.png)

These will remain close to the 3.3v pin of the esp.



Due to size constraints I need to put a few components on the back of the pcb. I made a query to claude and evything should be fine. and anyways Ill do a sanity check  by someone in slack.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4MSwicHVyIjoiYmxvYl9pZCJ9fQ==--6845c726835cd51d3ad8f29e40339ad9dd05794b/image.png)
I got a jst connecter 3d model (it was missing idk why )
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4MiwicHVyIjoiYmxvYl9pZCJ9fQ==--6997028bec69569665dc585a0d35b21c510fa9f8/image.png)


Edited some footprints coutyard and outline so that it allows me to arrange the components properly.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4MywicHVyIjoiYmxvYl9pZCJ9fQ==--8d24e290e703bd85c81a466b119531db36d0fd8e/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4NCwicHVyIjoiYmxvYl9pZCJ9fQ==--1769269675d913ecb8f8852fd56698b4e168ec3c/image.png)


I added two more buttons. Becasue i feel like I'll need them. And I can't just rely on the touch capacitance ones.. what if they dont work reliably? So just to be safe ill put two more momentary switches in the same rail (B) where I have hooked up the interrupt. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4NSwicHVyIjoiYmxvYl9pZCJ9fQ==--d7a0c195abe961d6ef6527029f724f94a98bce28/image.png)

Now that I mentioned that ... i checked and its hooked up in the A intercept pin. I need change the intercept pin to B.



And i need to do something about the momentary switches for the enable and boot. They are just too big.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4NiwicHVyIjoiYmxvYl9pZCJ9fQ==--d2ac1d707712672e75f156511c65627c47d930c2/image.png)

I changed the footprint for them and this is much better.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4NywicHVyIjoiYmxvYl9pZCJ9fQ==--62c508f8e6da4f3a6fb3a7d6dea2348a44fed93c/image.png)


Im chaging up the positions of components and figurin out where to put what.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU4OCwicHVyIjoiYmxvYl9pZCJ9fQ==--50ee0ce34948605940c7583f8fdaaf1a57bf226c/image.png)
I mistakenly  set the footprint of a resistor to this:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5MCwicHVyIjoiYmxvYl9pZCJ9fQ==--9ce491245a009820d6860f3bbb629e099b0dc984/image.png)
So i changed it!


so im grouping all the components  based on their category,
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5NywicHVyIjoiYmxvYl9pZCJ9fQ==--8a06e825fa83360a4f239e6c66a45f3b5cf24959/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5OCwicHVyIjoiYmxvYl9pZCJ9fQ==--af5647d322dc4fd608819cc87e259a61092893e5/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU5OSwicHVyIjoiYmxvYl9pZCJ9fQ==--1932b93a7c99ed8ec9bf148ec542638067664338/image.png)
And there it is .. all completely arranged.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMCwicHVyIjoiYmxvYl9pZCJ9fQ==--ae8264a72f95ac2ee78e4dc5624d173d31fdea07/image.png)


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMSwicHVyIjoiYmxvYl9pZCJ9fQ==--e4c36f7ca71c83d02112924154c9f3dab40a87c0/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTYwMiwicHVyIjoiYmxvYl9pZCJ9fQ==--470519023efd5a7ceb698578945af7c2dc813fae/image.png)

The dimensions are : 115.7mm * 79.1 mm

That is alright, I'm happy with it, The only thing im concerned about are the footprints. This will be my first time ordering SMD components. And Im paranoid that some might be too big and some too small for the components to be soldered on. Ill ask that in Slack maybe tomorrow.


### Recording Links

- https://public.lapse-hackclub.link/timelapses/1jc-eikASPak/timelapse-1jc-eikASPak.mp4

## Entry 9
- ID: 790
- Author: Manish
- Created At: 2026-03-31T13:33:59Z

### Content

To make it easier to source parts and opt for JLC PCBAservice.. I need to change all the footprints for all the general components to "0603" named ones. Thats the standard as suggested by a fellow hacker in Slack. And ill go with that advice. And there it is, I found it.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc2NSwicHVyIjoiYmxvYl9pZCJ9fQ==--00f89ee3daad946869d38e34f244ffdc78320560/image.png)


I changed all the general parts with that tag. And lets go tracing :)


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc2NiwicHVyIjoiYmxvYl9pZCJ9fQ==--8fb7939ea067e932ade5f9e42419a24286dabde4/image.png)
Defined the sizes.

First the decoupling caps.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTc2NywicHVyIjoiYmxvYl9pZCJ9fQ==--e11467b937d8fc98b15dc6976b9dcf282cda6281/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/S7r8BTSa-2Kl/timelapse-S7r8BTSa-2Kl.mp4

## Entry 10
- ID: 877
- Author: Manish
- Created At: 2026-04-01T16:00:40Z

### Content

I totally forgot about the Data pins and now Im out out og GPIOS in the esp. To resolve the GPIO issue.. I need to redo the shcmatic for some pins. Pins which are not timing critical. I'll connect them to the GPIO expander, which will leave valuable gpios for the peripherals.
And i need to make sure I connect the D+ and D- to the correct GPIOS.

The pins remapped:
AMP_SD.. this is not timing critical. (Just there to enable or disable the amp)
CAM_RST - simple state type signal
TFT_RST - simple state type signal
CAM_PWDN - power on/off camera


And there is is. Free GPIOS!.

D0 and D2 is connected to GPIO 45 and 46.

Now lets go back tracing.

I tried learning differential pairing for the data lines of the usb. BUt it all went over my head. Ill just do them manually, and it's just 2 traces. Ill have to learn that later for some other project or when I have some free time. :)

<!-- Uploading image.png (24 KB)... Processing... -->
I am doing the charging side of things. I noticed just now that there are 14 pins in the footprint while there are only 11 connections in the symbol.

That is not a problem. Its just that some pins had two pin pads. I did some tracing and thats pretty much it. Managing the trace width is touhg when the pads are very close together.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk3NCwicHVyIjoiYmxvYl9pZCJ9fQ==--30a07abc70f89e2d50bb7f9b23f99001173e1ff4/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/tc1BF-7RuEuU/timelapse-tc1BF-7RuEuU.mp4
- https://public.lapse-hackclub.link/timelapses/bKMoAXSzFaut/timelapse-bKMoAXSzFaut.mp4

## Entry 11
- ID: 1301
- Author: Manish
- Created At: 2026-04-06T05:49:52Z

### Content

I did the power circuit before. Now lets go to the rest of the ciruit. Frist we ll  do the charging part. Or should i first do the signals? I think that ll  be better. So that i dont have to put vias for the signals.

First lets do the sd card module.


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg0OCwicHVyIjoiYmxvYl9pZCJ9fQ==--41048c22b81e142baa0c3f7ed37a2201a6faf22d/image.png)

There is an issue though. The data routes are blocking me to route the entire left side of the esp32 chip. I also cant use vias for spi signals. So i need to figure out another way to route the data pins.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg1MSwicHVyIjoiYmxvYl9pZCJ9fQ==--4af0b62c090661ac08721060cb460942557a3fe4/image.png)

So what i figured out is, I can make do with 0.2mm for the data pins so that i can route them together through the small gap between the pins and the antenna. This way the pins on the left side is not blocked and free to route to.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg1NCwicHVyIjoiYmxvYl9pZCJ9fQ==--a86783bf4ef67444a0e3f8e34b6452466c763a9d/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg1NSwicHVyIjoiYmxvYl9pZCJ9fQ==--ba7a2ca25b70bb15b16df94194f80a672912f60a/image.png)


Now thats done, I can route the signals safely.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg1NiwicHVyIjoiYmxvYl9pZCJ9fQ==--7d536271ad06916b5dc890d01ee33c0ce61cc8c7/image.png)

Now for mic module:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg1NywicHVyIjoiYmxvYl9pZCJ9fQ==--12f782d6649131f6222798bfca272c681cc8c55c/image.png)
I  first route the sck and ws signals because they needs to have signal integrity and shortest legnth as possible.

As the mic and amp the clk signal I just connected the amp signals to the mic ones.
Now lets do the camera.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg1OSwicHVyIjoiYmxvYl9pZCJ9fQ==--7580a9bee6e6852b1c012c9e2af7de901e845de4/image.png)

First the most sensitive pins. But for me to route to the pin with just one via .. i will have to have approx 110 mm of trace. Thats not very good for clk signal.
I need to find a shorter path...
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg2MCwicHVyIjoiYmxvYl9pZCJ9fQ==--132f15c40e843e0ab8aeb8280a2d0f47ef0d5368/image.png)
Using two vias is also fine. So i used two vias and now the trace is much shorter.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg2MSwicHVyIjoiYmxvYl9pZCJ9fQ==--f8a9533895039c232025aaf96f349d46f8075ca8/image.png)

Now all the pins (signal ones) are routed. The most vias I have used is just 2 which should be fine. Ill route the gpio expander pins ones later, they can have multiple vias and have no problems.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/fA_E5Vxu9SCW/timelapse-fA_E5Vxu9SCW.mp4

## Entry 12
- ID: 1330
- Author: Manish
- Created At: 2026-04-06T14:55:51Z

### Content

OMG. :(
I made a mistake... I made the connections as if the mic module was on the underside of the PCB (b.cu layer). I need to fix that.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg3MSwicHVyIjoiYmxvYl9pZCJ9fQ==--0b309703c22dd285d53bf7dd11649b3c5a8fb14b/image.png)

Fixed it 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg4MCwicHVyIjoiYmxvYl9pZCJ9fQ==--dc97de4190e0b413ce832e9e06ea6bae7a19202d/image.png)

Fixed the connection to the amp as well.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg4MSwicHVyIjoiYmxvYl9pZCJ9fQ==--2a6185c590d62c60a34fd077d5e5dc986ed26466/image.png)

For the TFT SCL signal connection, I can't find a way to keep the route <80mm. The shortest length I have managed so far is 107mm, which is not very good for SPI signals.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg4MywicHVyIjoiYmxvYl9pZCJ9fQ==--5dcf151e8b5d5024a5b9bab44f49af24f781260f/image.png)
One reason is that the TFT pins are all the way across the board. And the board width is around 90mm itself.

This is what Claude says - "You're honestly in good shape. ST7789V is very commonly used with ESP32 and tolerates imperfect routing well in practice."
And i think it'll be okay.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg5MiwicHVyIjoiYmxvYl9pZCJ9fQ==--901ff40adc29dd71d4ee56f557b1f569d910a046/image.png)
Added this 33 ohm resistor to compensate for the length.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg5MywicHVyIjoiYmxvYl9pZCJ9fQ==--d990b35928703a3e0bce6b1f8ea172e279649f35/image.png)
Now the signals should be fine.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkxNywicHVyIjoiYmxvYl9pZCJ9fQ==--066c384d3c295197e7f8661af7d8b054e43aeb57/image.png)
All the pins are now routed for the display.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkxOSwicHVyIjoiYmxvYl9pZCJ9fQ==--26f853a4bf9d65192505191c116ccb72a43f28db/image.png)
I routed the scl and sd pins for the GPIO expander and routed some of the module pins.


Connected the switches.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkyOCwicHVyIjoiYmxvYl9pZCJ9fQ==--14a4305033e502b475ac393b31560dbd5252ce52/image.png)

And the ttp223 capacitance touch button:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkzMCwicHVyIjoiYmxvYl9pZCJ9fQ==--4187acbe2f466ef5412c00125459e1f79115616a/image.png)


I changed the footprint to MX switches instead of a pushbutton and then routed again.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkzNSwicHVyIjoiYmxvYl9pZCJ9fQ==--42c93e10db371094be3048c1e10e5774af8d0b21/image.png)


Did the en and boot buttons with their capacitors and resistors.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkzNiwicHVyIjoiYmxvYl9pZCJ9fQ==--08a7c02f359460c45c36532b0a381fb4f016db79/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkzOSwicHVyIjoiYmxvYl9pZCJ9fQ==--cd30e00a0802727dae9dfb7da3db6599a4ca16fe/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/NNWLjfov7HUF/timelapse-NNWLjfov7HUF.mp4
- https://public.lapse-hackclub.link/timelapses/WH4sSvl2SfX0/timelapse-WH4sSvl2SfX0.mp4
- https://public.lapse-hackclub.link/timelapses/A0MiM6Ac3z9Z/timelapse-A0MiM6Ac3z9Z.mp4

## Entry 13
- ID: 1388
- Author: Manish
- Created At: 2026-04-07T05:22:57Z

### Content

Routed the leds:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA3OSwicHVyIjoiYmxvYl9pZCJ9fQ==--291d8f9886c2b5be85a69402f60bd6ddf1d89177/image.png)

With that, all the traces for the components are routed. Now I need to do the battery part. I kept it till the last as I can have multiple vias and its not sensitive as component signals.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4MiwicHVyIjoiYmxvYl9pZCJ9fQ==--0a7ee69cd2f20c1d00aa0e291ac6d99135a20ad4/image.png)
This is the charging circuit. It needs to conduct around 1 amp of current to the battery. I have set the width of trace to 0.8mm and the via diameter and hole to 1.4 and 0.8mm.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4NCwicHVyIjoiYmxvYl9pZCJ9fQ==--b04202fb660f41d69aab7ae65b2ed32447934b2a/image.png)
Routing the 3.3v power rails.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4NiwicHVyIjoiYmxvYl9pZCJ9fQ==--6ec2f72a496a474c910b9dbc277c5ba93220d6b4/image.png)


Routing the other left-out pins:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4NywicHVyIjoiYmxvYl9pZCJ9fQ==--ffa7d23bcaa1f9658755c122b7de314890b86bc3/image.png)


I think Im done with routing:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4OCwicHVyIjoiYmxvYl9pZCJ9fQ==--a2e85b123ea567b1334c88e457f4e9cee618f5ea/image.png)

I resolved some of the issues. Most of the errors are regarding clearance.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4OSwicHVyIjoiYmxvYl9pZCJ9fQ==--9b9238f199bed7d9b2a372349f2aff5e4e3eb548/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5MCwicHVyIjoiYmxvYl9pZCJ9fQ==--4c05543ace82e847241c461a3b745de407e94bd6/image.png)
And this is what it looks like.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/CDrsKdclF5Dq/timelapse-CDrsKdclF5Dq.mp4
- https://public.lapse-hackclub.link/timelapses/61N_hln1dkUU/timelapse-61N_hln1dkUU.mp4

## Entry 14
- ID: 1393
- Author: Manish
- Created At: 2026-04-07T07:28:35Z

### Content

I resolved all the issue I could and now Ill do the ground pour.
There is a problem. The gnd net is not appearing for me to select it and then do the ground pour. I did the ground pour with the boot net but it doesnt seem right. Idk. I want the net class to be named gnd and not boot.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5NSwicHVyIjoiYmxvYl9pZCJ9fQ==--a2ffef6858050d73d831defe3bf36237a798b166/image.png)
I think its because of this. The gnd is directly connected to BOOT so kicad has renamed the net to BOOT or something like that.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5NiwicHVyIjoiYmxvYl9pZCJ9fQ==--dddea07bc8dc34f2df6dd99f44fc636209c02c7a/image.png)


Now its showing the gnd net. My suspicion was right. The issue was there was a direct connection between the pwr symbol and a net label and the net label became the one that was displayed.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5OCwicHVyIjoiYmxvYl9pZCJ9fQ==--efef73d3f011577ac85e8dfbbbc6a5a5b6968a4d/image.png)
I had to make changes to the en circuit aswell as it was also making a direct connection with the gnd net.


I did the copper fill and there are still a ton of issues.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5OSwicHVyIjoiYmxvYl9pZCJ9fQ==--e61243b3e34036fac49e5a29fa9362116dba8eca/image.png)
I don't really understand this issue. its connected wdym mean its not?



### Recording Links

- https://public.lapse-hackclub.link/timelapses/8-IWNVtRan76/timelapse-8-IWNVtRan76.mp4

## Entry 15
- ID: 1461
- Author: Manish
- Created At: 2026-04-08T06:00:37Z

### Content


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzIyOCwicHVyIjoiYmxvYl9pZCJ9fQ==--8739a860cf5af31a61fd23f96f3c7ac4936de55e/image.png)

There were some issues with the connection of en and boot pin. In hindsight, I connected directly to power when GPIO0 and pin 3 were supposed to be hooked up to switches. They are connected to the 3.3v net in the schematic, which confused me.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/6GrZIqtt2DdN/timelapse-6GrZIqtt2DdN.mp4

## Entry 16
- ID: 1886
- Author: Manish
- Created At: 2026-04-12T07:42:35Z

### Content

So after a few days not doing anything Im back :)
I asked in slack and on Discord about the issue, and all of them recommended me to redo the whole routing part.. So ill just do that then.

Someone suggested me to take 3.3v to the bottom layer through a thick trace and from there route power.
Ill do that as well.


I tried importing the schematic and footprint for a smaller footprint than I have for the GPIO expander. But I couldn't. I got it from the sourcing part website of jlc pcb and it only offers easy eda. And i cant export kicad files from there. And the files i did export(Altium Designer) I cant import in kicad Im going to use what I have -the ic scoket.

I redid the layout.
 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzk5NywicHVyIjoiYmxvYl9pZCJ9fQ==--2d03f41f52091e6dfbb8e6037e419b495ecaf037/image.png)
The new layout doesnt have power and the esp32 close together. So that's very good.

I made changes and grouped components together for a specific purpose.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDAwMSwicHVyIjoiYmxvYl9pZCJ9fQ==--e28f6f70f99e86688269a167fae66c379d557dee/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDAwMiwicHVyIjoiYmxvYl9pZCJ9fQ==--8ab7fe04b523c7a788e34148ee6bb6364d4fdcc2/image.png)

Now its time to route. First lets do usb and one thick trace of power and then to the signals.
<!-- Uploading image.png (46 KB)... Processing... -->
Usb data pins. Both are around 46mm. I had to shift the USB because of the length constrain of d+ and d-. If it was on the other side of the board the data traces will cross 100+mm which is bad.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDAwOCwicHVyIjoiYmxvYl9pZCJ9fQ==--25bea5583e1f75460f62c63d0782bedb5610335b/image.png)

THe battery connecter and the switch which controls it is in the bottom part of the pcb.

I have to do the same for the boost buck converter - 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDAwOSwicHVyIjoiYmxvYl9pZCJ9fQ==--647c4afba8488b6f48619e986e0b45e10b904abb/image.png)

So that 3.3v source is on the bottom of the pcb.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDAxNiwicHVyIjoiYmxvYl9pZCJ9fQ==--f4e10fd04049a91f2e4fba1d2112e4be78ba5319/image.png)

Okay now we have 3.3v on the bak of the board.

All the thick power traces are on the back :)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDAxNywicHVyIjoiYmxvYl9pZCJ9fQ==--6558216e83874d3fe216eabb7b1c8c76a517a70e/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/Xw2o7pK-mjAZ/timelapse-Xw2o7pK-mjAZ.mp4

## Entry 17
- ID: 2012
- Author: Manish
- Created At: 2026-04-13T08:19:54Z

### Content

Continuing routing.

The signals are impossible to route without a via after a couple of traces are drawn.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI3NSwicHVyIjoiYmxvYl9pZCJ9fQ==--79ccb4a56ded9e730e46330590a282dccd289e95/image.png)

Honestly looks very similar to what I had earlier. idk if this is gonna work :(

There was an error with the en and boot pins.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI4MCwicHVyIjoiYmxvYl9pZCJ9fQ==--ea1429f53ee6b6c9ab3bf7ebdc3ec6504b4c5e0c/image.png)
This is wrong. And connects directly to the 3.3v net.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI4NSwicHVyIjoiYmxvYl9pZCJ9fQ==--c5e6689c97c265c24973315e26833f938878bf78/image.png)
I fixed it.
And this is how its coming out.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI4NiwicHVyIjoiYmxvYl9pZCJ9fQ==--20a284a834b5f560bdf691e2444a4c835b3f3037/image.png)

The charging circuit.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI4NywicHVyIjoiYmxvYl9pZCJ9fQ==--22da6aadd6be0d5dd4c735008471d3e75f97d191/image.png)

I think im done with the routing,
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI5MCwicHVyIjoiYmxvYl9pZCJ9fQ==--b5a9a5e6ff53205a995bd5af2e918b710a9638ce/image.png)


This is how it looks
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI5MSwicHVyIjoiYmxvYl9pZCJ9fQ==--5b3f55521e77e17c2cf6c24b131c62f2a14e1310/image.png)
There are like 14 unrouted connections that i gotta fix and about 40 or so total errors.... Thats a work for another time. I guess the problem is less worse than before? Adding vias is working for 50% of the unconnected gnd.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/y87k9i4FvDW-/timelapse-y87k9i4FvDW-.mp4

## Entry 18
- ID: 2160
- Author: Manish
- Created At: 2026-04-14T07:55:51Z

### Content

ITs time to solve the issues with the copper fill.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDU1OCwicHVyIjoiYmxvYl9pZCJ9fQ==--da335a2e9d54f2f8aaebef83adc1eb60813ce668/image.png)
Fixed the issue here:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDU2OCwicHVyIjoiYmxvYl9pZCJ9fQ==--dc644f5ca097f81df51d62753cbfeb0b9292f30f/image.png)
Had to shift components somewhat to remove islands.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDU3MSwicHVyIjoiYmxvYl9pZCJ9fQ==--d2a75c4a2ade2eca1f78c34dfaea2322dcf71e77/image.png)
Good progress, guess. The rest of the errors expect for the 3 unconnected gnd- are thermal spokes related.



### Recording Links

- https://public.lapse-hackclub.link/timelapses/nRgXVYi_7gMz/timelapse-nRgXVYi_7gMz.mp4
- https://public.lapse-hackclub.link/timelapses/FT0dfEBG_SRZ/timelapse-FT0dfEBG_SRZ.mp4

## Entry 19
- ID: 2431
- Author: Manish
- Created At: 2026-04-16T07:11:18Z

### Content

FIxing the remaining bugs and finishing up the pcb now.


I realized for the camera module I have been using FCU layer traces to begin routing when they are at the bcu layer. So i added vias at the beginning of all the traces to begin from the bCu layer.

Then i resolved the disconnect issue.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTA2MiwicHVyIjoiYmxvYl9pZCJ9fQ==--e1bf23ba33ba8c537aedcd3df957d28bbf8eae6b/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTA2MywicHVyIjoiYmxvYl9pZCJ9fQ==--1090afaf23d75660669e616e22797207d866a445/image.png)


I have come a long way.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTA2NSwicHVyIjoiYmxvYl9pZCJ9fQ==--590c9c302e1eb0621edc441be8e6860560090fe3/image.png)

One more unconnected gnd.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTA3MCwicHVyIjoiYmxvYl9pZCJ9fQ==--c522163840feb1fa50638b64ddcaf861c798ecb6/image.png)
With the same technique as the one which fixed the other ones, I finished connecting all the islands to each other.


This i how it looks. If slack people say its all good ill finally begin cading.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTA3OSwicHVyIjoiYmxvYl9pZCJ9fQ==--092e2617053cb95cb1ec65e2bbba643a616a837b/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTA4MCwicHVyIjoiYmxvYl9pZCJ9fQ==--3b818effa7dc5129185f49ec9d4b7f3b5680c83e/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTA4MSwicHVyIjoiYmxvYl9pZCJ9fQ==--162427ebf232e8ac8f9541fe7c80a715c38c8c4c/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTA4MiwicHVyIjoiYmxvYl9pZCJ9fQ==--f2ee2697212b5ac15b00351f5818e10f4af81b04/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/rIVJTL-4ODJh/timelapse-rIVJTL-4ODJh.mp4

## Entry 20
- ID: 2537
- Author: Manish
- Created At: 2026-04-17T04:28:41Z

### Content

I think I should now move to 3d modelling the case. I post threads on Slack about reviewing my PCB to sanity check, and it doent seemt o getting too much attention. Guess I have to post it again later. ill lso post it in Discord and see if they can suggest any improvements if needed.

Im going to export the model to Fusion 360 and model on top of it.

I had to create another account because my free trial ran out. And it took more time than it should have.
Well anyways,
I imported the model
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTI5OSwicHVyIjoiYmxvYl9pZCJ9fQ==--cc5dc610605972426718909b6501324d55312cb5/image.png)

The first thing i notice is there are no holes on the PCB for me to mount on the case. And the PCB lacks fillet(it's not rounded - I forgot to redo to that after deleting it the first time around.

Ill have to resolve all that and then bring the model back in fusion.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/3lsvVYy2MFgF/timelapse-3lsvVYy2MFgF.mp4

## Entry 21
- ID: 2541
- Author: Manish
- Created At: 2026-04-17T05:48:40Z

### Content

So i watched some videos and got a fair idea of what i should do. So basically what i want is for the pcb to be elevated fromthe baseplate so that it doesnt damaged the sd card and scratch against the solder on the back of the pcb. For that Ill be using standoffs and nuts to secure it in place. The standoffs will be male to female. The female will go to the mounting holes of the pcb while the male one will poke out of the case to be secured with a nut.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTMwNiwicHVyIjoiYmxvYl9pZCJ9fQ==--89045bacec3b086b9d77661f8da9060780a9ed4b/image.png)
I put 4 mounting holes  -sym- MountingHole:MountingHole_3.2mm_M3 footprint-MountingHole:MountingHole_3.2mm_M3_DIN965_Pad_TopBottom.
Ill be using m3 screws to fasten the standoffs. So 3.2mm is all good!
Added a fillet and this is how it looks
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTMwNywicHVyIjoiYmxvYl9pZCJ9fQ==--05c5efb6968586936ec2e38e6831c9380f439b97/image.png)

THese come cheap
https://www.daraz.com.np/products/50pc-m2-m25-m3-m4-pcb-motherboard-black-nylon-plastic-phillips-screw-bolt-male-female-female-hex-standoff-hexagon-pillar-spacer-i510405883-s2284255938.html?
Ill be getting the one with 20mm to 25mm length so that i have a fair amount of space for the wire to come from the camera module to the header pins to the bottom of the pcb.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTMxMCwicHVyIjoiYmxvYl9pZCJ9fQ==--7de01d34b8fbe3b87a9c87eb1d42e77a4118aa86/image.png)


I got the 3d model for the standoffs aswl!
https://grabcad.com/library/m3-standoff-pcb-spacers-1

I brought it in my project and started making joints.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTMxNywicHVyIjoiYmxvYl9pZCJ9fQ==--f0575b97ee598ae09b4a9a6392bad740ff080c63/image.png)


With that all the spacers/standoffs are inplace.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTMxNiwicHVyIjoiYmxvYl9pZCJ9fQ==--399b1e686c18f7d9132863bf7fa078f6596c7f4c/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/O4yBCTVGq-O1/timelapse-O4yBCTVGq-O1.mp4

## Entry 22
- ID: 2555
- Author: Manish
- Created At: 2026-04-17T09:05:13Z

### Content

Now its time to make the front plate to go with the pcb.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM0MiwicHVyIjoiYmxvYl9pZCJ9fQ==--1106e9fcaf75364eff9e4def40c6613d11ae188f/image.png)

First i did the sketch and then extruded.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM0MywicHVyIjoiYmxvYl9pZCJ9fQ==--b2f352ebb9467032a948a1cdaa835fa9aedc2a7b/image.png)
It looks pretty nasty. Chamfer might fix it ig.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM0NCwicHVyIjoiYmxvYl9pZCJ9fQ==--9ebee71db26cb53f9d582b408cb0b0a6f547b40d/image.png)

I need to make a projection on the one i just extrued so that the pcb can sit inside of the case instead of being sandwiched.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM0NSwicHVyIjoiYmxvYl9pZCJ9fQ==--df07d49e6cc4d1ba0306b6c9b6da099079333827/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM0NiwicHVyIjoiYmxvYl9pZCJ9fQ==--75ebdf6851dc32b9b77c3ae720dc4da083701476/image.png)

This is for the usb
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM0NywicHVyIjoiYmxvYl9pZCJ9fQ==--22251588e44752cef9cb712478e7b97fee490914/image.png)

THese are the touch pads for input.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM1MCwicHVyIjoiYmxvYl9pZCJ9fQ==--7d38a191ed14a52fccabef609fccc18f9cc09cc9/image.png)


And this is how the front plate looks!
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM0OSwicHVyIjoiYmxvYl9pZCJ9fQ==--6c8efb09aac6a41c2dc078ae196bdda0a514fc28/image.png)


Im thinking im might have to change the spacers height from 20mm to 15mm or something. they are too long


### Recording Links

- https://public.lapse-hackclub.link/timelapses/5-yua68Zwj20/timelapse-5-yua68Zwj20.mp4

## Entry 23
- ID: 2563
- Author: Manish
- Created At: 2026-04-17T13:06:20Z

### Content

Now its time to figure out the back part of the case.
For the dimensions of the camera module Im asking the supplier for the dimensions and just hoping they reply.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM2MywicHVyIjoiYmxvYl9pZCJ9fQ==--dc737a382153c352e6d02ee713fe04fbb9b61b4a/image.png)
For now Im just gonna create this at the back and later edit it.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM2NCwicHVyIjoiYmxvYl9pZCJ9fQ==--de337d6be8b26b1da18f90febd0754e0291cda6f/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM2NSwicHVyIjoiYmxvYl9pZCJ9fQ==--16c4b546dd742a57b257f5ecf73f071f34fae10c/image.png)
There was some complication i was facing with the file type in fusion. I selected part instead of hybrid for the backplate. (there was a new update so still figuring out how to use all the constrains)
Then i made a assmebly file to put the backplate and the frontplate to create holes and put them together. I joined them together but i cant create holes. Apparently i can make holes in assmebly files. I need to set it to hybrid and then go on with it.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM2NiwicHVyIjoiYmxvYl9pZCJ9fQ==--181c2c474e2695b44738947bc818cdd839e0fe9f/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTM2NywicHVyIjoiYmxvYl9pZCJ9fQ==--7172d24011b8703ee57e48a1ca3e96356556a9fe/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/VTW43d-3vRuP/timelapse-VTW43d-3vRuP.mp4

## Entry 24
- ID: 2711
- Author: Manish
- Created At: 2026-04-18T13:55:54Z

### Content

So I got a reply from the supplier. And now i can design the camera mount :)

The module's info is here:
https://drive.google.com/drive/folders/1ehE1qqQgoStYUuSYHOSNaoHoHDkWDfHP?usp=sharing

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY3NSwicHVyIjoiYmxvYl9pZCJ9fQ==--16efffa9b1e35a983d1434975982d4a984fd421c/image.png)

This will be like some sort of hand-holding thing. It is really not holding the camera module-itll be attached witha screw. but it makes it intresting i think.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY3NywicHVyIjoiYmxvYl9pZCJ9fQ==--d57937febc8315dd314eed206bcb0b28e0a590c0/image.png)
Absolutely necessary.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY3OSwicHVyIjoiYmxvYl9pZCJ9fQ==--1d40a6cf15123a0d5013800a552c259a86da4884/image.png)

And with that, the case is almost done. I just need to figure out how to add holes in the new update (with components)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY4NSwicHVyIjoiYmxvYl9pZCJ9fQ==--57c9f0285380ec4a383fc4a05b43bed9eca4f6b7/image.png)
The hole type is simple. hole tap type is clearance  and dril point is angled . I have used m3 screws. They go 15mm deep which is couple of mm above the end of the backplate.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY4NiwicHVyIjoiYmxvYl9pZCJ9fQ==--382e4a91c3f86ae9db6066501e2de0442400d7e9/image.png)

These are the 4 holes.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY4NywicHVyIjoiYmxvYl9pZCJ9fQ==--0803fe5bddb2dbeec010e55536161c126beb2f3d/image.png)


oh flippppp. I forgot to make holes on the backplate for the screws that are mounted on the pcb. I have already unlinked the component so ill have to make it here. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY4OSwicHVyIjoiYmxvYl9pZCJ9fQ==--da79fc575200c88090e77a66f91f4c2efeee253d/image.png)
Done!


This is the final model :)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY5MCwicHVyIjoiYmxvYl9pZCJ9fQ==--fb82e2fd96811682638cb54e16461f2f8739131c/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY5MSwicHVyIjoiYmxvYl9pZCJ9fQ==--e1587fee7a6e927266992acade640cad445a5c44/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY5MiwicHVyIjoiYmxvYl9pZCJ9fQ==--83d47a884ee7bf9c1975a0491b39c449698a9802/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTY5MywicHVyIjoiYmxvYl9pZCJ9fQ==--6fd68739f5e1c9a2b60126664f7ac673889b7faf/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/EcUCTrN8ayMz/timelapse-EcUCTrN8ayMz.mp4

## Entry 25
- ID: 2858
- Author: Manish
- Created At: 2026-04-19T12:11:57Z

### Content

Now it's time to design the firmware.
First lets get the tft running.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTk4OCwicHVyIjoiYmxvYl9pZCJ9fQ==--ccb041dad00d054975189a6656a4c98f8e111f23/image.png)
In esp32 we cant install library packages from what i know. This is a library script in a file, and from we import functions for whateever we are doing.

The documentation.
https://russhughes.github.io/st7789py_mpy/examples/hello.html

Created this class
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTk4OSwicHVyIjoiYmxvYl9pZCJ9fQ==--a4d3dcd31f4355b21731060992db3b2400fd5312/image.png)
Which is set to define all the components.. so i can just define the pins and not worry about the initialization at all. This makes the 
whole system modular.


Now thats done lets do the mic.
https://github.com/miketeachman/micropython-esp32-i2s-examples
This is what Ill be referring to.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTk5NCwicHVyIjoiYmxvYl9pZCJ9fQ==--d01fd0d163ccd3dedd31d741485dabe4c5979dcd/image.png)

Now what do i do for the camera?
Claude found me the library to work with the camera. And i think it shoudl work all good.
https://github.com/cnadler86/micropython-camera-API

Might have to install firmware maybe idk
https://github.com/cnadler86/micropython-camera-API/releases

Ill check it out tommorrow. Its really overwhelming when you cant test out the code/firmware in real time. Instead just yolo it and hope it works. Ill not have a good time troubleshooting thats for sure.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/X8D1SpyWOGPh/timelapse-X8D1SpyWOGPh.mp4

## Entry 26
- ID: 3061
- Author: Manish
- Created At: 2026-04-20T15:58:47Z

### Content

It's time to get back at it. We have to figure out the camera initialization.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjM0NSwicHVyIjoiYmxvYl9pZCJ9fQ==--5e7a51021da8b20e089588bd64163b1d7077cdef/image.png)
I'm not sure which init is going to work. The bottom one should be the right one becasue its a custom module, so we gotta define the pins.


Later, after installing the firmware, I gotta work on a lot of stuff- capturing pics, sending data to the custom api of my website. But for now, this will be enought ot get a basic idea of the structure.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjM0OSwicHVyIjoiYmxvYl9pZCJ9fQ==--ee4d281c37622c2fc9d7c96876814986d7d750a0/image.png)
Defined the speaker and the mic.
And thats pretty much it for the components.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjM1MCwicHVyIjoiYmxvYl9pZCJ9fQ==--c9146ca4f1daaa1bb5e41ef523dd92984ac6e784/image.png)
Ahh i forgot about the switches and input components. They are simple. Just one pin.

And later in the main file, we can use asyncio library to check for their states continuously and report back when its high for input.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjM1MSwicHVyIjoiYmxvYl9pZCJ9fQ==--6fa3f07a049b053a90c8f7e965a41889802dcb8d/image.png)
Look at that now. Because we used a class-  integrating and defininig components becomes a whole lot simple.

Oh I completely forgot how i have setup my switches.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjM1MiwicHVyIjoiYmxvYl9pZCJ9fQ==--458895046980bf642b56b8a9c924b4eb9b1e79eb/image.png)

Their values is to be read with an interrupt pin. I cant simply define the pins for inputs. 
TO define the gpio expander... i got help from gemini
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjM1NCwicHVyIjoiYmxvYl9pZCJ9fQ==--62c2749e8421842a38c8edf1bc429b63e92cd79d/image.png)
I hope this works. its an i2c device and it sends a signal and we detech the high state fromt he interrupt pin when its triggered.


Now my plan for the whole device is:
There will multiple pages for the ui.
For example:
For the camera ui-- a spearte page when the user click to go to the camera from the menu. Like an application in a phone.
So for each of those applications/pages we will have a page which can be accessed when a button is pressed or some form of input. This input is detected by the interrupt pin and then reported tto the page handler, which handles the input, which then does what needs to be done based on the input. Lets say in the menu the user presses the left button then the user's inout will be first deteted then sent to the page input handler, which then decided where the user needs to go. IT sounds tedious to code but I really like this setup :)



<!-- Uploading image.png (25 KB)... Processing... -->
This is the ui page logic. I got help setting it up from gemini

In the main.py file

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjM2NSwicHVyIjoiYmxvYl9pZCJ9fQ==--c63922b6dd989a9182c60201670ecb4ac7653e70/image.png)
I defiined the pins for the tft and sd and began defifing the devices.
There is one issue though. The tft rst is connected to the mcp=gpio expander.. and parsing its value to the tft rst pin is hard. We need to do extra stuff to get it working normally.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/kIx1LHjyKyQa/timelapse-kIx1LHjyKyQa.mp4

## Entry 27
- ID: 3228
- Author: Manish
- Created At: 2026-04-21T16:02:12Z

### Content

Its time to get back at firmware. how exciting (not really )


Added this in define TFT

```
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
```

The manual sequence is given by gemini.. Because the tft rst pin is in the mpc gpio expander.. so we cant access it directly.


Setting up the MCP GPIO expander is complicated. I have hooked up the switches/touch sensors to GPB4, GPB6, GPB7 and GPB8..and i need to put an interrupt listener to the interrupt pin to look for their states. Im getting a lot of help from gemini.



With this function i will be able to get the input from the user and use it however i want

```
    
        
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
```



YES !!!
the program is coming together.
So this is how this works.
The file structure is 
**setup.py **-which has the class DefineAllCOmp .. which setups all the mode of communication and the components in the device

**ui.page** - which has the ui stuff like drawing the different pages  - for example the camera page of the deivce needs to have a record pciture/take picture button and a unique layout of ui elements. That is handles by the method inside the infered class of that specific page.


**actions.py** - which has all the actions definiton like taking a picture or recording voice memo. This basically defines how to do the required task. This is callled in the ui.py page where when teh page dtect a valid input which is for a specific taks. for say if i press switch 1 in the camera page that will be record or something (ill set this ) and then the specifc action gets carried out when that button is pressed (Detected by the inerrupt pin)

**main.py** -this is main file which handles the task of connecting everything. Evything passes from here. THis keeps track of the input values, the current page and whats happening.

now my task to deifne the actions and then itll be done! (basic structure and how it will work) Im sure there will be a lot of troubleshooting when i get the compoents and start building it in person.


Gemini came in as an angel. I wont be able to do it without its helpin setting up the mcp input interrupts and actaullly exceuting the idea in a efficient manner.

This is how the actions file are coming out:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjcxNCwicHVyIjoiYmxvYl9pZCJ9fQ==--a1f0eca8b177ef1f6cb2e6f67d748eb5418286d1/image.png)


```
import asyncio


async def takePicture(cam):
    img = await cam.acapture()
    return img


def storeInSd(sd, file, content, text):
    mode = "w" if text else "wb"
    with open(f'/sd/{file}', mode) as f:
        f.write(content)

        
def recordVoiceMemo(mic, sd):
    pass

def playSound(speaker,sd,file):
    pass

def loadPicture(file):
    pass

def callDbToStore(file):
    pass
```



### Recording Links

- https://public.lapse-hackclub.link/timelapses/s_nwKDz209Tf/timelapse-s_nwKDz209Tf.mp4

## Entry 28
- ID: 3515
- Author: Manish
- Created At: 2026-04-23T06:18:08Z

### Content

Okay enough of the firmware. If i have to manage changes (which i have to before submission) ill do it later. Now its time to build the website :)
first ill setup my Supabase DB and auth. Then make a basic layout. Then worry about the api calls from the device.



![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzIwNiwicHVyIjoiYmxvYl9pZCJ9fQ==--ed6d2616025fe02503820c5dd6a83b89ac328892/image.png)
I couldn't come up with a better name than my life for a journelling website ...😓ik im not that creative... ill figure it out later..

Here im setting my sveltekit project. Ill be using Tailwind CSS.. Drizzle for omr.. supabase for db and ts for server-side stuff.

Okay now its time to create the supabase db.
I already have one db for my other project.. so I asked gemini if the free tier can handle the data if there a lot of users (in case). so i thought its best oc reate a different suspbse account altogether. And i did that.
And now I have my db.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzIxNiwicHVyIjoiYmxvYl9pZCJ9fQ==--c5b5cb9bd88ae68a3ae43c264f3b8a205dd2ba30/image.png)
Now setting the db is simple enough but integrating it with the project is so much of a hassle.
I ran into multiple errors. Some were niave ones and some confusing.

This is how it let me finally integrate:
first we install the ssr package from supabase:
npm install @supabase/ssr @supabase/supabase-js  - (i only did npm install @supabase/ssr for the first time around)
then define the ts app types:

```
// See https://svelte.dev/docs/kit/types#app.d.ts

import type { SupabaseClient } from "@supabase/supabase-js";

// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			supabase: SupabaseClient,
			session: Session | null,
			user: User | null
		}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export { };

```

after that, define the .env files vars
the DATABASE URL, PUBIC_URL and the PUBLIC_ANON_KEY - all these can be found on the supabase dashboard.

I used the transaction pooler for the connection string.

Then add this in the hooks : - i got the code from my previous project... it should have generated me a basic hooks file but it didnt when i created a project.

```
import { createServerClient } from '@supabase/ssr'
import type { Handle } from '@sveltejs/kit'
import { PUBLIC_SUPABASE_ANON_KEY, PUBLIC_SUPABASE_URL } from '$env/static/public'



export const handle: Handle = async ({ event, resolve }) => {
    event.locals.supabase = createServerClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY, {
        cookies: {
            getAll: () => event.cookies.getAll(),
            setAll: (cookies) => cookies.forEach(({ name, value, options }) =>
                event.cookies.set(name, value, { ...options, path: '/' })
            )
        }
    })

    const { data: { session } } = await event.locals.supabase.auth.getSession()

    event.locals.session = session
    event.locals.user = session?.user ?? null


    const theme = event.cookies.get('user-theme') || 'blueprint';

    return resolve(event, {
        transformPageChunk: ({ html }) =>
            html.replace('data-theme=""', `data-theme="${theme}"`)
    })
}




```


Before I test the db integration, i have to enable remote fucnctions

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzIzNiwicHVyIjoiYmxvYl9pZCJ9fQ==--bf706cb40425f3ba6e913917a2b9a2800cdc38da/image.png)



Okay now lets try out the db.
This is the schma for a basic user.

```
import { pgTable, text, uuid, timestamp } from 'drizzle-orm/pg-core';


export const user = pgTable('user', {
	id: uuid('id').primaryKey().notNull(),
	username: text('username').notNull(),
	created_on: timestamp('created_on').defaultNow()
})
```


Awsome!

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzIzNywicHVyIjoiYmxvYl9pZCJ9fQ==--8d848b5ba22893f33f2094ec9cb43f9d09592b0c/image.png)
I pushed succesfully.
Now i can work on the website itself (the routes)


There was an erorr. I had defined th experimental feature for async fucntoins inside of kit. Instead it was to be done inside compiler option on the very top.

```
import adapter from '@sveltejs/adapter-vercel';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	compilerOptions: {
		// Force runes mode for the project, except for libraries. Can be removed in svelte 6.
		runes: ({ filename }) => (filename.split(/[/\\]/).includes('node_modules') ? undefined : true),
		experimental: {
			async: true
		}
	},
	kit: {
		experimental: {
			remoteFunctions: true
		},
		adapter: adapter(),
		typescript: {
			config: (config) => ({
				...config,
				include: [...config.include, '../drizzle.config.ts']
			})
		}
	},
};

export default config;

```

Now it works! I got help from gemini
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzIzOSwicHVyIjoiYmxvYl9pZCJ9fQ==--a7784828b4dfd9cbd104d5cf9888384a61fb7262/image.png)

This will serve as the navigation bar.

```
<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<nav class="mt-5 grid w-screen grid-cols-3">
	<div></div>
	<div class="flex w-full flex-row justify-evenly">
		<a href="/">Home</a>
		<a href="/memories">Memories</a>
		<a href="/pictures">Pictures</a>
		<a href="/connect">Connect</a>
	</div>

	<div class="absolute right-5">
		<button class="bg-amber-400 p-2">User</button>
	</div>
</nav>
<svelte:head><link rel="icon" href={favicon} /></svelte:head>
{@render children()}

```

Ill modifyfor it to only show when the user is logged it.
First we gotta return some data from the layout.server.ts file


```
export function load({ locals }) {
    return {
        user: locals.user
    }
}
```

This will return the user data.

This way i can add this if stament to only display the nav when the user is signed in.

```
<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children, data } = $props();
</script>

{#if data.user?.id}
	<nav class="mt-5 grid w-screen grid-cols-3">
		<div></div>
		<div class="flex w-full flex-row justify-evenly">
			<a href="/">Home</a>
			<a href="/memories">Memories</a>
			<a href="/pictures">Pictures</a>
			<a href="/connect">Connect</a>
		</div>

		<div class="absolute right-5">
			<button class="bg-amber-400 p-2">User</button>
		</div>
	</nav>
{/if}

<svelte:head><link rel="icon" href={favicon} /></svelte:head>
{@render children()}

```


Now we need to worry about the login. There are two ways to do this. Actuall three. First is just google auth. Second is just email sign-up. Third is both. And Im leaning towards the third one. 
First lets do the email one.
I create a remote function with a form - this way we can submit the form and call the db directly.

```
import { form } from "$app/server";
import * as v from "valibot"

export const signInForm = form(v.object({
    username: v.pipe(v.string(), v.nonEmpty())
}

), async () => {

})
```



I wrote the form page logic

```
<script lang="ts">
	import { enhance } from '$app/forms';
	import { form } from '$app/server';
	import { signInForm } from '../auth.remote';

	let { data } = $props();
	let confirmPass = $state('');
	let errorMessage = $state('');

	function handleSubmit(e: SubmitEvent) {
		errorMessage = '';
		const form = e.target as HTMLFormElement;
		const password = (form.elements.namedItem('password') as HTMLInputElement).value;
		if (password !== confirmPass) {
			e.preventDefault();
			e.stopPropagation();
			errorMessage = 'The passwords dont match';
		}
	}
</script>

<div class="flex h-screen items-center justify-center">
	<form {...signInForm} use:enhance onsubmit={handleSubmit} class="flex flex-col gap-y-8">
		<label>
			username
			<input {...signInForm.fields.username} required type="text" />
		</label>

		<label>
			Email:
			<input {...signInForm.fields.email} required type="email" />
		</label>

		<label>
			Password:
			<input {...signInForm.fields.password} required type="password" />
		</label>

		<label>
			Confirm Password:
			<input required bind:value={confirmPass} />
		</label>
		<div class="flex flex-col gap-y-3">
			<button type="submit" class="cursor-pointer bg-amber-300 p-2">SignUp</button>
			<hr class="my-5 bg-red-500" />
			<button type="button" class="cursor-pointer bg-amber-300 p-2">Google</button>
		</div>
	</form>
</div>

{#if errorMessage}
	<h3 class="absolute top-5 right-5 bg-amber-700">{errorMessage}</h3>
{/if}

```

Evything is done except the validation.... im facing issues there. I asek gemini and it was not very useful. NOw im trying out what claude does.... i just forgot how to do it:(... 

### Recording Links

- https://public.lapse-hackclub.link/timelapses/eRiMqTKx1qwl/timelapse-eRiMqTKx1qwl.mp4
- https://public.lapse-hackclub.link/timelapses/lViqwDdIDLmt/timelapse-lViqwDdIDLmt.mp4
- https://public.lapse-hackclub.link/timelapses/C7lMvPyUqKug/timelapse-C7lMvPyUqKug.mp4

## Entry 29
- ID: 3560
- Author: Manish
- Created At: 2026-04-23T14:36:26Z

### Content

Currently this is the error Im getting:
405
Method Not Allowed

Idk why...

It says this 

[405] POST /auth/signup
Error: POST method not allowed. No form actions exist for the page at /auth/signup
    at handle_action_json_request (C:\Users\manis\OneDrive\Desktop\mylife\node_modules\@sveltejs\kit\src\runtime\server\page\actions.js:33:28)
    at render_page (C:\Users\manis\OneDrive\Desktop\mylife\node_modules\@sveltejs\kit\src\runtime\server\page\index.js:57:36)
    at async resolve (C:\Users\manis\OneDrive\Desktop\mylife\node_modules\@sveltejs\kit\src\runtime\server\respond.js:603:18)

there is a form action though. The remote function. Maybe its because when the validation is over there is no return statement. But again,, when i tried it on.. the validation for the confirm pass was also not working.

I asked Claude, and it's telling me I have to use a different technique. And so does Gemini. But ill make do with what I have. Ill have the remote fucntion in the same file.


It works!
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzI5NywicHVyIjoiYmxvYl9pZCJ9fQ==--d1fdab59b62e1c80ad39753b283635b2dfef04b0/image.png)
I fixed it on my own. Though idk if its a good solution. But hey it works and thatll do.


oh.. no..
i calle dgetRequestEvent() in client side which is a server side fucntion. I need to get my supabase client to call it on the client side.

I cant do that aswl.... Claude says that. let me check my other project.. im sure this worked somehow.. maybe i called a remote function from inside of the handleSignup


Got it !
Got the response and now its working.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzMwMywicHVyIjoiYmxvYl9pZCJ9fQ==--054d467695be35b29bb3d6cc1af79b1917d108cc/image.png)
I got the auth user in my table as well! Im sure the email was sent. Ill have to send it through my emial  -idk what is that technique called (prob gmail mrcp or smth) ill do that later.

What i did was:
I created a supabase.ts file which has the code to create a borswerside client with the env variables:


```
import { createBrowserClient } from '@supabase/ssr'
import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY } from "$env/static/public"

export const supabase = createBrowserClient(
    PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY
)
```

This way i can access the sigin methods. without the server side fucntions that i used before (getRequestEvent())


Now this should only allow actual users to enter dashbaord page
import { redirect } from '@sveltejs/kit';

```
export function load({ locals }) {
    if (!locals.user?.id) {
        throw redirect(303, '/auth/login')
    }
    return {
        user: locals.user
    }
}
```



I ran into an issue.... i was seeing wether im recieving emials or not. And i was. But then the redirects had to be setup in supabase. ANd put in the urls... but i made a mistake . i put the site url as local:host5731/ .... thats the root folder.... and same for the redirect url... but for the site url it should be without the / - local:host5731 only.
I changed it after claude predicted that lol
And now the emial verification works fine.

NOw i just created the login..

```
<script lang="ts">
	import { supabase } from '$lib/supabase';
	import { redirect } from '@sveltejs/kit';

	let { data } = $props();
	let errorMessage = $state('');
	let loggingIn = $state(false);
	let email = $state('');
	let password = $state('');

	async function loginUser() {
		loggingIn = true;
		const { data: verifiedUser, error } = await supabase.auth.signInWithPassword({
			email: email,
			password: password
		});

		if (error) {
			errorMessage = error.message;
			return;
		}
		return redirect(304, `/${verifiedUser.user.id}`);
	}
</script>

<div class="flex h-screen items-center justify-center">
	<form onsubmit={loginUser} class="flex flex-col gap-y-8">
		<label>
			Email:
			<input bind:value={email} required type="email" />
		</label>

		<label>
			Password:
			<input bind:value={password} required type="password" />
		</label>

		<div class="flex flex-col gap-y-3">
			<button type="submit" class="cursor-pointer bg-amber-300 p-2">SignUp</button>
			<hr class="my-5 bg-red-500" />
			<button type="button" class="cursor-pointer bg-amber-300 p-2">Google</button>
		</div>
	</form>
</div>

{#if errorMessage}
	<h3 class="absolute top-5 right-5 bg-amber-700">{errorMessage}</h3>
{/if}
{#if loggingIn}
	<div class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm">
		<div class="flex flex-col items-center gap-4">
			<div
				class="h-12 w-12 animate-spin rounded-full border-4 border-amber-300 border-t-transparent"
			></div>
			<p class="font-medium text-black">Give me a moment ....</p>
		</div>
	</div>
{/if}

```
Its not that different from signup. It works!

Though im facing issue with one thing.. I want the user to got to their dashboard even if they to to the root url. i tried by keeping returing a redirect in the layout.server.ts file of the root folder but that a lot of redirects so that's not it.
maybe page.server.ts file?


YEA!
That works!


Ahh i forgot to add a custom sql script so that the users get copied to the user table.. supabase handles the users in the authentication table but i want those users to be in my user table as well.
I have it from my other project so ill just copy it from there.! And im not very good with sql anyways.

So i copied it. but the users are not getting to the table.. maybe it will work the ones that are signed after its been added.. ill check that tmr. Supabase only provides 3 emails per hr or day idk.

Im trying to picture what I want for the website to look like.

im so overwhelmed right now... no ideas at all...

Im deciding on wether i should allow for videos to be added. It'd be really, really cool if i could record videos and upload to the web straight from my esp device. but is it possible ? let me ask claude.

oh its very much doable...(or so says Claude) that's awesome!

So then first ill create a web version where users can login and then upload thier content from pc and later worry about the api endpoints.

For that ill need to learn about data buckets and how to handle them.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/c5VXspRgR3FR/timelapse-c5VXspRgR3FR.mp4

## Entry 30
- ID: 3674
- Author: Manish
- Created At: 2026-04-24T05:28:10Z

### Content

It's time to continue figuring out how to let users enter their images and videos.
But first lets check how is our  work from yesterday holding up.
Okay there was an small issue when loggin in.
I put redirect in svelte file which is a server side fucntion. I then used goto to fix it. Now it all good.

Now lets work on the file buckets system.

Okay, figured it out eventually. got a lot of help from claude. MOst of it was debugging.
The things that I needed help in:
Setting up proper input field fpr img upload. For image preview when uploading (to create a temp url) and creating bucket policy.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzU3MCwicHVyIjoiYmxvYl9pZCJ9fQ==--c1c2f4c9d6718a111d78a7b90c3835eeffa86e79/image.png)

This are the policies that resolved mt issue. I thought if i have no policy then its alright for testing just like the tables. But turns out i need policies to access or insert files.

```

<div class="m-4 flex h-[400px] justify-center bg-amber-600">
	<input
		class="h-full w-full"
		type="file"
		accept="image/png, image/jpeg"
		disabled={uploading}
		onchange={handleImagePick}
	/>

```
This will get the image and trigger handleImagePIck 

```

	function handleImagePick(e: Event) {
		const input = e.target as HTMLInputElement;
		const file = input.files?.[0];
		if (!file) return;

		selectedFile = file;
		preview = URL.createObjectURL(file);
	}
```

Which will store the file in a variable and create a preview url.
	{#if preview}
		<img src={preview} alt="preview" class="h-full w-full object-cover" />
	{:else}
		<span class="text-white">Click to pick an image</span>
	{/if}

which is then displayed if the preview url exists.

{#if selectedFile}
	<button onclick={handleImageUpload} disabled={uploading} class="cursor-pointer bg-red-200 p-2">
		{uploading ? 'Uploading' : 'Upload'}
	</button>
{/if}

if a fileis is selected - then the upoad button comes up. And thenthe usr can upload it or not.



NOt that hard now that  I have got the hang of it. Ill have to search for componets though for the file upload ui later.


Added logout feature!
Now the user can logut and the session will all be invalidated. And it works! 



I opened a repo aswl and did my first commit.


tried addingthe phosper icon pakacge. And ran into an issue I had to define it as no External in vit.config file. And had to restartthe langauge server multiple times. I want the user to click k a plus icon to add a meory rather than the adding feature being thrown when they vist the page. i have plans of displaying their memoery in clean, heartwarming ui of a random day or something like that.


i had to go little off track to fix the sql script issue so that the users can be copied to the usrs table from the auth table. AN dnowit works. got a lot of help from laude and had to fix schmea beacuse the one i had before was just for a qucik test.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/stWAQqFQ_etM/timelapse-stWAQqFQ_etM.mp4

## Entry 31
- ID: 3704
- Author: Manish
- Created At: 2026-04-24T12:46:04Z

### Content

Added a textbox for description:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzYxNiwicHVyIjoiYmxvYl9pZCJ9fQ==--2fd3449e6baa4339a317bbff6ab30aa17d5a81df/image.png)

now i need to add some more inputs. Maybe a title?

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzYyMCwicHVyIjoiYmxvYl9pZCJ9fQ==--7d109ad9d3abf8134bbb14d192676e5dc9a1dfda/image.png)

Okay thats done. And I added a preview panel as well. So when the user enters their memory content.. they can preview before they upload.

NOw i need to focus on how do i save the file so that i can acces it later while knowing which user upload which memory. Ill create a new table called memory and there I'll store the title, description, the time created and whatnot. And for the images attached.. Ill store the link to the buckets folder.So that i can access those assets later.



### Recording Links

- https://public.lapse-hackclub.link/timelapses/SdPKiotbozcJ/timelapse-SdPKiotbozcJ.mp4

## Entry 32
- ID: 3806
- Author: Manish
- Created At: 2026-04-25T03:31:38Z

### Content

I had abrubtly leave earlierI was trying to modify the memory page to havw arrays of images and videos to store.

I talked with claude quite a bit. And we (mostly claude 😓) has come with up the code to do the server side action of storing the img ids to the bucket and then posting it to the table memory.
The plan is ...
A user slects images..or files (for now images only - planning to do vids as well later)
There possibly multiple files are stored in an array named selectedFile and there is another array called preview to store the temporary viewable url for the upload file. These imgs are then displayed like this;
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzY2NiwicHVyIjoiYmxvYl9pZCJ9fQ==--d97b7bde574e013943ce72d5cdef2e7c61885cd6/image.png)
Then when the user presses the submit buttons, the images are stored to the buckets with this struture,
-memories bucket
    --- user.id 
               ----memory 1  (each user a unique folder based on the memory id to store its content)
               ----- memory 2
    ---- user.id2 (each user has its own folder)
                     ----memory 1  
                    ---- memory 2
                     ----memory 3

then aftter that is succesful (if not then the user is prompted to redo the upload) - an api call (fetch request ) call is made to the server by giving the data in json format. Then in the srver side, the +server.ts file handles the data and then posts it to the table  -memory
And if any errors occur here then the file is delted from the bucket.
if that fails then its not a huge deal as for each memory a new folder is created so for another try to upload the files, a new id will be generated so a different folder is chosen to store the content. This way the ones that have failed to delete after the db call to store info to the table - the bucket folder will just remain un unused.

okay lets test it.
The name of the stroage bucket is memories and the table is memory.


This is the schema. I tried testing it earier and i faced an error.
I have to push the new changes to the table.

```
export const memory = pgTable('memory', {
	id: uuid('id').primaryKey().notNull(),
	images: text("images").array().notNull().default([]),
	videos: text("images").array().notNull().default([]),
	userId: uuid('user_id').notNull().references(() => users.id),
	created_at: timestamp('created_at').defaultNow().notNull(),

})
```

I have been running into the internal error over and over again. first i had the server file placed outside the api route. And then I was editing that file inside of the one that was inisde the api route.Then i figured that there must be an issue with supabase as i fixed the event.locals.session not being a function error.
And indeed it was.
The schema was not correct. I forgot to include title and description.


Okay im trying to push the schma but idk why its talking so long.. it just keeps loading at
[⢿] Pulling schema from database...

Okay i fixe the issue somehow.... i used a session pooler instead of a direct or transactinal one.
Now the images are stored according to the user id and then memory folder. though i need to add the code to add memoryid for memory content.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/ipZe2nzq1Rma/timelapse-ipZe2nzq1Rma.mp4
- https://public.lapse-hackclub.link/timelapses/bjArcQUxDchJ/timelapse-bjArcQUxDchJ.mp4
- https://public.lapse-hackclub.link/timelapses/rskC6Nxu7RN5/timelapse-rskC6Nxu7RN5.mp4

## Entry 33
- ID: 3827
- Author: Manish
- Created At: 2026-04-25T06:15:18Z

### Content

I need to insert the memory id name for the folder of the image content.


What did is, i created the memory id while saving the imgs iteslef and then pass it in post method.

```
let memoryId = crypto.randomUUID();

		const filePaths: string[] = [];
		for (const file of selectedFile) {
			const filePath = `${data.user.id}/memory/${memoryId}/${Date.now()}-${file.name}`;

			const { error: fileUploadErr } = await supabase.storage
				.from('memories')
				.upload(filePath, file); // uploads the url to the temp bucket

			if (fileUploadErr) {
				errorMessage = fileUploadErr.message;
				uploading = false;
				return;
			}
			filePaths.push(filePath);
		}

		const res = await fetch('/api/memory', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ filePaths, title, description, memoryId })
		});
```

Now let's work on the voice journal where the user can insert a voice note every day to keep track of their days/moods/feelings and whatnot.

Same as the images, we ll create an input file section and from there they can upload it to the bucket.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Nzg5OSwicHVyIjoiYmxvYl9pZCJ9fQ==--8182ada4fcfff301954c2e503feca11cd8fa6050/image.png)



I created the api route for the voiceDiary and when a request is send there.. it does excatly the same thing as the memroy one xpect the voice diary has only one file input and no array.
I created the bucket in supabase and itll follow the same structure as the memory one:
 --- bucket
     - -per user folders
            -- inside which folders of the journal id
                  ---inisde which there is the file.


i need to create a schema now.


```
export const voiceDaiary = pgTable('voiceDiary', {
	id: uuid('id').primaryKey().notNull(),
	audio: text('audio').notNull(),
	userId: uuid('user_id').notNull().references(() => users.id),
	created_at: timestamp('created_at').defaultNow().notNull(),
})
```

Okay thats done... I created policies and now i can upload the voice files the way i want.


### Recording Links

- https://public.lapse-hackclub.link/timelapses/jlTRHe5UAWFj/timelapse-jlTRHe5UAWFj.mp4

## Entry 34
- ID: 3840
- Author: Manish
- Created At: 2026-04-25T08:53:51Z

### Content

Now im thinking of desiginig th user main page -the dashabord. But i really want to find a timeline ui compone to show those journals and voice memos in a beautiful layout.

Seems like there are none...
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzkwOSwicHVyIjoiYmxvYl9pZCJ9fQ==--2d99305f6a55f0ed0db35c74b0522df4ad94df54/image.png)
Claude generated me code so i told to generate a mockup and it looks pretty good. this will be my reference and ill create my own time line component.
First I need to write the function to retrieve the urls of the file.. and then display it.
to do that- i first list the buckets files and then later after they are lsited i genrate the publicUrl of those files.

```
import { getRequestEvent, query } from "$app/server";
import { memory } from "$lib/server/db/schema";
import * as v from "valibot"

export const getJournalDataForTime = query(v.object({
    time: v.string(),
    id: v.string(),
}
), async ({ time, id }) => {

    const event = getRequestEvent()
    if (id !== event.locals.user.id) return { type: "unauthorized", message: "You cant acces this data" }

    const timeframeMap: Record<string, number> = {
        week: 7,
        month: 30,
        quarter: 120,
        year: 365,
    }

    const timeframe = timeframeMap[time] ?? 7

    const cutoff = new Date()
    cutoff.setDate(cutoff.getDate() - timeframe)

    const { data, error } = await event.locals.supabase.from('memory').select("*").eq("user_id", id).gte("created_at", cutoff.toISOString()).single()

    if (error) {
        return { type: "db_error", message: error.message }
    }

    const result = await getJournalFileDataForTime(data.memory.id)

    if (!result.type) {
        return { type: "db_error", message: result.message }
    }

    return {
        type: "success", memoeryUrls: result.urls
    }

})



export const getJournalFileDataForTime = query(v.object({
    memoryId: v.string(),
}), async ({ memoryId }) => {
    const event = getRequestEvent()
    const { data: files, error: memoryFetchErr } = await event.locals.supabase
        .storage
        .from("memory")
        .list(`${event.locals.user.id}/${memoryId}`)

    if (memoryFetchErr) {

        return { type: "db_error", message: memoryFetchErr.message }
    }
    const urls = files.map(file => {
        const { data } = event.locals.supabase
            .storage
            .from("memory")
            .getPublicUrl(`${event.locals.user.id}/${memoryId}/${file.name}`)
        return data.publicUrl
    })

    return { type: "success", urls: urls }

})
```

I edited with the help of claude code

```
import { getRequestEvent, query } from "$app/server";
import * as v from "valibot"

export const getJournalDataForTime = query(v.object({
    time: v.string(),
    id: v.string(),
}
), async ({ time, id }) => {

    const event = getRequestEvent()
    if (id !== event.locals.user.id) return { type: "unauthorized", message: "You cant acces this data" }

    const timeframeMap: Record<string, number> = {
        week: 7,
        month: 30,
        quarter: 120,
        year: 365,
    }

    const timeframe = timeframeMap[time] ?? 7

    const cutoff = new Date()
    cutoff.setDate(cutoff.getDate() - timeframe)

    const { data, error } = await event.locals.supabase.from('memory').select("*").eq("user_id", id).gte("created_at", cutoff.toISOString())

    if (error) {
        return { type: "db_error", message: error.message }
    }
    const result = await Promise.all(data.map((memory: any) =>
        fetchMemoryUrls(event.locals.supabase, event.locals.user.id, memory.id)
    ))

    return { type: "success", memories: result }

})



async function fetchMemoryUrls(supabase: any, userId: string, memoryId: string) {

    const { data: files, error: memoryFetchErr } = await supabase
        .storage
        .from("memory")
        .list(`${userId}/${memoryId}`)

    if (memoryFetchErr) {

        return { type: "db_error", message: memoryFetchErr.message }
    }
    const urls = files.map((file: any) => {
        const { data } = supabase
            .storage
            .from("memory")
            .getPublicUrl(`${userId}/${memoryId}/${file.name}`)
        return data.publicUrl
    })

    return { type: "success", urls: urls }

}
```
I just hope this works.Ill check it out later.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/aSuRjjJ0a9WH/timelapse-aSuRjjJ0a9WH.mp4

## Entry 35
- ID: 4355
- Author: Manish
- Created At: 2026-04-28T14:51:31Z

### Content

Earlier I create the remote fucntion to fetch the all the imgs of a,, the memories over a time fram with claude. And now Im designing the compone twhich will display this data.


This is the component as of now:

```
<script lang="ts">
	import { getJournalDataForTime } from '../../routes/(app)/journal.remote';

	let { time, id } = $props();
</script>

{#await getJournalDataForTime({ time, id })}
	<p>Loading....</p>
{:then result}
	{#if result.type == 'success'}
		{#each result.memories as memory}
			<div>
				{#each memory.urls as url}
					<img src={url} />
				{/each}
			</div>
		{/each}
	{:else}
		<p>There was an error loading data</p>
	{/if}
{/await}

```

There seems to be an issue though. The imgs are not being displayed. I checked the network tab and i see the array is returned as [] - empty.



Ahh the locationus the problem... the memories are not properly stored. let me fix that.

I think its fixed. I mad ethe folder struture the same which is  user.id/memoery.id/filename .. now ill test and see if it works.
Good news! - 
I get the response:
{
    "type": "result",
    "result": "[{\"type\":1,\"memories\":2},\"success\",[3,5,7],{\"type\":1,\"urls\":4},[],{\"type\":1,\"urls\":6},[],{\"type\":1,\"urls\":8},[9,10],\"https://neaqqezbostlibynjyte.supabase.co/storage/v1/object/public/memories/556ee58a-b22d-4ba9-9288-be1931dfd0a0/d1a8123b-8f2d-44ef-9300-233b017b1f5a/1777269371195-image-Photoroom%20(1).png\",\"https://neaqqezbostlibynjyte.supabase.co/storage/v1/object/public/memories/556ee58a-b22d-4ba9-9288-be1931dfd0a0/d1a8123b-8f2d-44ef-9300-233b017b1f5a/1777269371672-download.png\"]"
}

but one issue.. they dont display!

its the bucket settting:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODY4MCwicHVyIjoiYmxvYl9pZCJ9fQ==--78b3dc0a6cf42fc2fb45f81952243fe6e8b4fb1d/image.png)
Now its set to public to be accessible.. the secuirty is added by rls policy.



YAYYY.


This is coming together. I can get the imgs now and display it aswl.

I got it!

```

{#await getJournalDataForTime({ time, id })}
	<p>Loading....</p>
{:then result}
	{#if result.type == 'success' && result.info}
		{#each result.memories as memory, i}
			<div>
				<h1>{result.info[i].description}</h1>
				<p>{result.info[i].description}</p>
				{#each memory.urls as url}
					<img src={url} />
				{/each}
			</div>
		{/each}
	{:else}
		<p>There was an error loading data</p>
	{/if}
{/await}

```
i return the data and then print it altogether. Now will work on the ui soon!
Still have to figure some issue out though.


Ahh fixed it. Its all done now. It works!
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ODk3OCwicHVyIjoiYmxvYl9pZCJ9fQ==--ed083d733be28ae738458b3038e78fda57611ca8/image.png)

Now i gotta work on the voice journal and combine it

This is what I did for the voiceDiary files.. havnt tested though

```
async function fetchAudioUrls(supabase: any, userId: string, memoryId: string) {
    const { data: audioFilesList, error: audioFetchErr } = await supabase.storage.from("voiceDiary").list(`${userId}/${memoryId}`)

    if (audioFetchErr) {
        return { type: "success", message: "There was an error listing voice files" }
    }

    const AudioUrls = audioFilesList.map((file: any) => {
        const { data } = supabase
            .storage
            .from("memories")
            .getPublicUrl(`${userId}/${memoryId}/${file.name}`)

        return data.publicUrl
    })

    return {
        type: "success", urls: AudioUrls
    }
}
```


I need to group the data together so I created thi record but im sure it s wrong.

```
type journalTimelineInfo = {
    title:  Array<string | null>,
    description: Array<string | null>,
    imageUrls: Array<string | null>,
    audioUrls: Array<string | null>,
    data:  Array<string | null>
}
```

 so i asked claude and it gave a better record structure.


Now i just finished making the whole jounral timeline data fetch setup. A lot of learnig from claude and it did almost all of the heavy lifting... its just like that... it was too complex for me to do it on my own. Well its alright. i can work on other parts of the project 100%.


This is how it works..

These are the types:

```

type MemoryEntry = {
    type: "success"
    id: string
    title: string | null
    description: string | null
    imageUrls: string[]
    date: string
} | {
    type: "db_error"
    message: string
}


type voiceDiaryEntry = {
    type: "success"
    audioUrl: string | null
    date: string
} | {
    type: "db_error"
    message: string
}


type DayEntry = {
    date: string
    memories: MemoryEntry[]
    voiceDiaries: voiceDiaryEntry[]
}


type JournaLTimeline = {
    type: "success"
    days: DayEntry[]
}
```

first we convert the string data -like "week" / "month" to number. Adn then pass it into two async fucntions - getmemoryData and getvoiceData to get data for each.
Inside each async fucntion .. there is  a db cal to the table and then fetch the users's memory/audio records and that exists within that timeframe. Then after that is fetched a loop is run to get all teh files from respective buckets for the imgs/voice files and then turned into public url. After all this is done.. all of this is encoded  - arranged - in the Day type based on the date match (a usser might have two memories ina  day and another audio journal aswl) and then added it to the journaltime data type. This way i can accumulate all the jounral content of a day/timeframe of theuser for both the memories and the voice altogether.

It works ! I did some troubleshooting and fixes and its perfect :)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTAwMywicHVyIjoiYmxvYl9pZCJ9fQ==--a4477b061213e9c83a6abbf61c5ca6512805a6a4/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTAwNywicHVyIjoiYmxvYl9pZCJ9fQ==--e92e6eb92750fa3a3070ccc7e682cdc47103498d/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/jzLLDcWk7LtC/timelapse-jzLLDcWk7LtC.mp4
- https://public.lapse-hackclub.link/timelapses/CLz_XWasqntY/timelapse-CLz_XWasqntY.mp4
- https://public.lapse-hackclub.link/timelapses/xtGA4i5YDxth/timelapse-xtGA4i5YDxth.mp4
- https://public.lapse-hackclub.link/timelapses/aBUMxWnsKYhN/timelapse-aBUMxWnsKYhN.mp4

## Entry 36
- ID: 4464
- Author: Manish
- Created At: 2026-04-29T08:48:32Z

### Content

I made some changes to the name of the routes. The voice -audio journal page is now logs. And there is no more pictures page instead there is a calendar page which will show a nice ui -(google calendar type) to display memories or acitivy maybe...

Now ill finish the ui part and start building the other stuff like the vids integration, calendar page and whatnot.
To do that.. first ill start with themes.I have written notes for that so ill just refer to that.

To get my them variables setup fast.. ill talk with my very good freind Claude!!
and from there ill integrate it in the code to switch between those themes. Im thinking of just going with two themes. light (warm type) and dark (professional dark black).

Yes! Claude got the feel just right. Now i have got the refrence for my website and the theme variables. NOw i can pretty up the website.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTIyNSwicHVyIjoiYmxvYl9pZCJ9fQ==--76441b1dba34b2ca2c89886a29ed40ed47c0ef36/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTIyNywicHVyIjoiYmxvYl9pZCJ9fQ==--968b3ded8ce4bcb68892bba7a6d410359bad9ce4/image.png)


I have the themes set up right. I used this resource mostly (i wrote this myself when i was working on another project of mine)
https://maker-base.vercel.app/view/manish_themes-in-svelekithttps://maker-base.vercel.app/view/manish_themes-in-svelekit

And used gemini to fill in the gaps in the resource.


Oh my days.
I  have been stuck on the navbar postioning for 30 mins i think. Neither was margin nor was padding working. And it was so weried. I askd gemin and gemini response was also not working. And I was like do i not know css now....
turns out the app.css was overwriting my margin and padding vaues to 0. Claude did that and i didnt check it ..(i left for me to review later when im done with the navbr and whanot).

I removed margin:0 and padding: 0

```
*, *::before, *::after {
  box-sizing: border-box;
}

```

This is how it looks like after making the chnages

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTI1NSwicHVyIjoiYmxvYl9pZCJ9fQ==--330016527910c3567b53fe105ce3c81084b58454/image.png)


I am working on the dashboard but im too overwhelemed to handle all these cards. Ill start fresh later.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTI1NywicHVyIjoiYmxvYl9pZCJ9fQ==--8f7990b5c958e00ae66bc3a3eacb03832b785a75/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/dJ4rLUcmTL72/timelapse-dJ4rLUcmTL72.mp4
- https://public.lapse-hackclub.link/timelapses/qOaujpozGsOE/timelapse-qOaujpozGsOE.mp4
- https://public.lapse-hackclub.link/timelapses/NWH4pTa7URiq/timelapse-NWH4pTa7URiq.mp4

## Entry 37
- ID: 4602
- Author: Manish
- Created At: 2026-04-30T08:59:47Z

### Content

Im working on the user dashboard now.
this is what will fetch the user info. for now im just fetching the usr memories and voice data.

```
import { getRequestEvent, query } from "$app/server";
import * as v from 'valibot'

export const getUserDashboardInfo = query(v.string(), async (id) => {
    const event = getRequestEvent()
    if (event.locals.user.id !== id) return { type: "unauthorized", message: "You cant view this page" }

    const recentMemories = event.locals.supabase.from("memories").select("*").eq("user_id", id).limit(4)
    const recentVoice = event.locals.supabase.from("voiceDiary").select("*").eq("user_id", id).limit(4)

    const [memoriesResult, voiceResult] = await Promise.all([recentMemories, recentVoice])
    if (memoriesResult.error || voiceResult.error) {
        return { type: "db_error", message: "There was an error fetching your data" }
    }


    return {
        type: "success",
        memories: memoriesResult.data,
        voice: voiceResult.data
    }
})
```


Everything seems fine but the console gives me this error:
runtime-tBM9B0p3.js?v=4f179450:449 Uncaught (in promise) Svelte error: hydratable_missing_but_required
Expected to find a hydratable with key `1mktawg/getUserDashboardInfo/WyI1NTZlZTU4YS1iMjJkLTRiYTktOTI4OC1iZTE5MzFkZmQwYTAiXQ` during hydration, but did not.
https://svelte.dev/e/hydratable_missing_but_required
    at hydratable_missing_but_required (runtime-tBM9B0p3.js?v=4f179450:449:33)
    at Module.hydratable (client-Ca7W1_f-.js?v=4f179450:19:3)
    at unfriendly_hydratable (shared.js?v=4f179450:320:16)
    at QueryProxy.<anonymous> (query.svelte.js?v=4f179450:58:54)
    at Query.<anonymous> (query.svelte.js?v=4f179450:492:53)
    at #run (query.svelte.js?v=4f179450:271:27)
    at query.svelte.js?v=4f179450:246:76
    at untrack (runtime-tBM9B0p3.js?v=4f179450:5030:10)
    at #get_promise (query.svelte.js?v=4f179450:246:8)
    at query.svelte.js?v=4f179450:219:31



OH MY GOD>
Could not find the table 'public.memories' in the schema cache

This stupid.
I shouldnt have just pritned the error msg.




![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTU5NSwicHVyIjoiYmxvYl9pZCJ9fQ==--bf75099c18572165939180e48f54a13344c161c7/image.png)

Now it works!

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTYwMSwicHVyIjoiYmxvYl9pZCJ9fQ==--aa5c2101d55f5783f34fb36291d329b1372273c0/image.png)

I did it for the voice as well. And got each recent memory's image public url. And displayed the first one.



I fixed the theme variables issue as well and now the website /coloring looks more welcoming
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTYwNSwicHVyIjoiYmxvYl9pZCJ9fQ==--3efc4884afae2d050f0d08d92d7e45f34c6af52e/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/vrGNTRdCMP3i/timelapse-vrGNTRdCMP3i.mp4

## Entry 38
- ID: 4625
- Author: Manish
- Created At: 2026-04-30T14:14:48Z

### Content

ITs time to update the memory adding page's ui.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTYxNCwicHVyIjoiYmxvYl9pZCJ9fQ==--c9be73ded170fed6c337dde8ad8d654fd9f51c9c/image.png)
I got a refrence from claude. And it looks good!
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTYyMCwicHVyIjoiYmxvYl9pZCJ9fQ==--fef836f00104e7f64bee802ec0db9687aeb50f31/image.png)
And its done!

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTYyMSwicHVyIjoiYmxvYl9pZCJ9fQ==--afb9ac6522d5ee021678524233b0fe728639d5a8/image.png)

I did some testing and it works!
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTYyMiwicHVyIjoiYmxvYl9pZCJ9fQ==--b7e190a7da59ecde24bef68d885e620b4cd8ac2e/image.png)
The ui testing memory was just uploaded.


Did the voice page as well.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTYyNywicHVyIjoiYmxvYl9pZCJ9fQ==--1d719d3686b311b518f9ad8d934d527606e27c7e/image.png)
now i need to clear up the timeline page. The data is fetched but the ui is not setup. Im giving claude to design the timeline component,


And claude gives me 700+ lines of code..... bruh,
Im not gonna copy all that.
itll be easier to debug and understand if i jutst do it myslef. I just ask fro the live mockup.


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTY3NywicHVyIjoiYmxvYl9pZCJ9fQ==--9220028aa9e5d9fc8574f21b8ae52b24aecb64be/image.png)

This is how it looks.Now gotta make the timeline line ui.


With the help of ai - claude and gemini i got this:

'
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTY3OSwicHVyIjoiYmxvYl9pZCJ9fQ==--6092f61fd937515fc7b40f780499c3a1512e938a/image.png)
Now gotta make the lune appear.


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTY4MSwicHVyIjoiYmxvYl9pZCJ9fQ==--52b556d41b53e52052c6aa04c193b58e803936ee/image.png)



Evything else is fine its just the text-font that needs work.
I cant change it from the default.
!text-[var(--font-display)]
this doesnt work
and neither does this- 
!font-[var(--font-display)]

### Recording Links

- https://public.lapse-hackclub.link/timelapses/XYhvmUZ3clm2/timelapse-XYhvmUZ3clm2.mp4
- https://public.lapse-hackclub.link/timelapses/oqYl6cD2KbI7/timelapse-oqYl6cD2KbI7.mp4

## Entry 39
- ID: 4737
- Author: Manish
- Created At: 2026-05-01T09:59:53Z

### Content

ITs now time to add the api routes for the esp32 devices. I have no idea till now how to handle to users from esp device. What i know is that the eps32 calls the web through the api key through web scokets from POST method like any other api projects. I need to figure out how to create that api key for each usres and authenticate and find that usr's table to insert into there.

Added the key genration and the inserting to the table flow.

```
import { db } from '$lib/server/db/index.js'
import { json } from '@sveltejs/kit'
import { error } from 'console'
import { randomBytes } from 'crypto'

export async function POST(event) {
    const session = event.locals.session
    const db = event.locals.supabase
    if (!session) return json({ error: 'authorized' }, { status: 401 })

    const userId = session.user.id

    const existing = await db.from('device_keys').select('*').eq('user_id', userId).limit(1).single()

    if (existing.data) {
        return json({ key: existing.data.raw_key, label: existing.data.label })

    }

    const rawKey = randomBytes(32).toString('hex')

    const { error: insertErr } = await db.from("device_key").insert({
        user_id: userId,
        raw_key: rawKey,
        label: 'My ESP32'
    })

    if (insertErr) {
        return json({ error: "There was an error" }, { status: 401 })
    }

    return json({ key: rawKey, label: 'My Esp32' })
}
```
This is the conenct page:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6OTk5NywicHVyIjoiYmxvYl9pZCJ9fQ==--638f385ae114c3136bcf0f9b48311e2d0ee6072f/image.png)


```
<script lang="ts">
    let apiKey = $state('')
    let errorMessage = $state('')
    let label = $state('')
    let loading = $state(false)
    let generated = $state(false)



    async function generateKey(){
        loading = true
        const res = await fetch('/api/device-keys/generate', {method: 'POST'})
        const data = await res.json()

        if (data.error){
            errorMessage = data.error
            loading = false
            return

        }

        apiKey = data.key
        label = data.label
        loading = false
        generated = true
    }

</script>


<div>
    <h1>Connect your Esp32</h1>


    {#if !generated}
        <button onclick={generateKey} disabled={loading}>
            {loading ? 'Geneerating...' : 'Generate Key'}
        </button>


        {:else}
        <div>
            <p>Your API key :</p>
            <code>{apiKey}</code>
        </div>
    {/if}
</div>
```

Now need to create an api for the esp32 same as thr one for the broswer usrs but little bit different.


I create supabaseAdmin client. And then realced the supabase calls with that client for the esp32.

```

import { json } from '@sveltejs/kit'


export async function POST(event) {
    const deviceKey = event.request.headers.get('x-device-key')


    if (!deviceKey) return json({ error: "unauthorized" }, { status: 401 })

    const supabase = event.locals.supabaseAdmin

    const {data: keyRow, error:keyError} = await supabase.from('device_keys').select('user_id').eq("raw_key", deviceKey).single()


    if (keyError){
        return json({error: "unauthorized"}, {status: 401})

    }

    const userId = keyRow.user_id

    const { filePaths, title, description, memoryId } = await event.request.json()



    const { error: dbError } = await supabase.from('memory').insert({
        id: memoryId,
        user_id: userId,
        title,
        description,
        images: filePaths
    })

    if (dbError) {
        await supabase.storage.from('memories').remove(filePaths)
        return json({ error: 'Failed please try again' }, { status: 500 })
    }

    return json({ success: true })
}
```

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMDUsInB1ciI6ImJsb2JfaWQifX0=--f430ef884e59e561be4976989cdb66e18df5bf60/image.png)
I created insert policy and it works now.

The testing for whether or not theuploadingthrough eps32 works or not will be done when i get my hands on the pcb itself.


### Recording Links

- https://public.lapse-hackclub.link/timelapses/8UvgkwqRvXKW/timelapse-8UvgkwqRvXKW.mp4

## Entry 40
- ID: 4743
- Author: Manish
- Created At: 2026-05-01T11:20:56Z

### Content

I need to host the website.
Its up but it doesnt showanything for its homepage.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMTIsInB1ciI6ImJsb2JfaWQifX0=--e2c701ad80d95627d671f01d90f256fb1a2bc965/image.png)


I added some fixes to the layout.svelte and it now works on the localhost
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMTQsInB1ciI6ImJsb2JfaWQifX0=--442162e6c178c28170a1ffaa92f2a775977f213d/image.png)

Its alright for now.

And i fixed the form pages as well. 
Add these "footers"
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAwMTksInB1ciI6ImJsb2JfaWQifX0=--8ca0a5d1483939a4cc8940b31718125f646a16f7/image.png)


Now i need to do something for the esp32 firmware.

This should do for now. This is to post memory to db. Nowif this works while testing then i can just copy and make change to this for the voice side of things aswl

```
def postMemoryToDb(files, title, description):
    headers = {
        'Content-Type': 'application/json',
        'x-device-key': DEVICE_KEY
    }
    
    body = json.dumps({
        'title':  title,
        'description': description,
        'filePaths': []
    })
    
    response = requests.post(MEMORY_API_URL, headers=headers, data=body)
    
    print("Status:", response.status_code)
    print("Response", response.text)
    
    response.close()
```

This si the ui pages:

```
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
```

Not much beacuse i cant just write code without testing. I ll get the tft and then make the ui and the fucntion works properly. The basic structure is laid out.


### Recording Links

- https://public.lapse-hackclub.link/timelapses/9JDfzF4XikiW/timelapse-9JDfzF4XikiW.mp4

## Entry 41
- ID: 5067
- Author: Manish
- Created At: 2026-05-02T06:07:53Z

### Content

what i noticed in the deployed website is that.. when the user logs in  - the dashboard doesnt show the nav bar because the if statement is not satisfied in the first instance.
I need to do await invalidateAll() to refetch the session data from layout.server.ts file.


I need to setup emial system through my gmail accountin supabase aswl. Or else only 3 auth emails will be sent each hr.

Okay now thats done. I oushed to github with the fixes i made regardingthe side navigation bar and other changes. Ill test the gamil SMTP.

Okay the SMTP was working. Im recieving the gmails but there was one issue. It takes me to the verify page and i have to hard relaod to take me to the dashboard.
So i fixed it after multiple tries
irst i tried adding a redirect to the page.server.ts file but instead i found out that there was redirect directly on the signup page which was wrong.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzMTMsInB1ciI6ImJsb2JfaWQifX0=--6e9c2ee637a6a3cbd269e716d2a6f1a3540da5b6/image.png)
thats why i made it so that the check email displayson the signup page only.

And later when the usr clicks on the email link it takes them to the verify page.

There:

```
<script lang="ts">
	import { supabase } from '$lib/supabase.js';
	import { goto, invalidateAll } from '$app/navigation';
	import { onMount } from 'svelte';

	onMount(async () => {
		// Wait for supabase to set the session
		const {
			data: { session }
		} = await supabase.auth.getSession();

		if (session) {
			await invalidateAll();
			goto('/');
		} else {
			supabase.auth.onAuthStateChange(async (event, session) => {
				if (session) {
					await invalidateAll();
					goto('/');
				}
			});
		}
	});
</script>

<p>Verifying your account...</p>

```

Onmount-itl check for a session and then redirect to the dashboard. And it works! Got help from claude for the session checking part.



Now that evything is fairly working. I focused on the readme files.
I edited both of them. but for the life_on_pocket repo i have to get images for the case and pcb render. Adn the 3d case to be exported. Fusion 360 keeps on crashing :(


### Recording Links

- https://public.lapse-hackclub.link/timelapses/07flrPcXL1ND/timelapse-07flrPcXL1ND.mp4
- https://public.lapse-hackclub.link/timelapses/gvlEimq0lNa_/timelapse-gvlEimq0lNa_.mp4
- https://public.lapse-hackclub.link/timelapses/wty90sTY8Ftl/timelapse-wty90sTY8Ftl.mp4

## Entry 42
- ID: 5107
- Author: Manish
- Created At: 2026-05-02T12:52:49Z

### Content

Now it time to make the poster.
Im deciding between canva and figma.

I think Canva is much more easier with its pre designed templates and elements.

I started designing...
And it turned out absolutely horrible.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzOTUsInB1ciI6ImJsb2JfaWQifX0=--fc254995580cc57e46d929b7cdeb115043c45f19/image.png)

So i asekd claude and it gave me a refrence to work with. But the reference wasnt that helped me.. it was the idea that struck me when it was designing the poster itself.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzOTYsInB1ciI6ImJsb2JfaWQifX0=--d68da6f1dcb6dae444a91ddcdf045b8df79f1c59/image.png)


Then, i locked in and at the end got this ..
![boo! (1).png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTAzOTcsInB1ciI6ImJsb2JfaWQifX0=--8aadad14bce2dfe30375ba6202489a980ff868cc/boo! (1).png)

I need to work on the bom now.

I need to do pcb assembly for smd parts as well. Both side becasue i have smd components on both.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTA0MTcsInB1ciI6ImJsb2JfaWQifX0=--06a31a9817d8ffa803ec1a2f35bdc43b8bb95388/image.png)
Ill need to ask help from slack on placing the order correctly.



I jjsut got some suggestions to improve my poster from slack, ill be qucik iwth it.

I added some elmetns and changed placment a bit and upadated the github. ITs all done!

### Recording Links

- https://public.lapse-hackclub.link/timelapses/5Tx82HwZsNwv/timelapse-5Tx82HwZsNwv.mp4
- https://public.lapse-hackclub.link/timelapses/0k93BNW8x1fL/timelapse-0k93BNW8x1fL.mp4

## Entry 43
- ID: 5598
- Author: Manish
- Created At: 2026-05-05T15:09:21Z

### Content

I need to integrate google auth and make the index page for the website and will call it done for the website. And also the user dashboard needs to be functional as well.

Alright first google auth.

Created a new project in google console.
Btw im using this as my guide - this was written by me.
https://maker-base.vercel.app/view/manish_google-auth-simplified


AHHH, i have been stuff at this issue for so long. 
The button was no working for the Google Auth. I checked with gemini and evything was good.. nothing big of a issue. I made those changes which gemini sugested and then too it was not responding. And now i just added another button and it works somehow... i can choose my google account for signup.

Oh.... The issue what i forgot the brackets () for the function call - signUpWithGoogleIO on click....

The user was not redirected to their dashboard page after signin becasue the client side info was not updated. It needed ahard refresh.
So we do a invalidteall on mount for any page..
this is the magic code:

```
const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
            // When the callback finishes and the user is 'SIGNED_IN', 
            // this triggers and refreshes all your server-side load functions.
            if (event === 'SIGNED_IN' || event === 'SIGNED_OUT') {
                invalidateAll();
            }
        });

        return () => subscription.unsubscribe();
```
 Gemini helped me with it.


Okay the main thing is done. The padding seems little bit off for the signup page but thats alirght. Thats a problem for another day. I cant deal with it now.. idk my brain is just like that today... gemini does seem to be getting to me aswl.. ill leave it to that.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE2NjgsInB1ciI6ImJsb2JfaWQifX0=--a272a0e969af0a78a06c37c101c9a841a00b1260/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/NjQwUVatBn9e/timelapse-NjQwUVatBn9e.mp4

## Entry 44
- ID: 5904
- Author: Manish
- Created At: 2026-05-07T14:23:26Z

### Content

Okay its time to build the home page.
This is the refrence Ill be using that was generated by claude.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MDAsInB1ciI6ImJsb2JfaWQifX0=--73f2e5f047d96adf731acd9035944115c9051824/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTIzOTksInB1ciI6ImJsb2JfaWQifX0=--89fe4a1c28f7de5b4a1cdc4af944071df505de65/image.png)


I out the already written signup and login row at the top.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MTQsInB1ciI6ImJsb2JfaWQifX0=--fb9c0a0fcb0fb24c6a86e033c518e5b2ab3804e3/image.png)
And make the hero text section. It feels mostly empty now -- will add stuff later. Like some cartoonish.. artwork and all that.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MTUsInB1ciI6ImJsb2JfaWQifX0=--350ee88743ed488c08f598fb0a8c51ca925427a4/image.png)
This should clear out what is included in the keep account.



Made this peak sectionw here we show what it would be like for users to save thier memories/voice
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MjcsInB1ciI6ImJsb2JfaWQifX0=--07b741ce6a9db0dd02e5fe7662a420f1c0a0d44d/image.png)


Its ready !
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0MzgsInB1ciI6ImJsb2JfaWQifX0=--db53cb45af3304ec0c441a36143d82d79baf7a6a/image.png)

Added theme slector..
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTI0NDEsInB1ciI6ImJsb2JfaWQifX0=--920fb69bc08676db17fd0e652ef7703b7a3eaf54/image.png)


### Recording Links

- https://public.lapse-hackclub.link/timelapses/clIZJNqLUwHH/timelapse-clIZJNqLUwHH.mp4

## Entry 45
- ID: 6280
- Author: Manish
- Created At: 2026-05-09T15:54:39Z

### Content

I first did some editing on the zine. Changed the texture of the 3d model. Settled on plastic at last..
I should have done this the first time around when i was making the zine but I hadn't updated Fusion 360, and it didnt allow me to change the texture cuz of that.

I added my name. Suggested by renran.

It seems i forgot to add a title input for the voice logs.

I updated the schmea for the voiceDiary table:

```
export const voiceDaiary = pgTable('voiceDiary', {
	id: uuid('id').primaryKey().notNull(),
	title: text('title').notNull().default((new Date().toISOString()).split('T')[0]),
	audio: text('audio').notNull(),
	userId: uuid('user_id').notNull().references(() => users.id),
	created_at: timestamp('created_at').defaultNow().notNull(),
})

```

I chose just the date with no timestamp becasue its too long for the default title.

And look at that.. it works!

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMzMTYsInB1ciI6ImJsb2JfaWQifX0=--7f0e101230f7d0183a714e72dafbc672d7dba6f8/image.png)
I tested it too.

And did some ui changes  (error handling to show to users)
And create a new remote fucntion to get the user stats:
And it works! NOt that muhc of a deal. Copilot helped
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMzMjAsInB1ciI6ImJsb2JfaWQifX0=--2d088faf8e46fa1f8f0416bb14f360e8004c6e68/image.png)


Create this new table - to save the streaks for users:

```
export const streak = pgTable('streak', {
	id: uuid('id').primaryKey().notNull(),
	userId: uuid('user_id').notNull().references(() => users.id, { onDelete: 'cascade' }),
	currentStreak: text('current_streak').notNull().default("0"),
	longestStreak: text('longest_streak').notNull().default("0"),
	lastUpdated: timestamp('last_updated').defaultNow().notNull(),
})
```

NOw need to handle increasing th streak if the user posts.



I have added a streak fetch for the dash... but it doesnt work.. idk why. Maybe rls? but it seems fine.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTMzMzYsInB1ciI6ImJsb2JfaWQifX0=--a43ef553e0dfc94a54d777f02e654798c4da6045/image.png)
Ill just fix it tmr. And have to see wether the streak works or  not aswl.

### Recording Links

- https://public.lapse-hackclub.link/timelapses/laPls-MIt9HM/timelapse-laPls-MIt9HM.mp4
- https://public.lapse-hackclub.link/timelapses/NKziJJU4h9DX/timelapse-NKziJJU4h9DX.mp4
