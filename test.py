import requests
import json
from get_images import get_image_height
url = 'http://127.0.0.1:8000/photo/'
name = get_image_height(0)
# myfiles = {'file': open(name ,'rb')}
f = open(name,'rb')
response = requests.post(url,files={'name':f})
response = json.loads(response.text)
print(response)
# {'prediction': 'bean_rust', 'score': 99.61293935775757}
# {'prediction': 'water_stressed', 'score': 51.284801959991455}