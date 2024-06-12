import tkinter as tk
from tkinter import messagebox

# Declare global variables
val = ""
sub = None

def create_main_window(root):
    sub = tk.Toplevel(root)
    sub.title("Message Processing")
    sub.geometry("700x350")
    sub.configure(bg="#f0f0f0")
    sub.iconbitmap("icon.ico")
    sub.withdraw()
    return sub

def btn(txt,sub):
    global val
    val = txt
    sub.quit()

def go_home(sub):
    global val
    val="h"
    sub.quit()

def clear_window(sub):
    for widget in sub.winfo_children():
        widget.destroy()

def first_ui(sub,count):

    def on_mousewheel(event):
        sub.yview_scroll(int(-1 * (event.delta / 120)), "units")
    clear_window(sub)

    # Create a Scrollbar and place it with grid
    scrollbar = tk.Scrollbar(sub, orient="vertical", command=sub.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configure the Canvas to work with the Scrollbar
    sub.configure(yscrollcommand=scrollbar.set)
    sub.bind("<Configure>", lambda e: sub.configure(scrollregion=sub.bbox("all")))

    title_label = tk.Label(
        sub, text="Processing Messages", font=("Helvetica", 22, "bold"), bg="#f0f0f0", fg="#333"
    )
    title_label.pack(pady=20)

    msg = f"Number of Messages sent: {count}"
    message_label = tk.Label(
        sub, text=msg, font=("Helvetica", 12), bg="#f0f0f0", fg="#666"
    )
    message_label.pack(pady=10)

    btn_frame = tk.Frame(sub, bg="#f0f0f0")
    btn_frame.pack(pady=10)

    btn_label = tk.Label(btn_frame, text="Send the message?", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
    btn_label.pack(side=tk.LEFT, padx=5)

    btn1 = tk.Button(btn_frame, text="Send", font=("Helvetica", 12), command=lambda: btn("y",sub), bg="#4CAF50", fg="white", bd=0, padx=5, pady=5)
    btn1.pack(side=tk.LEFT, padx=5)

    btn2 = tk.Button(btn_frame, text="Skip", font=("Helvetica", 12), command=lambda: btn("n",sub), bg="#ff3333", fg="white", bd=0, padx=5, pady=5)
    btn2.pack(side=tk.LEFT, padx=5)

    quit_button = tk.Button(sub, text="Quit", font=("Helvetica", 12, "bold"), command=lambda: go_home(sub), bg="#008CBA", fg="white", bd=0, padx=20, pady=10)
    quit_button.pack(pady=20)

def second_ui(sub,msg,count):
    clear_window(sub)
    title_label = tk.Label(
        sub, text="Message Generation Completed", font=("Helvetica", 22, "bold"), bg="#f0f0f0", fg="#333"
    )
    title_label.pack(pady=20)

    msg = f"Number of Messages sent: {count}"
    message_label = tk.Label(
        sub, text=msg, font=("Helvetica", 12), bg="#f0f0f0", fg="#666"
    )
    message_label.pack(pady=10)

    submit_button = tk.Button(sub, text="Home", font=("Helvetica", 12, "bold"), command=go_home, bg="#008CBA", fg="white", bd=0, padx=20, pady=10)
    submit_button.pack(pady=20)

def prc_ui(count,msg,root):
    sub = create_main_window(root)
    sub.deiconify()
    first_ui(sub, count)
    sub.mainloop()
    sub.withdraw()
    return val
