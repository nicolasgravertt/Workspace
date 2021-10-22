from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Carrusel')

img1 = ImageTk.PhotoImage(Image.open('Images/1.png'))
img2 = ImageTk.PhotoImage(Image.open('Images/2.png'))
img3 = ImageTk.PhotoImage(Image.open('Images/3.png'))
img4 = ImageTk.PhotoImage(Image.open('Images/4.png'))

lista = [img1,img2,img3,img4]
l = Label(root,image=img1)
l.grid(row=0,column=0,columnspan=3)

def forward(img_num):
    global l
    global btnForward
    global btnBackward

    l.grid_forget()
    l = Label(root,image=lista[img_num])
    btnBackward = Button(root,text='<-',command=lambda:backward(img_num - 1))
    btnForward = Button(root,text='->',command=lambda:forward(img_num + 1))

    if img_num == 3:
        btnForward = Button(root,text='N/A',state='disable')

    l.grid(row=0,column=0,columnspan=3)
    btnBackward.grid(row=1,column=0)
    btnForward.grid(row=1,column=2)

def backward(img_num):
    global l
    global btnForward
    global btnBackward

    l.grid_forget()
    l = Label(root,image=lista[img_num])
    btnBackward = Button(root,text='<-',command=lambda:backward(img_num - 1))
    btnForward = Button(root,text='->',command=lambda:forward(img_num + 1))

    if img_num == 0:
        btnBackward = Button(root,text='N/A',state='disable')

    l.grid(row=0,column=0,columnspan=3)
    btnBackward.grid(row=1,column=0)
    btnForward.grid(row=1,column=2)

btnBackward = Button(root,text='N/A',state='disable')
btnForward = Button(root,text='->', command=lambda:forward(1))

btnBackward.grid(row=1,column=0)
btnForward.grid(row=1,column=2)



root.mainloop()