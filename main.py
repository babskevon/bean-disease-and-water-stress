from get_images import get_bean_image, get_image_height
from time import sleep
import os
import requests
import RPi.GPIO as GPIO
CAPTURE_PHOTO13 = 13
CAPTURE_PHOTO12 = 12
IRRIGATE_COMMAND11 = 11
SPRAY_COMMAND10 = 10
print("Program started")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CAPTURE_PHOTO13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(CAPTURE_PHOTO12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# GPIO.setup(FLOW_SENSOR_GPIO12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(IRRIGATE_COMMAND11, GPIO.OUT)
url = 'https://farmbotug.pythonanywhere.com/data/'


# function to take photo and diagnise beans
def spray_beans():
    name = get_bean_image(0)
    url = 'https://farmbotug.pythonanywhere.com/photo/'
    f = open(name,'rb')
    response = requests.post(url,files={'name':f}).text
    if(response['irrigate'] == 1):
        GPIO.output(IRRIGATE_COMMAND11, GPIO.HIGH)
        sleep(6)
        GPIO.output(IRRIGATE_COMMAND11, GPIO.LOW)
    if(response['spray']== 1):
        GPIO.output(SPRAY_COMMAND10, GPIO.HIGH)
        sleep(6)
        GPIO.output(SPRAY_COMMAND10, GPIO.LOW)
    os.remove(name)

def plant_height():
    name = get_bean_image(1)
    url = 'https://farmbotug.pythonanywhere.com/photo2/'
    f = open(name,'rb')
    response = requests.post(url,files={'name':f}).text
    sleep(1)
    os.remove(name)


GPIO.add_event_detect(CAPTURE_PHOTO13, GPIO.RISING, callback=spray_beans)
GPIO.add_event_detect(CAPTURE_PHOTO12, GPIO.FALLING, callback=plant_height)
while True:
    # keep listening to server for irrigate or spray commands
    try:
        data = {}
        value = requests.post(url,data=data)
        if(value['spray']==1):
            GPIO.output(SPRAY_COMMAND10, GPIO.HIGH)
            sleep(6)
            GPIO.output(SPRAY_COMMAND10, GPIO.LOW)
        if(value['irrigate'] == 1):
            GPIO.output(IRRIGATE_COMMAND11, GPIO.HIGH)
            sleep(6)
            GPIO.output(IRRIGATE_COMMAND11, GPIO.LOW)
        if(value['photo'] ==1):
            spray_beans()
        if(value['photo']==2):
            plant_height()
    except:
        pass
    break

    
# os.remove(name)
# os.remove("img_2022-11-26-14:08:54.051870.jpg")