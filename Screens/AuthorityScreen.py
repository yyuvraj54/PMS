from tkinter import *
# from function import image
from Screens.function import image ,dataAdapter
from PIL import ImageTk, Image
import os





def openCreateAccound():
    os.system('python3 Screens/newAuthScreen.py')
    
def logIn():
    enteredUsername=tokenValue.get()
    enteredPassword=password.get()

    check=dataAdapter.Authentication(enteredUsername,enteredPassword)
    check=check+","+enteredUsername
    if(check):
        errorLabel.config(text="Done",fg="green")
        dataAdapter.write_value(check)
        authRoom.destroy()

    else:
        errorLabel.config(text="Username or password is incorrect!",fg="red")


    
    

authRoom=Tk()
authRoom.geometry("500x500+700+100")
authRoom.minsize("500","500")
authRoom.maxsize("500","500")
authRoom.title("BandobastSoftware")

centerFrame=Frame(authRoom , background="white")
centerFrame.pack(padx=10,pady=10,fill=BOTH,expand=True)

erathImage= Image.open('Icons/earthlogo.png')
erathImageResize=image.ImageResize(erathImage,150,150)
imageLabelEarth=Label(centerFrame , image=erathImageResize)
imageLabelEarth.pack(pady=10)


tokenFrame=Frame(centerFrame)
tokenFrame.pack()
Label(tokenFrame,text="TokenId:").pack()

tokenValue=StringVar()
enterToken=Entry(tokenFrame,textvariable=tokenValue)
enterToken.pack(side="top")


passwordFrame=Frame(centerFrame)
passwordFrame.pack(pady=20)
Label(passwordFrame,text="Password").pack()
password=StringVar()
enterpassword=Entry(passwordFrame,show = '*',textvariable=password)
enterpassword.pack(side="top")

errorLabel=Label(centerFrame,text="")
errorLabel.pack()

logInBtn=Button(centerFrame,text=" LogIn ",command=logIn)
logInBtn.pack(side="top")

Label(centerFrame,text="or").pack(pady=10)

createBandobastArea=Button(centerFrame,text=" Create new Token ",command=openCreateAccound)
createBandobastArea.pack(side="top")


authRoom.mainloop()


