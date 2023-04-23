from tkinter import *
import tkintermapview
import time
from Screens.function import image ,dataAdapter
from PIL import ImageTk, Image
from threading import Thread




personCoordinates=[]
username=""
bandobastId=""
personId=[]
hostlora=[]
allData=[]



def getSelectedItems(event):

    try:
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            
            for x in allData:
                if x[0]==data:
                    detailLabel.config(text="Person Details",fg="red")
                    personIdLabel.config(text="Person Id: "+x[0])
                    personName.config(text="Person Name:"+x[1])
                    personContact.config(text="Person Contact: "+x[3])
                    personRank.config(text="Person Rank: "+x[2]) 
                    logLabel.config(text="Logitude: "+str(x[4])) 
                    latLabel.config(text="Latitude: "+str(x[5]))
            
    except(Exception):print(Exception)    

def setlocation():

    try:
        map_widget.set_position(hostlora[0], hostlora[1]) 
        map_widget.set_zoom(50)
    except Exception as e:print(e)


def updateLocation():
    global map_widget ,personId, hostLoraMark
    while(True):
        time.sleep(2)
        
        try:
            newlocation=[]
            for singlePerson in personId:
                dataAdapter.getMarkLocationCoordinates(username,bandobastId,singlePerson,newlocation)
            
            map_widget.delete_all_marker()
            hostLoraMark=map_widget.set_marker(hostlora[0], hostlora[1], text="Host Lora Device")
            
            # hostLoraMark.change_icon(loraimage)
            for dataset in newlocation:
                map_widget.set_marker(dataset[1], dataset[2], text=dataset[0])
            newlocation.clear()
        except Exception as e:print(e)    



def LoadData():
    global username,bandobastId ,personId ,hostlora
    authValue=dataAdapter.read_value()
    authval=authValue[0].split(',')
    username=authval[1]
    bandobastId=authval[0]
    personnelDetails=dataAdapter.getPersonDataFilesFromRuntime(authval[1],authval[0])
    for personID in personnelDetails:
        if(personID!='lat' and personID!='log'):personListbox.insert(END,personID)
        dataAdapter.getContactDetails(username,bandobastId,personID,allData)
        personId.append(personID)
        locationMarker = Thread(target=dataAdapter.getMarkLocationCoordinates,args=(authval[1], authval[0],personID,personCoordinates))
        locationMarker.start()
    hostlora=dataAdapter.getHostLoraCoordinates(username,bandobastId)
    
    

    




guiBackGround="#98999B"

liveScreen=Tk()
liveScreen.geometry("1000x750+500+150")
liveScreen.minsize("1000","750")
liveScreen.maxsize("1000","750")
liveScreen.title("Live Screen")

window=Frame(liveScreen,bg=guiBackGround)
window.pack(padx=10,pady=10,expand=True,fill=BOTH)

mapsFrame=Frame(window,bg=guiBackGround)
mapsFrame.pack(padx=5,pady=5)
map_widget = tkintermapview.TkinterMapView(mapsFrame, width=980, height=450, corner_radius=60)
map_widget.pack(padx=5,pady=5)
map_widget.set_position(28.6128938, 77.3595316)

# loraImg= Image.open('Icons/lora.png')
loraimage = PhotoImage(file = "Icons/lora.png")
# loraImgResize=image.ImageResize(loraImg,50,50)


toolsFrame=Frame(window)
toolsFrame.pack(expand=True,fill=BOTH)

leftwidgetFrame=Frame(toolsFrame)
leftwidgetFrame.pack(side=LEFT)

stateFrame=Frame(leftwidgetFrame)
stateFrame.pack()
indicatorStatusLabel=Label(stateFrame,text="State Indicator: All Good")
indicatorStatusLabel.pack()


ListboxFrame=Frame(leftwidgetFrame,)
ListboxFrame.pack()




PersonListboxFrame=Frame(ListboxFrame)
PersonListboxFrame.pack(side=LEFT)
Label(PersonListboxFrame,text="Ground Personnels").pack()
personListbox=Listbox(PersonListboxFrame,width=60)
personListbox.pack(padx=5)
personListbox.bind("<<ListboxSelect>>", getSelectedItems)

# outOfRangeListboxFrame=Frame(ListboxFrame)
# outOfRangeListboxFrame.pack(side=LEFT)
# Label(outOfRangeListboxFrame,text="Risk Factor").pack()
# outOfRangeListbox=Listbox(outOfRangeListboxFrame,width=20)
# outOfRangeListbox.pack(padx=5)

# riskRangeListboxFrame=Frame(ListboxFrame)
# riskRangeListboxFrame.pack(side=LEFT)
# Label(riskRangeListboxFrame,text="Out of Range").pack()
# riskRangeListbox=Listbox(riskRangeListboxFrame,width=20)
# riskRangeListbox.pack(padx=5)

detailsFrame=Frame(toolsFrame)
detailsFrame.pack(side=LEFT,expand=True)


middleWidgetFrame=Frame(toolsFrame)
middleWidgetFrame.pack(side=LEFT,expand=True,fill=Y)


buzzerImage= Image.open('Icons/buzzerOffstate.png')
buzzerImageResize=image.ImageResize(buzzerImage,100,100)
imageLabelBuzzer=Label(middleWidgetFrame , image=buzzerImageResize)
imageLabelBuzzer.pack(pady=10,side=BOTTOM)


frameBandobastAreaPersonDetails=Frame(detailsFrame)
frameBandobastAreaPersonDetails.pack(pady=5,expand=True)

detailLabel=Label(frameBandobastAreaPersonDetails,text="")
detailLabel.pack()
personIdLabel=Label(frameBandobastAreaPersonDetails,text="")
personIdLabel.pack(anchor=NW)
personName=Label(frameBandobastAreaPersonDetails,text="")
personName.pack(anchor=NW)
personRank=Label(frameBandobastAreaPersonDetails,text="")
personRank.pack(anchor=NW)
personContact=Label(frameBandobastAreaPersonDetails,text="")
personContact.pack(anchor=NW)
logLabel=Label(frameBandobastAreaPersonDetails,text="")
logLabel.pack(anchor=NW)
latLabel=Label(frameBandobastAreaPersonDetails,text="")
latLabel.pack(anchor=NW)



Btnframe=Frame(middleWidgetFrame)
Btnframe.pack(padx=5,pady=5,side="bottom")
# showListPoliceBtn=Button(Btnframe,text="Show List of policeman")
# showListPoliceBtn.pack()


showListPoliceBtn=Button(Btnframe,text="Show Lora Details",command=setlocation)
showListPoliceBtn.pack()


# showListPoliceBtn=Button(Btnframe,text="Review")
# showListPoliceBtn.pack()


loadDataRunner= Thread(target=LoadData)
loadDataRunner.start()

locationUpdaterRunner = Thread(target=updateLocation)
locationUpdaterRunner.start()
liveScreen.mainloop()

