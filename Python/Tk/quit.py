from tkinter import *

root = Tk()
root.configure(background='#333333')
root.geometry('386x168')
root.title('Boton de Salida')

exit = Button(root,text='Salir',command=root.quit)
exit.pack()

root.mainloop()