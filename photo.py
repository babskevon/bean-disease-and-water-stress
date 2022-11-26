from picamera import PiCamera
from time import sleep, time
import requests
from get_images import get_bean_image, get_image_height
def photo():
    camera = PiCamera()
    camera.start_preview()
    name = str(int(time())) + ".jpg"
    camera.capture(name)
    sleep(2)
    camera.stop_preview()
    return name



name = photo()
print(name)
url = 'https://robinah.pythonanywhere.com/photo/'

f = open(name,'rb')

tt = requests.post(url,files={'name':f})
print(tt.text)