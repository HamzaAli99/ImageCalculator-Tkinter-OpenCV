import tkinter
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import cv2 as cv
import numpy

photo = []

def simage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(),title = 'select',filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All files","*.")))
    img = Image.open(fln)
    img.thumbnail((400,500))
    open_cv_image = numpy.array(img) 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    open_cv_image = cv.resize(open_cv_image, (400,500))
    photo.append(open_cv_image)
    imgBrowse = tkinter.Tk()
    img = ImageTk.PhotoImage(img, master = imgBrowse)
    panel = tkinter.Label(imgBrowse, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    render = Label(image=img)
    img.image = render
    
def addcv():
    print(photo[0])
    #img1=cv.imread(photo[0])
    #img2=cv.imread(photo[1])
    added=cv.add(photo[0],photo[1])
    #added = cv.cvtColor(added,cv.COLOR_BGR2RGB)
    added = cv.cvtColor(added, cv.COLOR_BGR2RGB)
    added = Image.fromarray(added)
    added.thumbnail((400,500))
    outputWindow = tkinter.Tk()
    added = ImageTk.PhotoImage(added, master = outputWindow)
    
    panel = tkinter.Label(outputWindow, image = added)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    render = tkinter.Label(image=added)
    added.image = render
    
def subcv():
    subtracted = cv.subtract(photo[0],photo[1])
    subtracted = cv.cvtColor(subtracted, cv.COLOR_BGR2RGB)
    subtracted = Image.fromarray(subtracted)
    subtracted.thumbnail((400,500))
    outputWindow = tkinter.Tk()
    subtracted = ImageTk.PhotoImage(subtracted, master = outputWindow)
    
    panel = tkinter.Label(outputWindow, image = subtracted)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    render = tkinter.Label(image=subtracted)
    added.image = render


windoww = tkinter.Tk()
windoww.geometry("500x250")
windoww.configure(bg='#f8e0cf')
windoww.title("Image calculator")
top_frame = tkinter.Frame(windoww).pack(fill=BOTH)
bottom_frame = tkinter.Frame(windoww).pack()#side = "bottom")
label = tkinter.Label(windoww,text = 'My image calculator',font =('Arial Bold',10),bg='#f8e0cf').pack()
label1 = tkinter.Label(windoww,text = 'Submitted by: HAMZA ALI , B17158021',font =('Arial Bold',10),bg='#f8e0cf').pack(side = 'bottom')
bt = tkinter.Button(top_frame,text = 'Browse',command = simage).pack(side = 'left',padx = 10)

ent = tkinter.Entry(top_frame,bg='#f8e0cf').pack(side = 'left',padx = 5)
bt1 = tkinter.Button(bottom_frame,text = 'Browse',command = simage).pack(side = 'left',padx = 20)
print(type(bt1))
ent1 = tkinter.Entry(bottom_frame,bg='#f8e0cf').pack(side='left',pady = 2)

bt2 = tkinter.Button(top_frame,text = 'add', command = addcv).pack(side = 'left',padx = 10)   
bt2 = tkinter.Button(bottom_frame,text = 'sub', command = subcv).pack(side = 'right',padx = 0)
windoww.mainloop()