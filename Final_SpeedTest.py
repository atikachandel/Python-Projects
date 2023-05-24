import random
import time
import tkinter as tk
from tkinter import messagebox

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("500x300")

        self.words = ["python", "programming", "typing", "practice",
                      "interface", "challenge", "speed", "accuracy", "development", "keyboard"]

        self.current_word = ""
        self.user_input = ""
        self.start_time = 0
        self.end_time = 0

        self.word_label = tk.Label(self.root, text=self.current_word, font=("Arial", 20))
        self.word_label.pack(pady=50)

        self.entry = tk.Entry(self.root, font=("Arial", 16))
        self.entry.pack(pady=20)

        self.entry.bind("<Return>", self.check_input)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        self.start_button.pack()

    def start_test(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.user_input = ""
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.start_time = time.time()

    def check_input(self, event):
        user_input = self.entry.get()
        if user_input == self.current_word:
            self.end_time = time.time()
            elapsed_time = round(self.end_time - self.start_time, 2)
            self.show_result(elapsed_time)
        else:
            messagebox.showinfo("Incorrect", "Wrong word. Try again.")
            self.entry.delete(0, tk.END)

    def show_result(self, elapsed_time):
        messagebox.showinfo("Result", f"Time elapsed: {elapsed_time} seconds")
        self.start_button.focus()

if __name__ == "__main__":
    root = tk.Tk()
    SpeedTypingTest(root)
    root.mainloop()
