import tkinter as tk  # Importing tkinter for GUI components

# Function to handle button clicks
def click(event):
    current = str(entry.get())  # Get the current text from the entry widget
    text = event.widget.cget("text")  # Get the text from the clicked button

    if text == "=":
        try:
            result = eval(current)  # Evaluate the expression
            entry.delete(0, tk.END)  # Clear the entry field
            entry.insert(tk.END, result)  # Display the result
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")  # Show error for invalid expressions
    elif text == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    else:
        entry.insert(tk.END, text)  # Append the clicked button's text

# Initialize the main application window
root = tk.Tk()
root.title("Basic Calculator")  # Set the title of the window
root.geometry("300x400")        # Set window size
root.resizable(False, False)    # Disable window resizing

# Entry widget for input and output
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame to hold all the calculator buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Layout for buttons in rows
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Create buttons dynamically using nested loops
for row in buttons:
    row_frame = tk.Frame(button_frame)  # Create a row frame
    row_frame.pack(expand=True, fill="both")  # Expand it to fit window
    for btn_text in row:
        # Create each button with styling
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief="ridge", border=1)
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)  # Bind click event to the click() function

# Run the application
root.mainloop()




