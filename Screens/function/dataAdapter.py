import firebase_admin
from firebase_admin import credentials, initialize_app, storage ,db
cred = credentials.Certificate("Screens/monitoring-ground-personnel-51b9f97f5da1.json")
bucketPath="https://monitoring-ground-personnel-default-rtdb.firebaseio.com/"
firebase_admin.initialize_app(cred,{'databaseURL': bucketPath})



def getHostLoraCoordinates(username , bandobastId):
    ref=db.reference(username).child(bandobastId)
    try:
        log=ref.child('log').get()
        lat=ref.child('lat').get()
        location=[lat,log]
        return location
    except Exception as e:print(e)



def getMarkLocationCoordinates(username, bandobastId , personId,personCoordinates):
    
    ref=db.reference(username).child(bandobastId).child(personId)
    try:
        lat=ref.child("lat").get()
        log=ref.child("log").get()
        personCoordinates.append([personId,lat,log])

    except(Exception):pass

def getContactDetails(username, bandobastId , personId,allData):
    ref=db.reference(username).child(bandobastId).child(personId)
    try:
        lat=ref.child("lat").get()
        log=ref.child("log").get()
        contact=ref.child("Contact").get()
        name=ref.child("Name").get()
        rank=ref.child("Rank").get()

        allData.append([personId,name,rank,contact,log,lat])
        return allData        
        

    except(Exception):pass
    
    


    


def Authentication(username,password):
    ref = db.reference(username)

    if(password==ref.child('passwrod').get()):
        print("Correct Password")
        value=db.reference(username).get()
        for x in value:
            return x
    else:
        print("Incorrect Username or Password")
        return value

def getPersonDataFilesFromRuntime(username,bandobastId):
    person=[]
    ref = db.reference(username).child(bandobastId).get()
    for y in ref:
        person.append(y)
    return person

def uploadfilesToRuntime(token,bandobastId,password,personList):
    ref = db.reference('/').child(token)
    ref.update({
        'passwrod':password,
    })
    
    person=ref.child(bandobastId)
    for y in personList:
        
        
        personId=y[0]
        personName=y[1]
        personContact=y[3]
        personRank=y[2]
        
        

        person.update({
            personId:{
            'Name':personName,
            'Contact':personContact,
            'Rank':personRank,
            }
        })
    
    print("All Process Done")


def write_value(value):
    with open('IdText','w') as f:
        f.write(value)
def read_value():
    with open('IdText','r') as f:
        r=f.readlines()
        return r