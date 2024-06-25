import tkinter as tk

root = tk.Tk()
root.geometry("750x550")
root.minsize(300,200)
root.title("Slot Reminder")

f1 = tk.Frame(root)
f2 = tk.Frame(root)

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
btn2 = tk.Button(f2,text="button2")

lab4.pack(fill='x')
text2.pack(fill='both',expand=True)
btn2.pack(fill='x')

f1.pack(side=tk.TOP,fill='both',expand=True)
f2.pack(side=tk.TOP,fill='both',expand=True)

root.mainloop()