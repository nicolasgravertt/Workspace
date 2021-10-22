from tkinter import * 

root = Tk()
root.title('Hola Mundo')

r = IntVar()
r.set('2')

CHANCHITOS = [
    ('FelizzzZz','Feliz'),
    ('TristeeeASD','Triste'),
    ('AmargadoaASD','Amargado'),
    ('WolfgangaAAAa','Wolfgang')
]

chanchito = StringVar()
chanchito.set('Wolfgang')


def seleccionar():
    print(chanchito.get())

for text,chancho in CHANCHITOS:
    Radiobutton(root,text=text,variable=chanchito,value=chancho,command=seleccionar).pack()

Label(root,textvariable=chanchito).pack()


root.mainloop()