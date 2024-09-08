from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def deleteTask():
    lb.delete(ANCHOR)

def on_enter(e):
    e.widget['background'] = '#F39C12'

def on_leave(e):
    e.widget['background'] = '#E67E22'

ws = Tk()
ws.geometry('500x500+500+200')
ws.title('Enhanced To-do List')
ws.config(bg='#2C3E50')
ws.resizable(width=False, height=False)

frame = Frame(ws, bg='#2C3E50')
frame.pack(pady=20)

lb = Listbox(
    frame,
    width=30,
    height=8,
    font=('Helvetica', 18),
    bd=0,
    fg='#2C3E50',
    selectbackground='#E67E22',
    selectforeground="#FFFFFF",
    highlightthickness=0,
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

TASK_LIST = ['Assignment', 'Projects', 'Study']

for item in TASK_LIST:
    lb.insert(END, item)

sb = Scrollbar(frame, bg='#E67E22')
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('Helvetica', 18),
    fg='#2C3E50',
    bg='#ECF0F1',
    bd=0,
    insertbackground='#2C3E50',
    justify='center'
)
my_entry.pack(pady=20, ipadx=10, ipady=10)

button_frame = Frame(ws, bg='#2C3E50')
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Helvetica', 14),
    bg='#E67E22',
    fg='white',
    padx=20,
    pady=10,
    bd=0,
    highlightthickness=0,
    activebackground='#D35400',
    cursor="hand2"
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

addTask_btn.bind("<Enter>", on_enter)
addTask_btn.bind("<Leave>", on_leave)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Helvetica', 14),
    bg='#E67E22',
    fg='white',
    padx=20,
    pady=10,
    bd=0,
    highlightthickness=0,
    activebackground='#D35400',
    cursor="hand2"
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn.bind("<Enter>", on_enter)
delTask_btn.bind("<Leave>", on_leave)

addTask_btn.config(command=newTask)
delTask_btn.config(command=deleteTask)

ws.mainloop()
