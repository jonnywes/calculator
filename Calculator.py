import tkinter as tk
from tkinter import * 

#variables
problem = ""

def quit_(window):
    return window.destroy

def push(num):
    global problem

    problem = problem + str(num)

    equation.set(problem)

def error_check():
    try:
        global problem

        total = str(eval(problem))

        equation.set(total)

        problem =  ""
    except:
        equation.set(" error ")
        problem = ""

def clear():
    global problem
    problem =""
    equation.set("")


#GUI
#create Instance
root = tk.Tk()
#Add title to GUI
root.title('CALCULATOR')

root.configure(background="grey")
root.geometry("280x180")
#var
equation = StringVar()
problem_box = Entry(root, textvariable=equation)
problem_box.grid(columnspan= 5, ipadx=100)
equation.set('')
#Integer Buttons
button1 = Button( root, text=' 1 ', fg='black', bg='white', command=lambda: push(1), height=1, width=7)
button1.grid(row=3, column=0)

button2 = Button( root, text=' 2 ', fg='black', bg='white', command=lambda: push(2), height=1, width=7)
button2.grid(row=3, column=1)

button3 = Button( root, text=' 3 ', fg='black', bg='white', command=lambda: push(3), height=1, width=7)
button3.grid(row=3, column=2)

button4 = Button( root, text=' 4 ', fg='black', bg='white', command=lambda: push(4), height=1, width=7)
button4.grid(row=4, column=0)

button5 = Button( root, text=' 5 ', fg='black', bg='white', command=lambda: push(5), height=1, width=7)
button5.grid(row=4, column=1)

button6 = Button( root, text=' 6 ', fg='black', bg='white', command=lambda: push(6), height=1, width=7)
button6.grid(row=4, column=2)

button7 = Button( root, text=' 7 ', fg='black', bg='white', command=lambda: push(7), height=1, width=7)
button7.grid(row=5, column=0)

button8 = Button( root, text=' 8 ', fg='black', bg='white', command=lambda: push(8), height=1, width=7)
button8.grid(row=5, column=1)

button9 = Button( root, text=' 9 ', fg='black', bg='white', command=lambda: push(9), height=1, width=7)
button9.grid(row=5, column=2)

button0 = Button( root, text=' 0 ', fg='black', bg='white', command=lambda: push(0), height=1, width=7)
button0.grid(row=6, column=0)

decimal = Button( root, text=' . ', fg='black', bg='white', command=lambda: push("."), height=1, width=7)
decimal.grid(row=6, column=1)
#Math function buttons

multiply = Button( root, text=' * ', fg='black', bg='white', command=lambda: push("*"), height=1, width=7)
multiply.grid(row=8, column=0)

devide= Button( root, text=' / ', fg='black', bg='white', command=lambda: push("/"), height=1, width=7)
devide.grid(row=8, column=1)

add = Button( root, text=' + ', fg='black', bg='white', command=lambda: push("+"), height=1, width=7)
add.grid(row=7, column=0)

subtract = Button( root, text=' - ', fg='black', bg='white', command=lambda: push("-"), height=1, width=7)
subtract.grid(row=7, column=1)

equal = Button( root, text=' = ', fg='black', bg='white', command= error_check, height=1, width=7)
equal.grid(row=7, column=2)

clear = Button( root, text=' C ', fg='black', bg='white', command= clear, height=1, width=7)
clear.grid(row=6, column=2)



#START GUI mainloop

root.mainloop()
