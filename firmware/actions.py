import asyncio
import socket

DEVICE_KEY = 'raw_api_key'
MEMORY_API_URL = 'https://keeplife.vercel.app/api/esp32/memory'

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