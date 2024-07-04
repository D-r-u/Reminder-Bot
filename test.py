import tkinter as tk
from tkinter import ttk


def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))


root = tk.Tk()
root.geometry("750x550")
root.minsize(300,200)
root.title("Slot Reminder")

f21 = tk.Frame(root)

canvas = tk.Canvas(f21, bg="#f0f0f0", highlightthickness=0)
scrollbar = tk.Scrollbar(f21, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas,style="TFrame" )
scrollable_frame.bind("<Configure>", on_frame_configure)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.bind_all("<MouseWheel>", on_mousewheel)


f1 = tk.Frame(root)
f2 = tk.Frame(scrollable_frame)

lab1 = tk.Label(f1, text="Reminder Bot", font=("Helvetica", 32, "bold"),anchor="center",
                            bg="#f0f0f0", fg="#333")
ent1 = tk.Entry(f1)
lab2 = tk.Label(f1,text="label2")
ent2 = tk.Entry(f1)
lab3 = tk.Label(f1, text="label3")
text1 = tk.Text(f1, width=20, height=5)
btn1 = tk.Button(f1,text="button1")

lab1.pack(fill='x')
ent1.pack(fill='x')
lab2.pack(fill='x')
ent2.pack(fill='x')
lab3.pack(fill='x')
text1.pack(fill='both',expand=True)
btn1.pack(fill='x')

lab4 = tk.Label(f2,text="label4")
text2 = tk.Text(f2,width=20,height=10)
btn2 = tk.Button(f2,height=40,text="button2")

lab4.pack()
text2.pack()
btn2.pack()

canvas.pack(fill='both',expand=True)
scrollable_frame.pack(fill='both',expand=True)

f1.pack(side=tk.TOP,fill='both',expand=True)
f2.pack(side=tk.TOP,fill='both',expand=True)
f21.pack(side=tk.TOP,fill='both',expand=True)

root.mainloop()