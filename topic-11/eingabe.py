from tkinter import *
fenster = Tk()
fenster.title('Eingabe')

def button_action():
    text = eingabe.get()
    ausgabe.config(text=text)

eingabe = Entry(fenster, width=20)
button = Button(fenster, text='Eintragen', command=button_action)
ausgabe = Label(fenster, text='')

eingabe.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)
ausgabe.pack(padx=10, pady=10)

fenster.mainloop()