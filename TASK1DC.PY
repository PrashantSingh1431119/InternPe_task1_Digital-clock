import tkinter as tk
import time

def update_time():
     current_time=time.strftime('%H:%M:%S')
     label.config(text=current_time)
     label.after(1000, update_time)
root=tk.Tk()
root.title("My Clock")

label=tk.Label(root, font=('Seouge', 48), bg='black', fg='white')
label.pack(padx=0, pady=0)

update_time()

root.mainloop()    