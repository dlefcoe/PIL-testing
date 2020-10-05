'''

example of tkinter to view pandas df or excel

'''


import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd


root = tk.Tk()

# root window size
root.geometry('500x500')

#keep root window the same size
root.pack_propagate(False)

# prevent window from being resized
root.resizable(0,0)

# frame for TreeView
frame1 = tk.LabelFrame(root, text='excel data')
frame1.place(height=250, width=500)

# Frame for open file dialogue
file_frame = tk.LabelFrame(root, text='openfile')
file_frame.place(height=100, width=400, rely=0.65, relx=0)

# buttons
button1 = tk.Button(file_frame, text='browse a file', command=lambda: file_dialogue())
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(file_frame,text='load file', command = lambda: load_excel_data())
button2.place(rely=0.65, relx=0.30)

label_file = ttk.Label(file_frame, text='no file selected')
label_file.place(rely=0, relx=0)

## tree view widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) #fill whole container with treeview

treescrolly = tk.Scrollbar(frame1, orient='vertical', command=tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient='horizontal', command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side='bottom', fill='x')
treescrolly.pack(side='right', fill='y')


def file_dialogue():
    filename = filedialog.askopenfilename(initialdir='/', 
                                        title='select a file', 
                                        filetype=(('xlsx files','.xlsx'),('all files','*.*')))
    label_file['text'] = filename

def load_excel_data():
    file_path = label_file['text']
    try:
        excel_filename = r'{}'.format(file_path)
        df = pd.read_excel(excel_filename)
    except ValueError:
        tk.messagebox.showerror('informaiton', 'the file you have entered is invalid')
        return None
    except FileNotFoundError:
        tk.messagebox.showerror('informaiton', f'no such file as {file_path}')
        return None
    
    clear_data()
    tv1['column'] = list(df.columns)
    tv1['show'] = 'headings'

    for column in tv1['columns']:
        tv1.heading(column, text=column)
    
    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert('', 'end', values=row)
    return None


def clear_data():
    tv1.delete(*tv1.get_children())




root.mainloop()





