#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade Pillow
#para usar la libreria

from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')

#image = Image.open('cascada.jpg')
#image.show()

img = ImageTk.PhotoImage(Image.open('cascada.jpg'))
l = Label(image=img)
l.pack()

root.mainloop()