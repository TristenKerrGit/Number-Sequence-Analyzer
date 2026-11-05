import math
import tkinter as tk

root = tk.Tk()
root.title("Number Sequence Analyzer")

title_card = tk.Frame(root)
title_card.grid(row=0, column=0)


fibonacci_seq = tk.Frame(root)
fibonacci_seq.grid(row=0, column=0)

prime_num_chk = tk.Frame(root)
prime_num_chk.grid(row=0, column=0)

prime_num_rng = tk.Frame(root)
prime_num_rng.grid(row=0, column=0)

multiply_table = tk.Frame(root)
multiply_table.grid(row=0, column=0)

factorial = tk.Frame(root)
factorial.grid(row=0, column=0)

collatz_seq = tk.Frame(root)
collatz_seq.grid(row=0, column=0)



exit_only = tk.Frame(root)
exit_only.grid(row=10, column=0)


def on_click_():
    root.destroy()


lbl = tk.Label(title_card, text="<< Number Sequence Analyzer >>")
lbl.grid(row=0, column=0)


calc1 = tk.Button(fibonacci_seq, text="", )


calc2 = tk.Button(prime_num_chk, text="", )


calc3 = tk.Button(prime_num_rng, text="", )


calc4 = tk.Button(multiply_table, text="", )


calc5 = tk.Button(factorial, text="", )


calc6 = tk.Button(collatz_seq, text="", )



btn = tk.Button(exit_only, text="QUIT APP", command=on_click)
btn.grid(row=0, column=0)

root.mainloop()