from random import choice
from tkinter import *

colors = ['blue','red','green', 'purple','dark red']
root = Tk()
root.geometry('300x300')

rows = 10
columns = 10

for i in range(rows):
    root.rowconfigure(index=i,weight=1)

for i in range(columns):
    root.columnconfigure(index=i, weight=1)

for r in range(rows):
    for c in range(columns):
        lbl  = Label(root,bg=choice(colors))
        lbl.grid(row=r,column=c,sticky='news')

if __name__ == '__main__':
    root.mainloop()
