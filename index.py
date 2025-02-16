import tkinter as tk
from time import strftime
import requests

def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return f"{data['city']}, {data['region']}, {data['country']}"
    except:
        return "Location Unavailable"

def update_time():
    current_time = strftime('%H:%M:%S')  
    current_date = strftime('%Y-%m-%d')  
    label.config(text=current_time)
    date_label.config(text=current_date)
    location_label.config(text=get_location())
    label.after(1000, update_time)

def minimize_window():
    root.iconify()

def close_window():
    root.destroy()

root = tk.Tk()
root.title('Flip Clock')
root.state('zoomed') 
root.configure(bg='black')
root.overrideredirect(True)  

title_bar = tk.Frame(root, bg='black', relief='raised', bd=2)
title_bar.pack(fill='x')
title_label = tk.Label(title_bar, text='Flip Clock', fg='white', bg='black', font=('Helvetica', 12))
title_label.pack(side='left', padx=10)

minimize_button = tk.Button(title_bar, text='➖', command=minimize_window, bg='black', fg='white', borderwidth=0)
minimize_button.pack(side='right', padx=10)

close_button = tk.Button(title_bar, text='✖', command=close_window, bg='black', fg='white', borderwidth=0)
close_button.pack(side='right', padx=10)


label = tk.Label(root, font=('Helvetica', 200, 'bold'), bg='black', fg='white')
label.pack(expand=True)

date_label = tk.Label(root, font=('Helvetica', 50, 'bold'), bg='black', fg='white')
date_label.pack()

location_label = tk.Label(root, font=('Helvetica', 40, 'bold'), bg='black', fg='white')
location_label.pack()

update_time()

root.mainloop()
