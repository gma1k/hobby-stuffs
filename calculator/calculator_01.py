# Import module
import tkinter as tk

# Create a function that updates the display with the button value
def update_display(button_value):
    # Get the current value of the display
    current_value = display.get()
    # If the current value is 0, replace it with the button value
    if current_value == "0":
        display.delete(0, tk.END)
        display.insert(0, button_value)
    # Otherwise, append the button value to the current value
    else:
        display.insert(tk.END, button_value)

# Create a function that clears the display
def clear_display():
    # Delete all the characters from the display
    display.delete(0, tk.END)
    # Set the display value to 0
    display.insert(0, "0")

# Create a function that evaluates the expression on the display
def evaluate_display():
    # Get the expression from the display
    expression = display.get()
    # Try to evaluate the expression using the eval function
    try:
        result = eval(expression)
        # Clear the display and show the result
        clear_display()
        display.insert(0, result)
    # If there is an error, show "Invalid input" on the display
    except:
        clear_display()
        display.insert(0, "Invalid input")

# Create a root window
root = tk.Tk()
# Set the title of the window
root.title("Calculator")
# Set the size of the window
root.geometry("300x400")

# Create a display entry to show the input and output
display = tk.Entry(root, font=("Arial", 20), justify="right")
# Place the display at the top of the window
display.place(x=0, y=0, width=300, height=50)
# Set the initial value of the display to 0
display.insert(0, "0")

# Create a list of button labels
buttons = ["7", "8", "9", "+",
           "4", "5", "6", "-",
           "1", "2", "3", "*",
           "0", ".", "=", "/",
           "C"]

# Create a list of button colors
colors = ["lightgray", "lightgray", "lightgray", "orange",
          "lightgray", "lightgray", "lightgray", "orange",
          "lightgray", "lightgray", "lightgray", "orange",
          "lightgray", "lightgray", "orange", "orange",
          "red"]

# Loop through the buttons and create them on the window
for i in range(len(buttons)):
    # Create a button with the corresponding label and color
    button = tk.Button(root, text=buttons[i], font=("Arial", 20), bg=colors[i])
    # Place the button on a 5x4 grid
    button.place(x=(i%4)*75, y=(i//4)*75+50, width=75, height=75)
    # Bind the button to a function depending on its label
    if buttons[i] == "=":
        # If the button is "=", bind it to the evaluate_display function
        button.configure(command=evaluate_display)
    elif buttons[i] == "C":
        # If the button is "C", bind it to the clear_display function
        button.configure(command=clear_display)
    else:
        # Otherwise, bind it to a lambda function that updates the display with the button value
        button.configure(command=lambda value=buttons[i]: update_display(value))

# Start the main loop of the window
root.mainloop()
