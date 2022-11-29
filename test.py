import requests
import json
from get_images import get_image_height
url = 'https://farmbotug.pythonanywhere.com/photo/'
# url = 'http://127.0.0.1:8000/photo/'
name = get_image_height(0)
# myfiles = {'file': open(name ,'rb')}
f = open(name,'rb')
response = requests.post(url,files={'name':f})
# response = json.loads(response.text)
response = response.text
print(response)
# {'stress': 'water_stressed', 'stress_score': 99.89928603172302, 'bean': 'bean_rust', 'bean_score': 86.40068769454956}


# c166dc5464c154f7b30909e1783243f4cb7a96a4