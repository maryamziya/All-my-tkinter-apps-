from tkinter import *

window = Tk()
window.config(padx=70)

# Here is the step-by-step instruction flow for the **Basic Quiz with Options** project, focusing on using `Radiobutton` and `StringVar`.
#
# ***
#
# 🧠 Basic Quiz App Instruction Flow
#
# This project requires you to link several radio buttons to a single variable so only one can be selected at a time, and then check that variable's value against the correct answer.
#
# ### Step 1: Initialize the Application and Control Variable
#
# 1.  **Import Tkinter:** Start your script with `from tkinter import *`.
# 2.  **Create Main Window:** Set up the main `Tk()` window and give it a title (e.g., "Quiz Time!").
# 3.  **Define Control Variable:** Create a **`StringVar`** object. This variable will be automatically updated by the `Radiobutton`s and will store the user's current selection.
#     * *Hint:* `selected_answer = StringVar()`
selected_answer = StringVar()
# ### Step 2: Create the Widgets
#
# 1.  **Question Label:** Create a **`Label`** widget to display the quiz question (e.g., "What is the capital of France?").
question1 = Label(text="What is my favorite color?")
question2 = Label(text="What is my favorite fruit?")
question3 = Label(text="Who is my best friend?")
question4 = Label(text="What game does I like better?")
# 2.  **Result Label:** Create a second **`Label`** widget (initially empty or set to "Make a selection.") where the final result ("Correct!" or "Incorrect!") will be displayed.
result = Label(text="Make a selection")
# 3.  **Radiobuttons:** Create three or four **`Radiobutton`** widgets for the options (e.g., "Paris," "Rome," "Berlin").
#     * **Crucial Setup:** For *each* `Radiobutton`:
#         * Set the `variable` option to your **`StringVar`** created in Step 1.
#         * Set the **`value`** option to a unique identifier (a string or number) for that specific option. This is the value that will be stored in the `StringVar` when this button is selected.
    #     * *Hint:* The correct answer's `value` must match the string you will use in your checking function.


def check_ans1():
    user_choice = selected_answer.get()
    if user_choice == "13":
        result.config(text="Correct!")
    else:
        result.config(text="Wrong!")

def check_ans2():
    user_choice = selected_answer.get()
    if user_choice == "24":
        result.config(text="Correct!")
    else:
        result.config(text="Wrong!")

def check_ans3():
    user_choice = selected_answer.get()
    if user_choice == "33":
        result.config(text="Wrong!")
    else:
        result.config(text="Correct!")

def check_ans4():
    user_choice = selected_answer.get()
    if user_choice == "44":
        result.config(text="Correct!")
    else:
        result.config(text="Wrong!")



answer11 = Radiobutton(text="Blue",variable=selected_answer,value=11,command=check_ans1)
answer12 = Radiobutton(text="Pink",variable=selected_answer,value=12,command=check_ans1)
answer13 = Radiobutton(text="White",variable=selected_answer,value=13,command=check_ans1)
answer14 = Radiobutton(text="Black",variable=selected_answer,value=14,command=check_ans1)

answer21 = Radiobutton(text="Strawberry",variable=selected_answer,value=21,command=check_ans2)
answer22 = Radiobutton(text="Watermelon",variable=selected_answer,value=22,command=check_ans2)
answer23 = Radiobutton(text="Peach",variable=selected_answer,value=23,command=check_ans2)
answer24 = Radiobutton(text="Mango",variable=selected_answer,value=24,command=check_ans2)

answer31 = Radiobutton(text="Ella",variable=selected_answer,value=31,command=check_ans3)
answer32 = Radiobutton(text="Sloane",variable=selected_answer,value=32,command=check_ans3)
answer33 = Radiobutton(text="Emma",variable=selected_answer,value=33,command=check_ans3)
answer34 = Radiobutton(text="Elena",variable=selected_answer,value=34,command=check_ans3)

answer41 = Radiobutton(text="Steal a brainrot",variable=selected_answer,value=41,command=check_ans4)
answer42 = Radiobutton(text="Nintendo",variable=selected_answer,value=42,command=check_ans4)
answer43 = Radiobutton(text="Five star",variable=selected_answer,value=43,command=check_ans4)
answer44 = Radiobutton(text="Playing with friends",variable=selected_answer,value=44,command=check_ans4)
# ### Step 3: Define the Check Answer Function
# 1.  **Define the function:** Create a function named `check_answer`.
# 2.  **Get Selection:** Inside the function, use the `.get()` method on your **`StringVar`** to retrieve the value of the currently selected `Radiobutton`.
#     * *Example:* `user_selection = selected_answer.get()`
# 3.  **Check Condition:** Write an `if/else` block to compare the `user_selection` to the known correct `value`.
#     * *Hint:* If the correct answer is "Paris," the check is `if user_selection == "Paris":`
# 4.  **Update Result Label:** Use the `.config()` (or `[]` dictionary syntax) method on the **Result Label** to update its `text` option to display "Correct!" or "Incorrect!" based on the condition.
#
# ### Step 4: Link and Layout
# 1.  **Link Button:** Set the `command` option of the **"Submit Answer" Button** to the `check_answer` function.
# 2.  **Layout Widgets:** Use the **`grid()`** layout manager (or another method) to arrange the components neatly:
#     * Place the Question Label at the top.
question1.grid(row=0,column=0)
question2.grid(row=0,column=1)
question3.grid(row=0,column=2)
question4.grid(row=0,column=3)
#     * Place the Radiobuttons vertically below the question (one per row).
answer11.grid(row=1,column=0)
answer12.grid(row=2,column=0)
answer13.grid(row=3,column=0)
answer14.grid(row=4,column=0)

answer21.grid(row=1,column=1)
answer22.grid(row=2,column=1)
answer23.grid(row=3,column=1)
answer24.grid(row=4,column=1)

answer31.grid(row=1,column=2)
answer32.grid(row=2,column=2)
answer33.grid(row=3,column=2)
answer34.grid(row=4,column=2)

answer41.grid(row=1,column=3)
answer42.grid(row=2,column=3)
answer43.grid(row=3,column=3)
answer44.grid(row=4,column=3)

#     * Place the Submit Button below the options.
#     * Place the Result Label last.


result.grid(row=0,column=4)
# 3.  **Run Main Loop:** Call `window.mainloop()` to display the application.

window.mainloop()
# ***
#
# Would you like me to provide the complete Python code for this second project to compare with your solution
                                                                                                                                                                                                                                                                                                                                            