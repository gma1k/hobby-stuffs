import tkinter as tk

def update_display(button_value):
    current_value = display.get()
    if current_value == "0":
        display.delete(0, tk.END)
        display.insert(0, button_value)
    else:
        display.insert(tk.END, button_value)

def clear_display():
    display.delete(0, tk.END)
    display.insert(0, "0")

def evaluate_display():
    expression = display.get()
    try:
        result = eval(expression)
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0, "Invalid input")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.place(x=0, y=0, width=300, height=50)
display.insert(0, "0")

buttons = ["7", "8", "9", "+",
           "4", "5", "6", "-",
           "1", "2", "3", "*",
           "0", ".", "=", "/",
           "C"]

colors = ["lightgray", "lightgray", "lightgray", "orange",
          "lightgray", "lightgray", "lightgray", "orange",
          "lightgray", "lightgray", "lightgray", "orange",
          "lightgray", "lightgray", "orange", "orange",
          "red"]

for i in range(len(buttons)):
    button = tk.Button(root, text=buttons[i], font=("Arial", 20), bg=colors[i])
    button.place(x=(i%4)*75, y=(i//4)*75+50, width=75, height=75)
    if buttons[i] == "=":
        button.configure(command=evaluate_display)
    elif buttons[i] == "C":
        button.configure(command=clear_display)
    else:
        button.configure(command=lambda value=buttons[i]: update_display(value))

root.mainloop()
