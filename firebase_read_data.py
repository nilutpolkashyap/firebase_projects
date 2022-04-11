import pyrebase
import time

firebaseConfig= {
    "apiKey": "AIzaSyDCE8PFIpoTwsz8WZ4ZJEoo6IOSjXDUV68",
    "authDomain": "esp32-firebase-e009f.firebaseapp.com",
    "databaseURL": "https://esp32-firebase-e009f-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "esp32-firebase-e009f",
    "storageBucket": "esp32-firebase-e009f.appspot.com",
    "messagingSenderId": "93810068764",
    "appId": "1:93810068764:web:a4abb0d7117aed04adfed9"
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






