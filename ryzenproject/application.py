#This is the windows or mobile application through which we can access the app with all the function of the
# webApi


# import requests
#
# URL='http://127.0.0.1:8080/Datas/'
#
# r=requests.get(url=URL)
# data=r.json()
# print(data)
import requests
import json


URL='http://127.0.0.1:8080/datacreate/'
data={
    'first_name':"kar",
    "last_name":'mn',
    "roll_number":5


}
json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json
print(data)