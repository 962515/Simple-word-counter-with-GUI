import tkinter as tk
from tkinter import messagebox

def count_words(text):
    words = text.split()   
    return len(words)

def count_words_event():
    user_input = text_entry.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showerror("Input Error", "Please enter some text.")
        return
    word_count = count_words(user_input)
    result_label.config(text=f"Word Count: {word_count}")

root = tk.Tk()
root.title("Word Counter")
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)
count_button = tk.Button(root, text="Count Words", command=count_words_event)
count_button.pack(pady=5)
result_label = tk.Label(root, text="Word Count: 0")
result_label.pack(pady=10)

root.mainloop()
