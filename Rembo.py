
# Copyright [2024] [Drupad M D]

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd

import prc_ui as pu
import strings as st
import whatsapp as wa

def main_ui():
    def browse_files():
        filename = filedialog.askopenfilename(
            title="Select an Excel File",
            filetypes=(("Excel files", "*.xlsx*"), ("all files", "*.*"))
        )
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)

    def submit_form():
        file_path = file_entry.get()
        msg = msg_entry.get()
        if file_path and msg:
            result = read_file(file_path, msg, root)
            messagebox.showinfo("Done", f"Messages sent: {result}")
            root.destroy()
            main_ui()
        else:
            messagebox.showwarning("Incomplete Form", "Please fill in all fields.")

    def on_closing():
        root.quit()
        root.destroy()

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    root = tk.Tk()
    root.title("Slot Reminder")
    root.geometry("750x450")
    root.configure(bg="#f0f0f0")
    root.iconbitmap("icon.ico")

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle the window close event
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create a Canvas and place it with grid
    canvas = tk.Canvas(root, bg="#f0f0f0", highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Create a Scrollbar and place it with grid
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configure the Canvas to work with the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a Frame inside the Canvas
    scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    # Add the Frame to the Canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Ensure the scrollable_frame takes up all available space
    scrollable_frame.grid_rowconfigure(0, weight=1)
    scrollable_frame.grid_columnconfigure(0, weight=1)


    center_frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
    center_frame.grid(row=0, column=0, padx=20, pady=20)

    title_label = tk.Label(center_frame, text="Reminder Bot", font=("Helvetica", 32, "bold"), bg="#f0f0f0", fg="#333")
    title_label.pack(pady=20)

    sub_label = tk.Label(center_frame, text="This is an automated messaging service.", font=("Helvetica", 12), bg="#f0f0f0", fg="#666")
    sub_label.pack(pady=10,padx=5)

    txt = """   NOTE:
    - Make sure all the phone numbers have total of 12 digits and does not contain '+'.
    - After you click 'Send' in the Message Processing window, do not move your mouse or press any 
        keys on your keyboard.
    - A maximum of 100 bulk messaging is only allowed in a day.
    - Confirm that you have logged in on the intended Account in your default browser.
    - The Excel file given as input should not contain any headers.
    - Make sure the Excel file is not open in any other application.
    - Please do contact the Developer if any issue arises."""
    message_label = tk.Label(center_frame, text=txt,anchor="nw",justify="left", font=("Helvetica", 12), bg="#f0f0f0", fg="#666")
    message_label.pack(pady=10)

    file_frame = tk.Frame(center_frame, bg="#f0f0f0")
    file_frame.pack(pady=10)

    file_label = tk.Label(file_frame, text="File:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
    file_label.pack(side=tk.LEFT, padx=5)

    file_entry = tk.Entry(file_frame, width=40, font=("Helvetica", 12), bd=2, relief="groove")
    file_entry.pack(side=tk.LEFT, padx=5)

    browse_button = tk.Button(file_frame, text="Browse", font=("Helvetica", 12), command=browse_files, bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)
    browse_button.pack(side=tk.LEFT, padx=5)

    input_frame = tk.Frame(center_frame, bg="#f0f0f0")
    input_frame.pack(pady=10)
    
    msg_label = tk.Label(input_frame, text="Enter the Message", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
    msg_label.pack(side=tk.LEFT,padx=5)

    msg_entry = scrolledtext.ScrolledText(input_frame, width=30, font=("Helvetica", 12), bd=2, relief="groove")
    msg_entry.pack(side=tk.LEFT,padx=5)

    submit_button = tk.Button(center_frame, text="Submit", font=("Helvetica", 12, "bold"), command=submit_form, bg="#008CBA", fg="white", bd=0, padx=20, pady=10)
    submit_button.pack(pady=20)

    root.mainloop()


def read_file(path, date, root):
    count = 0
    msg = ""

    file = pd.read_excel(path, header=None)
    file = file.reset_index(drop=True)

    for index, row in file.iterrows():
        row_list = row.to_list()

        phone = "+" + str(row_list[1])
        time = str(row_list[3])
        addr = str(row_list[4])
        city = str(row_list[5])

        msg = st.generate_msg(time, addr, city, date)

        flag = pu.prc_ui(count, msg, root)
        print(flag)
        if flag == "n":
            continue
        if flag == "h":
            break
        
        if wa.send_msg(phone, msg) == 1:
            count += 1
        
    else:
        return count
main_ui()