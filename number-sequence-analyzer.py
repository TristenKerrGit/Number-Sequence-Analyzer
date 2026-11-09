import tkinter as tk
import copy

def fibonacci()








root = tk.Tk()
root.title("Number Sequence Analyzer")

title_card = tk.Frame(root)
title_card.grid(row=0, column=0)


exit_only = tk.Frame(root)
exit_only.grid(row=10, column=0)



def on_click():
    root.destroy()


lbl = tk.Label(title_card, text="<< Number Sequence Analyzer >>")
lbl.grid(row=0, column=0)

btn = tk.Button(exit_only, text="QUIT APP", command=on_click)
btn.grid(row=0, column=0)

root.mainloop()