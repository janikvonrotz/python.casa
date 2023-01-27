from tkinter import *

# Ein Fenster erstellen
fenster = Tk()

# Den Fenstertitle festlegen
fenster.title('Nur ein Fenster')

# Funktion für Button
def button_action():
    anweisungs_label.config(text='Sie haben auf "Ändern" geklickt.')

# Button und Labels erstellen
change_button = Button(fenster, text='Ändern', command=button_action)
exit_button = Button(fenster, text='Beenden', command=fenster.quit)
anweisungs_label = Label(fenster, text='Klicken Sie auf Ändern')

# Elemente in Reihenfolge laden
# anweisungs_label.pack()
# change_button.pack()
# exit_button.pack()

# Elemente mit Grid laden
anweisungs_label.grid(row=1, column=1, pady=10, padx=10)
change_button.grid(row=2, column=1, pady=10)
exit_button.grid(row=3, column=1, pady=10)

# Fenster anzeigen und Eingabe abwarten
fenster.mainloop()