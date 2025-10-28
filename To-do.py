

## Simple To-Do List App Instructions

### Step 1: Set up the Main Window and Widgets

# 1.  **Import Tkinter:** Start your script by importing the necessary module.
#     ```python
from tkinter import *
# 2.  **Create the Main Window:** Instantiate the main window (`Tk()`) and give it a title.
windows = Tk()
windows.minsize(height=500,width=300)
windows.config(padx=700,pady=70)
to_do = Label(text="TO-DO",font=("Times New Roman",24,"bold"))
lists = Label(text="LIST",font=("Times New Roman",24,"bold"))
to_do.grid(row=0,column=0)
lists.grid(row=1,column=0)
# 3.  **Create the Entry Widget:** Make an **`Entry`** widget where the user will type a new task.
#       * *Hint:* This is where you get the input text.
task = Entry()
# 4.  **Create the Listbox Widget:** Create the **`Listbox`** widget to display the tasks. Give it a reasonable height.
all_tasks = Listbox(windows,height = 20)
# 5.  **Create the Buttons:** Create two **`Button`** widgets:
#       * One labeled **"Add Task"**.
def add_tasks():
      all_tasks.insert(END, task.get())
      task.delete(0,END)
add_task = Button(text="Add Text",command=add_tasks)
#       * One labeled **"Delete Selected"**.
def delete_task():
      all_tasks.delete(all_tasks.curselection())
delete_selected = Button(text="Delete Selected",command=delete_task)

### Step 2: Define the `add_task` Function

# 1.  **Define the function:** Create a function named `add_task`.
# 2.  **Get the input:** Inside this function, use the `.get()` method on your **`Entry`** widget to retrieve the text the user typed.
# 3.  **Insert into Listbox:** Use the `.insert()` method of the **`Listbox`** to add the retrieved text.
#       * *Hint:* You should insert the new task at the end of the list. Use the constant `END` for the index.
#       * Example: `my_listbox.insert(END, task_text)`
#-----------------------------------------------
# 4.  **Clear the Entry:** After adding the task, use the `.delete()` method on the **`Entry`** widget to clear the input field, ready for the next task.
#       * *Hint:* You need to delete from index `0` to `END`.

### Step 3: Define the `delete_task` Function

# 1.  **Define the function:** Create a function named `delete_task`.
# 2.  **Delete from Listbox:** Use the `.delete()` method of the **`Listbox`** to remove the selected item.
#       * *Hint:* To delete the *currently selected* item, use the constant `ANCHOR` for the index.
#       * Example: `my_listbox.delete(ANCHOR)`
#       * *Note:* Using `ANCHOR` works well for single selection.
#done up 1
### Step 4: Link Functions to Buttons

# 1.  **Configure "Add Task" Button:** Set the `command` option of the "Add Task" button to the `add_task` function.
# 2.  **Configure "Delete Selected" Button:** Set the `command` option of the "Delete Selected" button to the `delete_task` function.
#done up 1
### Step 5: Layout the Widgets
#
# 1.  **Use `grid()` Layout:** Use the **`grid()`** manager (like you did in your practice) to arrange the widgets neatly.
#       * Place the **`Entry`** and the **"Add Task" Button** in the first row (e.g., row 0, column 0 and 1).
task.grid(row=2,column=0)
#       * Place the **`Listbox`** in the second row (e.g., row 1, spanning multiple columns if needed, using `columnspan`).

all_tasks.grid(row=3,column=0)
add_task.grid(row=2,column=1)
#       * Place the **"Delete Selected" Button** in the third row (e.g., row 2).
delete_selected.grid(row=4,column=0)
#       * *Hint:* The `Listbox` will look better if it fills the width, so consider using `sticky="ew"` or `columnspan`.
### Step 6: Run the Main Loop

# 1.  **Call `mainloop()`:** Don't forget to call `window.mainloop()` at the end of your script to make the application run and wait for events.
windows.mainloop()