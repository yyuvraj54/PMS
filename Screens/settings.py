from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Settings')
root.iconbitmap('./favicon.ico')
root.geometry('400x500')

link = ImageTk.PhotoImage(Image.open('./link.png'))
meta = ImageTk.PhotoImage(Image.open('./meta.png'))
language = ImageTk.PhotoImage(Image.open('./language.png'))
save = ImageTk.PhotoImage(Image.open('./Save.png'))

Link = Button(image=link, pady=50, borderwidth=0).pack(
    pady=(100, 5))
Meta = Button(image=meta, pady=40, borderwidth=0).pack(
    pady=5)
Language = Button(image=language, pady=40, borderwidth=0).pack(
    pady=5)
Save = Button(image=save, pady=40, borderwidth=0).pack(
    pady=(80, 50))

root.mainloop()
