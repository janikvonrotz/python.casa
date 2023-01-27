from tkinter import *
fenster = Tk()
fenster.title('Menü')

# Menüleiste erstellen 
menuleiste = Menu(fenster)
# Menüeintrag erstellen 
datei_menu = Menu(menuleiste, tearoff=0)
# Menüaktion hinzufügen
datei_menu.add_command(label='Schliessend', command=fenster.quit)
# Menüeintrag an Menüleiste übertragen
menuleiste.add_cascade(label='Datei', menu=datei_menu)
# Menüleiste in Fenster laden
fenster.config(menu=menuleiste)

label = Label(fenster, text='Klick auf "Datei > Schliessen".')
label.pack(padx=30, pady=30)

fenster.mainloop()