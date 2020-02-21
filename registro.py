from tkinter import *

def mscreendestroy():
    mscreen.destroy()

def mediascreen():
    global mscreen
    global voti
    global md
    mscreen = Tk()
    mscreen.configure(bg="grey14")
    Label(mscreen,text="voti: ",bg="grey14",fg="white").pack()
    Label(mscreen,text=voti,bg="grey14",fg="white").pack()
    Label(mscreen,text="media: "+str(md),bg="grey14",fg="white").pack()
    Button(mscreen,text="Ok",bg="grey19",fg="white",command=mscreendestroy).pack()

def subloadmedia():
    global s
    s = sentry.get()
    subj.destroy()
    print(s)
    media()

def subload():
    global s
    s = sentry.get()
    subj.destroy()
    print(s)
    voto()

def subget():
    global subj
    global sentry
    global s
    subj = Tk()
    subj.configure(bg = "grey14")
    s = StringVar()
    sentry = Entry(subj, textvariable = s)
    Label(subj,text="Materia?",bg="grey14",fg="white").pack()
    sentry.pack()
    Button(subj,text="Ok",command=subload,bg="grey19",fg="white").pack()

def subgetmedia():
    global subj
    global sentry
    global s
    subj = Tk()
    subj.configure(bg = "grey14")
    s = StringVar()
    sentry = Entry(subj, textvariable = s)
    Label(subj,text="Materia?",bg="grey14",fg="white").pack()
    sentry.pack()
    Button(subj,text="Ok",command=subloadmedia,bg="grey19",fg="white").pack()

def voto():
    global s
    e = entry.get()
    print(e)
    votes = open(s, "a+")
    votes.write(e+"\n")
    votes.close()

def media():
    global s
    global voti
    global md
    votes = open(s, "r")
    voti = []
    for line in votes:
        currentPlace = line[:-1]
        voti.append(currentPlace)
    print(voti)
    md = 0
    for i in voti:
        md = md + float(i)
    md = md/len(voti)
    print(md)
    mediascreen()

#schermata principale
screen = Tk()
screen.title("Registro by federicodc05")
screen.configure(bg = "grey14")
#screen.geometry("250x200")
e = StringVar()
entry = Entry(textvariable = e)
title = Label(text = "Registro \n by federicodc05", font = ("Agency FB", 20), bg = "grey14", fg = "white")
text1 = Label(text = "Inserisci il voto", bg = "grey14", fg = "white")
Ok = Button(text = "Ok", bg = "grey19", fg = "white", command = subget)
Media = Button(text = "Fai la media", bg = "grey19", fg ="white", command = subgetmedia)

#posizionamento elementi
title.grid(row=0,column=0,columnspan=2)
text1.grid(row=1,column=0,columnspan=2)
entry.grid(row=2,column=0)
Ok.grid(row=2,column=1)
Media.grid(row=3,column=0,columnspan=2)

screen.mainloop()
