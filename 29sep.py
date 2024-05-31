import tkinter as tk
app=tk.Tk()
app.geometry("400x400")
app.title("My Form")
app.configure(background="pink")

labl1 = tk.Label(app,text="hey this is a chair",font=("robort", 20, "bold"))
labl1.place(x=100,y=100)
labl2 = tk.Label(app, text = "hey this is  a car", font=("robort", 20, "bold"))
labl2.place(x=200,y=200)
labl3 = tk.Label(app, text = "hey im your jin", font=("robort", 20, "bold"))
labl3.place(x=300,y=300)
labl4 = tk.Label(app, text = "hey look at me!!", font=("robort", 20, "bold"))
labl4.place(x=400,y=400)
labl5 = tk.Label(app, text = "hey im happy singh", font=("robort", 20, "bold"))
labl5.place(x=500,y=500)
labl6 = tk.Label(app, text = "hey anjali nirmohi", font=("robort", 20, "bold"))
labl6.place(x=600,y=600)


app.mainloop()