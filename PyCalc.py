# Simple Calculator
# Created by Justin Mercado
# 6/25/20

import tkinter as tk
from math import sqrt

# Create window and title
root = tk.Tk()
root.title("Simple Calculator")

# Global variable to keep track of first number in operation
global firstNum
firstNum = 0

# Global variable to keep track of what operation to execute
global operationFlag
operationFlag = ""

# Create Display Entry
display = tk.Entry(root, width=40, borderwidth=5)


# Updates display after button click
def buttonClick(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + number)


# Clears display
def buttonClear():
    display.delete(0, tk.END)


# Remembers current number displayed, updates flag for addition, and clears display for next number input
def addFunc():
    global firstNum
    global operationFlag
    operationFlag = "add"
    firstNum = float(display.get())
    display.delete(0, tk.END)


# Remembers current number displayed, updates flag for subtraction, and clears display for next number input
def subFunc():
    global firstNum
    global operationFlag
    operationFlag = "sub"
    firstNum = float(display.get())
    display.delete(0, tk.END)


# Remembers current number displayed, updates flag for multiplication, and clears display for next number input
def multiplyFunc():
    global firstNum
    global operationFlag
    operationFlag = "multiply"
    firstNum = float(display.get())
    display.delete(0, tk.END)


# Remembers current number displayed, updates flag for division, and clears display for next number input
def divideFunc():
    global firstNum
    global operationFlag
    operationFlag = "divide"
    firstNum = float(display.get())
    display.delete(0, tk.END)


# Squares the current number by itself
def squareFunc():
    global firstNum
    firstNum = float(display.get())
    display.delete(0, tk.END)
    display.insert(0, float(firstNum) * float(firstNum))


# Square roots the current number
def squareRootFunc():
    global firstNum
    firstNum = float(display.get())
    display.delete(0, tk.END)
    display.insert(0, sqrt(float(firstNum)))


# Multiplies current number by -1 to flip between positive and negative
def inverseFunc():
    global firstNum
    firstNum = float(display.get())
    display.delete(0, tk.END)
    display.insert(0, float(firstNum) * -1)


# Stores second number, checks operation flag, performs operation of saved first and second number, displays result
def equalFunc():
    secondNum = display.get()
    display.delete(0, tk.END)
    if operationFlag == "add":
        display.insert(0, float(firstNum)+float(secondNum))
    elif operationFlag == "sub":
        display.insert(0, float(firstNum) - float(secondNum))
    elif operationFlag == "multiply":
        display.insert(0, float(firstNum) * float(secondNum))
    elif operationFlag == "divide":
        display.insert(0, float(firstNum) / float(secondNum))
    else:
        display.insert(0, "Error")


# Create number buttons
button0 = tk.Button(root, padx=25, pady=10, text="0", command=lambda: buttonClick("0"))
button1 = tk.Button(root, padx=25, pady=10, text="1", command=lambda: buttonClick("1"))
button2 = tk.Button(root, padx=25, pady=10, text="2", command=lambda: buttonClick("2"))
button3 = tk.Button(root, padx=25, pady=10, text="3", command=lambda: buttonClick("3"))
button4 = tk.Button(root, padx=25, pady=10, text="4", command=lambda: buttonClick("4"))
button5 = tk.Button(root, padx=25, pady=10, text="5", command=lambda: buttonClick("5"))
button6 = tk.Button(root, padx=25, pady=10, text="6", command=lambda: buttonClick("6"))
button7 = tk.Button(root, padx=25, pady=10, text="7", command=lambda: buttonClick("7"))
button8 = tk.Button(root, padx=25, pady=10, text="8", command=lambda: buttonClick("8"))
button9 = tk.Button(root, padx=25, pady=10, text="9", command=lambda: buttonClick("9"))

# Create Number Modifier Buttons
buttonPlusMinus = tk.Button(root, padx=20, pady=10, text="+/-", command=inverseFunc)
buttonDot = tk.Button(root, padx=20, pady=10, text=".", command=lambda: buttonClick("."))
buttonClear = tk.Button(root, padx=20, pady=10, text="C", command=buttonClear)

# Create Operator Buttons
buttonDiv = tk.Button(root, padx=20, pady=10, text="/", command=divideFunc)
buttonMul = tk.Button(root, padx=20, pady=10, text="x", command=multiplyFunc)
buttonSub = tk.Button(root, padx=20, pady=10, text="-", command=subFunc)
buttonAdd = tk.Button(root, padx=20, pady=10, text="+", command=addFunc)
buttonEqual = tk.Button(root, padx=20, pady=10, text="=", command=equalFunc)
buttonSquare = tk.Button(root, padx=20, pady=10, text="x^2", command=squareFunc)
buttonSquareRoot = tk.Button(root, padx=20, pady=10, text="sqRoot", command=squareRootFunc)

# Add Display to Grid
display.grid(row=0, column=0, columnspan=4)

# Add Number Buttons to Grid
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

# Add Number Modifier Buttons to Grid
buttonPlusMinus.grid(row=5, column=0)
button0.grid(row=5, column=1)
buttonDot.grid(row=5, column=2)
buttonClear.grid(row=1, column=2)

# Add Operator Buttons to Grid
buttonDiv.grid(row=1, column=3)
buttonMul.grid(row=2, column=3)
buttonSub.grid(row=3, column=3)
buttonAdd.grid(row=4, column=3)
buttonEqual.grid(row=5, column=3)
buttonSquare.grid(row=1, column=0)
buttonSquareRoot.grid(row=1, column=1)

root.mainloop()
