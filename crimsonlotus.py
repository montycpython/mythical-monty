__doc__ = """
Stasis: Once upon a time lived a man.
Trigger: He felt lonely.
Quest: He went to find company.
Surprise: He found no one.
Choice: Stay alone or create company.
Climax: Man creates a copy of himself.
Reversal: Man's copy isn't good enough.
Resolution: Man wants to be alone.
"""

humanNames = """Socrates, Plato, \
Aristotle, Pythagorus, Euclid, \
Archimedes""".split(", ")

divineNames = """Apollo, Python""".split(", ")

#Button(root, text="退出", command=root.destroy, borderwidth=5).grid(column=2, row=3)

import tkinter as t
from tkinter.messagebox import showinfo
from pickle import load, dump
from deep_translator import GoogleTranslator as gt

book = "/storage/emulated/0/Python2020/database.pkl"

def Remember():
    with open(book, "rb") as mind:
        story = load(mind)
    if bool(story):
        pass
    else:
    	story = {"start":"end"}
    return story

def englishSpanish():
    w = toBeTrans.get()
    x = gt("en", "es").translate(w)
    Transd.delete(0, "end")
    Transd.insert(0, x)
    app.clipboard_clear()
    app.clipboard_append(x)
    return x
    
def paste():
    a = app.clipboard_get()
    Value.insert(t.INSERT, a)
    return None
    
def cutIt():
    a = Value.get(t.SEL_FIRST, t.SEL_LAST)
    Value.delete(t.SEL_FIRST, t.SEL_LAST)
    app.clipboard_clear()
    app.clipboard_append(a)
    return None

def Save():
    keys = sorted(story.keys())
    global a,b;
    new_key= Key.get()
    showinfo(message= new_key)
    try:
        old_key = keys[b]
        old_value = story.pop(old_key)
    except:
        old_key = "New"
    showinfo(message= old_key+"$$$")
    new_value = Value.get(a, "end")
    showinfo(message= new_value)
    story.update({new_key:new_value})
    showinfo(message="Saved: {} items total.\n".format(len(story)))
    with open(book, "wb") as mem:
        dump(story, mem)
    showinfo(message="Your story is saved at novel.pkl")
    return None

def Next():
    global a, b;
    story = Remember()
    keys = sorted(story.keys())
    try:
        b += 1
        Key.delete(0, "end")
        Value.delete(a, "end")
        Key.insert(0, keys[b])
        Value.insert(a,  story[keys[b]])
        label.delete(a, "end")
        label.insert(1.0, story[keys[b-1]])
    except:
        Key.insert(0, str(len(keys)).zfill(2))

def Previous():
    global a, b;
    story = Remember()
    keys = sorted(story.keys())
    try:
        b -= 1
        Key.delete(0, "end")
        Value.delete(a, "end")
        Key.insert(0, keys[b])
        Value.insert(a,  story[keys[b]])
        label.delete(a, "end")
        label.insert(1.0, __doc__)
    except:
        pass

story = Remember()
keys = sorted(story.keys())
a = 1.0
b = 0
app = t.Tk()
key = t.StringVar(app)
toBeTrans = t.StringVar(app)
trans = t.StringVar(app)
frame = t.Frame(app, bg="red", bd=40)
Key = t.Entry(frame, textvariable=key)
Trans = t.Entry(frame, textvariable=toBeTrans)
butSpanish = t.Button(frame, text= "Spanish", command=englishSpanish)
label = t.Text(frame, height=12, bg="black", fg="yellow")
butPaste = t.Button(frame, text="Paste sel", command=paste)
butCopy = t.Button(frame, text="Copy sel", command=cutIt)
Transd = t.Entry(frame, textvariable=trans)
Value = t.Text(frame, height=12, bg="blue", fg="white", insertbackground="white")
butS = t.Button(frame, text="寫", command=Save)
butN = t.Button(frame, text="__Next__", command=Next)
butP = t.Button(frame, text="Previous", command=Previous)

if __name__ == "__main__":
    frame.pack(side="bottom", expand=True, fill="both")
    butPaste.pack(side="top", expand=False)
    butCopy.pack(side="top", expand= False)
    Key.pack(side="top", expand=False, fill="x")
    Trans.pack(side="top", expand=False, fill="x")
    butSpanish.pack(side="top", expand=False)
    label.pack(side="bottom", expand=False, fill="x")
    label.insert(1.0, __doc__)
    Value.pack(side="top", fill="x", expand=False)
    Transd.pack(side="top", expand=False, fill="x")
    butP.pack(side="left", expand=True)
    butS.pack(side="left", expand=True)
    butN.pack(side="left", expand=True)
    Value.insert(a,  story[keys[b]])
    Key.insert(0, keys[b])
    
    app.mainloop()
