# Tkinter-------------------------------------
import tkinter as tk
app = tk.Tk()
app.geometry("500x400")
app.title("My FIrst Tkinter App")
app.configure(background="purple")

lbl = tk.Label(app, text = "welcome to my page", font=("cursive", 20, "bold"), fg="purple", bg="white")
lbl.pack(fill="x", padx = 30, pady = 20, ipady=10)

entr = tk.Entry(app, font=("Gill Sans", 20))
entr.pack(ipadx=20, ipady=10)

btn = tk.Button(app, text = "Submit", font=("cursive", 20, "bold"))
btn.pack(pady=20)

ck = tk.Checkbutton(font=("cursive", 10))
ck = tk.Radiobutton(font=("cursive", 10))
ck.pack()
app.mainloop()


# 1) pack()
# 2) grid()
# 3) place()
