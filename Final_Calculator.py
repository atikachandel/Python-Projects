import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Create the entry widget
        self.entry = tk.Entry(self.root, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        # Create a dictionary to store the button widgets
        self.button_widgets = {}

        # Create the buttons and assign their actions
        row = 1
        col = 0
        for button in buttons:
            self.button_widgets[button] = tk.Button(
                self.root, text=button, width=5, height=2,
                command=lambda x=button: self.button_click(x)
            )
            self.button_widgets[button].grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, value):
        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except SyntaxError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, value)


# Create the Tkinter root window
root = tk.Tk()

# Create the Calculator instance
calculator = Calculator(root)

# Run the Tkinter event loop
root.mainloop()
