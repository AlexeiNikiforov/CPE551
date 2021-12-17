from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Uh Oh", "Please enter a task")

def deleteTask():
    lb.delete(ANCHOR)

def editTask():
   for item in lb.curselection():
      lb.delete(item)
      task = my_entry.get()
      lb.insert(END, task)
      my_entry.delete(0, "end")

def highPriorityTask():
   for item in lb.curselection():
      position = str(item)
      lb.itemconfig(position,bg = 'YELLOW')     

    
ws = Tk() #creates the box initially
ws.geometry('1000x550+500+200')
ws.title('To Do List')
ws.config(bg='#223441')
ws.resizable(width=True, height=True)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox( #displays the list
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(#entry box
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(#adds a new task
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(#deletes an existing task
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

editTask_btn = Button(#deletes an existing task
    button_frame,
    text='Edit Task',
    font=('times 14'),
    bg='#FFFC2B',
    padx=20,
    pady=10,
    command=editTask
)
editTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

highPriorityTask_btn = Button(#deletes an existing task
    button_frame,
    text='Highlight Task',
    font=('times 14'),
    bg='#FF2BFF',
    padx=20,
    pady=10,
    command=highPriorityTask
)
highPriorityTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()