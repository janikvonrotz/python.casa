from tkinter import *
from tkinter import messagebox

# Ein Fenster erstellen
fenster = Tk()

# Den Fenstertitle festlegen
fenster.title('Kalkulator')

fenster.geometry('300x200')
rows = 9
columns = 9
for i in range(rows):
    fenster.rowconfigure(index=i,weight=1)
for i in range(columns):
    fenster.columnconfigure(index=i, weight=1)

# Funktion für Button
def button_action():
    try:
        x = float(zahl1.get())
        y = float(zahl2.get())
        label2.config(text=f'= {x+y}')
    except BaseException as error:
        messagebox.showerror(message=error, title='Error')

# Button und Labels erstellen
zahl1 = Entry(fenster, width=20)
label1 = Label(fenster, text='+')
zahl2 = Entry(fenster, width=20)
label2 = Label(fenster, text='= ?')
change_button = Button(fenster, text='Berechnen', command=button_action)
exit_button = Button(fenster, text='Beenden', command=fenster.quit)

# Elemente mit Grid laden
zahl1.grid(row=0, column=4, pady=0, padx=10)
label1.grid(row=1, column=4, pady=0, padx=0)
zahl2.grid(row=2, column=4, pady=0, padx=10)
label2.grid(row=3, column=4, pady=0, padx=0)
change_button.grid(row=4, column=4, pady=0, padx=0)
exit_button.grid(row=5, column=4, pady=0, padx=10)

# Fenster anzeigen und Eingabe abwarten
fenster.mainloop()