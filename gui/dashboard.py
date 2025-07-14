import tkinter as tk
from tkinter import scrolledtext
from db.practice_db import get_data, close_db_conn


#Function to execute SQL statement and display results in query_view scrolledtext widget.
def launch_app():
    user_query = query_entry.get('1.0', tk.END).strip()
    result = get_data(user_query)

    if user_query.endswith(';'): #check for semicolon at end of edxpression, if not present, do not execute.
        query_view.insert(tk.END, result) #insert result into query_view scrolledtext widget.
        statement_tag = (f'\n***End of Query***\n')#tag to indicate end of query.
        query_view.insert(tk.END, statement_tag)#insert tag into query_view scrolledtext widget.
    else:
        query_view.insert(tk.END, '')
    
#Function to handle Enter key press events
def on_enter(event):
    cursor = query_entry.get('1.0', tk.END).strip().lower()#get current text in query_entry widget and convert to lowercase.
    if cursor in ['clear', 'delete', 'exit']:
        if cursor == 'exit':
            close_app()    
        query_view.delete('1.0', tk.END)#clear query_view widget if user types 'clear' or 'delete'.
        query_entry.delete('1.0', tk.END)#clear query_entry widget.
    launch_app()

#Function to clear the query_entry scrolledtext widget.
def clear_entry():
    query_entry.delete('1.0', tk.END)
    
#Function to close the application.
def close_app():
    root.quit()
    
#create root window
root = tk.Tk()

#configure root window
root.title('PySQL')
root.config(bg='lightblue')
root.geometry('650x750')

#scrolledtext widget to enter SQL statements.
query_entry = scrolledtext.ScrolledText(root, width=20)
query_entry.bind('<Return>', on_enter)#bind Enter key to on_enter function.
query_entry.config(background='black', fg='white', insertbackground='white')

query_entry.pack(side='top', fill='x', padx='5', pady=5)

button_frame = tk.Frame(root, bg='lightblue')
button_frame.pack(side='top', pady=5)

execute = tk.Button(button_frame, text='Execute', width=5, height=2, command=launch_app)
execute.pack(side='left')

clear_button = tk.Button(button_frame, text='Clear', width=5, height=2, command=clear_entry)
clear_button.pack(side='left', padx=5)

close = tk.Button(button_frame, text='Close', width=5, height=2, command=close_app)
close.pack(side='left')

#label to display query
query_frame = tk.Frame(root, bg='lightblue')
query_frame.pack(side='top')

query_view = scrolledtext.ScrolledText(root)
query_view.config(background='black', fg='white', insertbackground='white')
query_view.pack(side='top', fill='x', padx='5', pady='5')

root.mainloop()