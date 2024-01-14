#This is the windows or mobile application through which we can access the app with all the function of the
# webApi


import requests

URL='http://127.0.0.1:8080/Datas/'

r=requests.get(url=URL)
data=r.json()
print(data)