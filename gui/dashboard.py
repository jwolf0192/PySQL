import tkinter as tk
from db.practice_db import get_data

def sql_statement():
    user_query = query_entry.get()
    result = get_data(user_query)
    query_view.config(text=result)
    
#close app
def close_app():
    root.quit()

#tkinter object 
root = tk.Tk()

#create root level window
root.title('TK DB')
root.config(bg='lightblue')
root.geometry('250x250')

#entry widget to enter SQL statements.
query_entry = tk.Entry(root, width=20)
query_entry.pack(side='top', fill='x', pady='5')

button_frame = tk.Frame(root, bg='lightblue')
button_frame.pack(side='top', pady=5)

execute = tk.Button(button_frame, text='Execute', width=5, height=2, command=sql_statement)
execute.pack(side='left', padx=5)

close = tk.Button(button_frame, text='Close', width=5, height=2, command=close_app)
close.pack(side='left')

#label to display query
query_frame = tk.Frame(root, bg='lightblue')
query_frame.pack(side='top', pady=5)

query_view = tk.Label(root, text='Place holder', bg='lightblue')
query_view.pack(side='top', fill='x')

root.mainloop()