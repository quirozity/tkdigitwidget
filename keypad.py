import tkinter as tk

def button_click(digit):
    entry.insert(tk.END, digit)

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get()) - 1)

def submit():
    value = entry.get()
    # Do something with the entered value (e.g., validate, process, etc.)
    print("Submitted value:", value)
    clear_entry()

root = tk.Tk()
root.title("Custom Keyboard")
root.geometry("300x200")

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

# Create digit buttons
digits_frame = tk.Frame(root)
digits_frame.pack()

for i in range(1, 10):
    button = tk.Button(digits_frame, text=str(i), width=6, height=2,
                       command=lambda digit=i: button_click(digit))
    button.grid(row=(i-1) // 3, column=(i-1) % 3)

# Create special buttons
special_frame = tk.Frame(root)
special_frame.pack()

button_0 = tk.Button(special_frame, text="0", width=6, height=2,
                     command=lambda: button_click(0))
button_0.grid(row=0, column=0)

button_clear = tk.Button(special_frame, text="Clear", width=6, height=2,
                         command=clear_entry)
button_clear.grid(row=0, column=1)

button_backspace = tk.Button(special_frame, text="Backspace", width=10, height=2,
                             command=backspace)
button_backspace.grid(row=0, column=2)

button_submit = tk.Button(special_frame, text="Submit", width=6, height=2,
                          command=submit)
button_submit.grid(row=1, columnspan=3, pady=5)

root.mainloop()
