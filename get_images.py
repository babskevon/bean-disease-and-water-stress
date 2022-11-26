import cv2
import datetime
from time import sleep


def get_bean_image(index):
    image_name = "img_"+str(datetime.datetime.now()).replace(" ","-")+".jpg"
    cam = cv2.VideoCapture(index)
    
    while True:
        ret, image = cam.read()
        sleep(2)
        # cv2.imshow(image_name,image)
        # k = cv2.waitKey(1)
        # if k != -1:
        #     break
        break
        
    cv2.imwrite(image_name, image)
    cam.release()
    cv2.destroyAllWindows()

    return image_name



def get_image_height(index):
    image_name = "img_"+str(datetime.datetime.now()).replace(" ","-")+".jpg"
    cam = cv2.VideoCapture(index)
    
    while True:
        ret, image = cam.read()
        cv2.imshow(image_name,image)
        k = cv2.waitKey(1)
        if k != -1:
            break
        
    cv2.imwrite(image_name, image)
    cam.release()
    cv2.destroyAllWindows()

    return image_name
