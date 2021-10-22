from tkinter import * 
import sqlite3

root = Tk()
root.title('Hola mundo: Todo List')
root.geometry('500x500')

conn = sqlite3.connect('todo.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")

conn.commit()

def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE id = ? ",(id, ))
        conn.commit()
        renderToDo()

    return _remove

def complete(id):
    def _complete():
        todo = c.execute("SELECT * FROM todo WHERE id = ? ",(id, )).fetchone()
        c.execute("UPDATE todo SET completed = ? WHERE id = ? ",(not todo[3],id))
        conn.commit()
        renderToDo()

    return _complete
    

def renderToDo():
    rows = c.execute("SELECT * FROM todo").fetchall()

    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(0,len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        color = '#666666' if completed else '#666666'
        ch = Checkbutton(frame,text=description,fg=color,width=42,anchor='w',command=complete(id))
        ch.grid(row=i,column=0,sticky='w')
        btnEliminar = Button(frame,text='Eliminar',command=remove(id))
        btnEliminar.grid(row=i,column=1)
        ch.select() if completed else ch.deselect()

def addToDo():
    todo = e.get()

    if todo:
        c.execute("""
        INSERT INTO todo (description,completed) VALUES(?,?)
        """,(todo,False))
        conn.commit()
        e.delete(0, END)
        renderToDo()
    else:
        pass
    

l = Label(root,text='Tarea')
l.grid(row=0,column=0)

e = Entry(root,width=40)
e.grid(row=0,column=1)

btn = Button(root,text='Agregar',command=addToDo)
btn.grid(row=0,column=2)

frame = LabelFrame(root,text='Mis Tareas', padx=5,pady=5)
frame.grid(row=1,column=0,columnspan=3,sticky='nswe',padx=5)

e.focus()

root.bind('<Return>',lambda x:addToDo())

renderToDo()

root.mainloop()