import tkinter as tk
from tkinter import scrolledtext
from db.practice_db import get_data

def sql_statement():
    user_query = query_entry.get('1.0', tk.END).strip()
    result = get_data(user_query)
    query_view.delete('1.0', tk.END)
    query_view.insert(tk.END, result)

#clear query_entry scrolledtext widget
def clear_entry():
    query_entry.delete('1.0', tk.END)
    
#close app
def close_app():
    root.quit()

#tkinter object 
root = tk.Tk()

#create root level window
root.title('PySQL')
root.config(bg='lightblue')
root.geometry('650x750')

#scrolledtext widget to enter SQL statements.
query_entry = scrolledtext.ScrolledText(root, width=20)
query_entry.config(background='black', fg='white', insertbackground='white')
query_entry.pack(side='top', fill='x', padx='5', pady='5')

button_frame = tk.Frame(root, bg='lightblue')
button_frame.pack(side='top', pady=5)

execute = tk.Button(button_frame, text='Execute', width=5, height=2, command=sql_statement)
execute.pack(side='left')

clear_button = tk.Button(button_frame, text='Clear', width=5, height=2, command=clear_entry)
clear_button.pack(side='left', padx=5)

close = tk.Button(button_frame, text='Close', width=5, height=2, command=close_app)
close.pack(side='left')

#label to display query
query_frame = tk.Frame(root, bg='lightblue')
query_frame.pack(side='top', pady=5)

query_view = scrolledtext.ScrolledText(root)
query_view.config(background='black', fg='white', insertbackground='white')
query_view.pack(side='top', fill='x', padx='5', pady='5')

root.mainloop()