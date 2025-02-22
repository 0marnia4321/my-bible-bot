import requests
from urllib.parse import *

#Webserver

from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "I'm still alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()



#Main Code

csrf_token = requests.get("https://api.darflen.com/data").json()['csrf']

login_info = {

     "email" : "coolkat_the_tester@gmail.com",
     "password" : "nij791@#$"

}
login = requests.post("https://api.darflen.com/auth/login", data=login_info)
log_token = login.json()["token"]

url = 'https://api.darflen.com/posts/create'
data = {

     "textarea" : "The weather in ",
     "audience" : "private",
     "files" : [],
     "csrf-token" : csrf_token

}


request = urlencode(data)
response = requests.post(url, data=data, headers = {"Authorization": f"Bearer {log_token}"})  
print(response.text, response.status_code)

