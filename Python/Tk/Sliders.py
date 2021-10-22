from tkinter import * 

root = Tk()
root.title('Hola mundo:Sliders')

vertical = Scale(root,from_=0,to=200,command=lambda x:enviar())
vertical.pack()

horizon = Scale(root,from_=0,to=200,orient=HORIZONTAL)
horizon.pack()

def enviar():
    hor = horizon.get()
    ver = vertical.get()
    print(str(hor) + ' ' + str(ver))

btn = Button(root,text='Enviar',command=enviar).pack()

root.mainloop()