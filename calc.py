import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

#create the main window
root = tk.Tk()
root.title("simplecalculator")

#entry widget for displaying the results
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

#Button for digits and operators
buttons = [
   '7', '8', '9', '/',
   '4', '5', '6', '*',
   '1', '2', '3', '-',
   '0', '.', '=', '+'
]

#function to generate button click callbacks
def button_callback(value):
    return lambda: on_button_click(value)

#cretae and place the button in the grid
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, command=button_callback(button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()
