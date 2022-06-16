import tkinter as t
from tkinter.messagebox import showinfo
from pickle import load, dump
__doc__ = """Life is as transparent as you're capable of seeing it."""
book = "novel.pkl"

def Remember():
    with open(book, "rb") as mind:
        story = load(mind)
    return story

story = Remember()
app = t.Tk()
key = t.StringVar(app)
frame = t.Frame(app, bg="red", bd=40)
frame.pack(expand=True, fill="both")
Key = t.Entry(frame, textvariable=key)
Key.pack(expand=False, fill="x")
keys = sorted(story.keys())
a = 1.0
b = 0
Key.insert(0, keys[b])
label = t.Label(frame, text=__doc__)
label.pack(expand=True, fill="x")
Value  = t.Text(frame, height=12)
Value.pack(fill="both")
Value.insert(a, story[keys[b]])

def Save():
    keys = sorted(story.keys())
    global a, b;
    new_key = Key.get()
    showinfo(message=new_key)
    try:
        old_key = keys[b]
        old_value = story.pop(old_key)
    except:
        old_key = "New"
    showinfo(message=old_key + "$$$")
    new_value = Value.get(a, "end")
    showinfo(message = new_value)
    story.update({new_key:new_value})
    showinfo(message="Saved: {} items total.\n".format(len(story)))
    with open(book, "wb") as mem:
        dump(story, mem)
    showinfo(message = "Your story is saved at novel.py")

s = t.Button(frame, text = "Save", command=Save)
s.pack()

def Next():
    global a, b;
    story = Remember()
    keys = sorted(story.keys())
    try:
        b+= 1
        Key.delete(0, "end")
        Value.delete(a, "end")
        Key.insert(0, keys[b])
        Value.insert(a, story[keys[b]])
    except:
        Key.insert(0, str(len(keys)).zfill(2))
    
def Previous():
    global a, b;
    story = Remember()
    keys = sorted(story.keys())
    try:
        b-= 1
        Key.delete(0, "end")
        Value.delete(a, "end")
        Key.insert(0, keys[b])
        Value.insert(a, story[keys[b]])
    except:
        pass
    
c = t.Button(frame, text="__Next__", command=Next)
c.pack(side="right")
d = t.Button(frame, text="Previous", command=Next)
d.pack(side="left")

if __name__ == "__main__":
    app.mainloop()
