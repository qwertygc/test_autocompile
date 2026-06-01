import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk
root = ThemedTk(theme="breeze")
root.title("Hello world")

ttk.Label(root, text="Hello world").grid(row=3, column=0, padx=5, pady=5, sticky="e")
root.mainloop()
