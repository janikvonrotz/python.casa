from tkinter import *
from tkinter import messagebox
fenster = Tk()
fenster.title('Messagebox')

def ping():
	nachricht = """
    Pong
    """
	messagebox.showinfo(message=nachricht, title='Infos')

button = Button(fenster, text='Ping', command=ping)
button.pack(padx=30, pady=30)

fenster.mainloop()