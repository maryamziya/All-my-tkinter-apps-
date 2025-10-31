# Yes, let's explore the **`Canvas`** widget\! Here are the step-by-step instructions for building the **Simple Color Picker** app.
#
# -----
#
# ## 4\. Simple Color Picker Instructions (Canvas) 🎨
#
# This exercise focuses on using the `Canvas` widget for visual display and changing its properties dynamically.
#
# ### Step 1: Set up the Window and Widgets
#
# 1.  **Import Tkinter:** Start with the standard import.
#     ```python
from tkinter import *
from turtledemo.paint import changecolor

#     ```
# 2.  **Create the Main Window:** Instantiate `Tk()` and give it a title.
windows = Tk()
# 3.  **Create the Canvas:** Create a **`Canvas`** widget
#       * Set its `height` and `width` to a significant size (e.g., 200).
#       * Give it an initial background color using the `bg` option (e.g., `bg="lightgray"`).
#       * *Hint:* This is the area that will change color.

# ### Step 2: Define the `change_color` Function
#
# 1.  **Define the function:** Create a function named `change_color`.
# 2.  **Get the Input:** Use the `.get()` method on your **`Entry`** widget to retrieve the user's color input.
# 3.  **Attempt to Change Canvas Color:** Use the `.config()` (or `.configure()`) method on the **`Canvas`** widget to change its background color (`bg`).
#       * Example: `my_canvas.config(bg=color_input)`
# 4.  **Implement Error Handling (Crucial\!):** If the user types an invalid color name (e.g., "fdsfds"), the program will crash when it tries to configure the canvas.
#       * Use a Python **`try...except`** block around the `.config()` call.
#       * In the `except` block, print a message to the console (e.g., "Invalid color entered\!") or update a status label in the window.
#
def change_color():
    label.config(text="")
    color_input = color.get()
    try:
        canvas.config(bg=color_input)
    except Exception as e:
        label.config(text="Invalid input!")


canvas = Canvas(height=200,width=200,bg="lightgray")
canvas.pack()
# 4.  **Create the Entry:** Create an **`Entry`** widget where the user will type a color name (like "red", "blue", or a hex code like "\#FF5733").
color = Entry()
color.pack()

label = Label(text="")
label.pack()

# 5.  **Create the Button:** Create a **`Button`** labeled "Change Color."
#
change_colors = Button(text="Change Color",command=change_color)
change_colors.pack()
#

# -----
#
# ### Step 3: Link and Layout the Widgets
#
# 1.  **Link the Command:** Set the **`command`** option of the "Change Color" **`Button`** to your `change_color` function.
# 2.  **Layout Manager:** Use the **`grid()`** manager.
#       * Place the **`Canvas`** near the top (e.g., Row 0). It will look better if it spans two columns (`columnspan=2`) and is centered.
#       * Place the **`Entry`** and the **`Button`** side-by-side below the canvas (e.g., Row 1, Column 0 and Column 1).
#       * *Optional:* Add padding (`padx`, `pady`) to make the interface look cleaner.
#
# -----
#
# ### Step 4: Run the Main Loop
#
# 1.  **Call `mainloop()`:** Add `window.mainloop()` at the end of your script to run the application.
windows.mainloop()
# Let me know when you're ready for the final practice problem, **Layout Manager Challenge (Using `Pack` and `Place`)**, or if you'd like the solution code for the color picker\!