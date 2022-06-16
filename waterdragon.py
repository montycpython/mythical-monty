import tkinter as t
from tkinter.messagebox import showinfo
from pickle import load, dump
book = "novel.pkl"

def Remember():
    with open(book, "rb") as mind:
        story = load(mind)
    return story

story = Remember()
app = t.Tk()
key = t.StringVar(app)
frame = t.Frame(app, bg="red", bd=40)

if __name__ == "__main__":
    app.mainloop()
