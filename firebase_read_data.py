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

count = 0

while True:
    users = db.child("test").child("arm").get().val()
    if users == 0:
        print(count, users)
    elif users == 1:
        print(count, users)
    elif users == 2:
        print(count, users)
    # print(count, users)
    # time.sleep(.5)
    count = count + 1
    
    users = db.child("test").child("arm").get().val()

    




# data={"test":{"command":"FR", "light":1, "arm":0.5}}
# db.update(data)

# time.sleep(5)

# data={"test":{"command":"TR"}}
# db.update(data)






