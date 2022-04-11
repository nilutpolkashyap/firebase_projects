import pyrebase
import time

firebaseConfig= {
    "apiKey": "###############################",
    "authDomain": "###############################",
    "databaseURL": "###############################",
    "projectId": "###############################",
    "storageBucket": "###############################",
    "messagingSenderId": "###############################",
    "appId": "###############################"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

data={"test":{"command":"FR", "light":1, "arm":0.5}}
db.update(data)

# time.sleep(5)

# data={"test":{"command":"TR"}}
# db.update(data)






