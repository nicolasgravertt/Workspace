from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo: Archivos')

#root.filename = filedialog.askopenfilename(title='elige una foto',filetypes=(("Archivos PNG","*.png"),('Todos','*')))
#l = Label(root,text=root.filename).pack()
#img = Image.open(root.filename)
#imgtk = ImageTk.PhotoImage(img)
#l2 = Label(root,image=imgtk).pack()

def open():
    global imgtk
    root.filename = filedialog.askopenfilename(title='elige una foto',filetypes=(("Archivos PNG","*.png"),('Todos','*')))
    l = Label(root,text=root.filename).pack()
    img = Image.open(root.filename)
    imgtk = ImageTk.PhotoImage(img)
    l2 = Label(root,image=imgtk).pack()


btn = Button(root,text='Cargar IMG',command=open).pack()
root.mainloop()