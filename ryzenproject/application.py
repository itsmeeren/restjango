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

u
# for creating database and updating the content


def get_data(id=None):
    data1={}
    if id is not None:
        data1={'id':id}
    json1=json.dumps(data1)
    r=requests.post(url=URL,data=json1)# use new url dont use the url above mentioned
    data2=r.json()
    print(data2)

# this is for updating the database

import requests
import json


URL='http://127.0.0.1:8080/datacreate/'
data={
    'id':2 ,# we have send in the id of the database to get updated
    'first_name':"kar",
    "last_name":'mn',
    "roll_number":5


}
json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json
print(data)
