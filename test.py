import tkinter as tk
from tkinter import ttk


def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

txt = """   NOTE:
    - Make sure all the phone numbers have total of 12 digits and does not contain '+'.
    - After you click 'Send' in the Message Processing window, do not move your mouse or press any 
        keys on your keyboard.
    - A maximum of 100 bulk messaging is only allowed in a day.
    - Confirm that you have logged in on the intended Account in your default browser.
    - The Excel file given as input should not contain any headers.
    - Make sure the Excel file is not open in any other application.
    - Please do contact the Developer if any issue arises."""
sub = "This is an automated messaging service.\n Takes .xlsx files and the message to be sent."

root = tk.Tk()
root.geometry("750x550")
root.minsize(300,200)
root.title("Slot Reminder")


f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)

canvas = tk.Canvas(f2, bg="#f0f0f0", highlightthickness=0)
scrollbar = tk.Scrollbar(f2, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas,style="TFrame" )
scrollable_frame.bind("<Configure>", on_frame_configure)

f21 = tk.Frame(scrollable_frame)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.bind_all("<MouseWheel>", on_mousewheel)


title = tk.Label(f1, text="Reminder Bot", font=("Helvetica", 32, "bold"),anchor="center",
                            bg="#f0f0f0", fg="#333")
sub_title = tk.Label(f1, text=sub,font=("Helvetica", 12), bg="#f0f0f0", fg="#666")

title.pack(fill='x')
sub_title.pack(fill='x')

instr = tk.Label(f2,text="txt")

instr.pack(fill='x')

f31 = tk.Frame(f3)
f32 = tk.Frame(f3)
f33 = tk.Frame(f3)

file_label = tk.Label(f31, text="File:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
lab3 = tk.Label(f1, text="label3")

file_label.pack(side=tk.LEFT,fill='x')
lab3.pack(fill='x')

lab4 = tk.Label(f21,text="label4")
text2 = tk.Text(f21,width=20,height=10)
btn2 = tk.Button(f21,height=40,text="button2")

lab4.pack(fill='x')
text2.pack(fill='both',expand=True)
btn2.pack(fill='x')

canvas.pack(fill='both',expand=True)
scrollable_frame.pack(fill='both',expand=True)

f31.pack(side=tk.TOP,fill='x')
f32.pack(side=tk.TOP,fill='x')
f33.pack(side=tk.TOP,fill='x')

f1.pack(side=tk.TOP,fill='both',expand=True)
f2.pack(side=tk.TOP,fill='both',expand=True)
f3.pack(side=tk.TOP,fill='both',expand=True)



root.mainloop()