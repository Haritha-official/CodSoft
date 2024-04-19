#To-Do-List APPLICATION that performs create, update and track the Lists
from tkinter import *
window = Tk()
#Naming it has To-Do-List
window.title("To-Do-List")
#Set the size 
window.geometry("500x550")
#Set the color
window.configure(bg='pink')

tasks = {}
#Choice Label
l1 = Label(window, text='ENTER A NEW TASK:', bg='pink', font=10)
l1.grid(row=0, column=0, padx=10, pady=10, sticky='e')
#Entry box
task_entry = Entry(window, width=30)
task_entry.grid(row=0, column=1, padx=10, pady=10)
#Function to add new task
def add_task():
    task = task_entry.get()
    if task:
       tasks[task] = False
       update(tasks)
       task_entry.delete(0, END)
#Function to mark the Completed task
def update(tasks):
    listbox.delete(0, END)  # Clear the listbox
    for task, completed in tasks.items():
        if completed:
           listbox.insert(END, f"\u2713 {task}")
        else:
            listbox.insert(END, task)


def mark():
    index = listbox.curselection()
    if index:
        task = listbox.get(index[0])
        # Update completion status in the dictionary
        tasks[task] = True
        update(tasks)
#Function to track the task
def track():
    listbox.delete(0, END)  # Clear the listbox
    for task, completed in tasks.items():
        if completed:
           listbox.insert(END, f"\u2713 {task}")
           listbox.itemconfig(END, {'fg': 'green'})
        else:
            listbox.insert(END, task)
#Function for Deleting a task
def delete():
    index = listbox.curselection()
    if index:
       task = listbox.get(index[0])
       del tasks[task]  # Remove the selected task from the dictionary
       update(tasks)
#Add listbox
listbox_font = ('Helvetica', 12)
listbox = Listbox(window, width=40, font=listbox_font)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
#Add buttons for the task
b1 = Button(window, text='New Task', bg='skyblue', command=add_task, padx=15, pady=8, font=6)
b1.grid(row=3, column=0, columnspan=2, padx=(10, 5), pady=10, sticky='w')  

b2 = Button(window, text='Mark Task', bg='skyblue', command=mark, padx=15, pady=8, font=6)
b2.grid(row=4, column=0, columnspan=2, padx=(10, 5), pady=10, sticky='w')

b3 = Button(window, text='Track', bg='skyblue', command=track, padx=15, pady=8, font=6)
b3.grid(row=5, column=0, columnspan=2, padx=(10, 5), pady=10, sticky='w')

b4 = Button(window, text='Remove task', bg='brown', command=delete, padx=15, pady=8, font=6)
b4.grid(row=6, column=0, columnspan=2, padx=(10, 5), pady=10, sticky='w')


window.mainloop()
