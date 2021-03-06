from tkinter import *
import matplotlib.pyplot as plt
import os
try:
    os.mkdir("Subj")
    print("cartella creata")
except:
    print("la cartella esiste già")

def mscreendestroy():
    mscreen.destroy()

def subloadgraph():
    global s
    s = sentry.get()
    subj.destroy()
    print(s)
    grafico()

def subgetgraph():
    global subj
    global sentry
    global s
    subj = Tk()
    subj.configure(bg = "grey14")
    subj.resizable(0,0)
    #subj.iconbitmap("Img/icon.ico")
    s = StringVar()
    sentry = Entry(subj, textvariable = s)
    Label(subj,text="Materia?",bg="grey14",fg="white").pack()
    sentry.pack()
    Button(subj,text="Ok",command=subloadgraph,bg="grey19",fg="white").pack()

def grafico():
    global s
    global err
    try:
        vt = open("Subj/"+s,"r")
        votesget = []
        for line in vt:
            currentPlace = line[:-1]
            votesget.append(currentPlace)
        print(votesget)
        y = [float(i) for i in votesget] 
        x = [i+1 for i in range(len(y))]
        ytick = [i/2 for i in range(21)]
        print(x)
        print(y)
        plt.plot(x,y)
        plt.xticks(x)
        plt.yticks(ytick)
        plt.title("Grafico voti in "+s)
        plt.show()
    except:
        err = Label(text="Materia invalida",bg="grey14",fg="white")
        err.grid(row=5,column=0)

def mediascreen():
    global mscreen
    global voti
    global md
    mscreen = Tk()
    mscreen.resizable(0,0)
    mscreen.configure(bg="grey14")
    l1 = Label(mscreen,text="voti ("+str(len(voti))+"): ",bg="grey14",fg="white")
    l2 = Label(mscreen,text=voti,bg="grey14",fg="white")
    l3 = Label(mscreen,text="media: "+str(md),bg="grey14",fg="white")
    if md < 6:
        l3.configure(fg="red")
    b1 = Button(mscreen,text="Ok",bg="grey19",fg="white",command=mscreendestroy)
    l1.pack()
    l2.pack()
    l3.pack()
    b1.pack()

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
    subj.resizable(0,0)
    #subj.iconbitmap("Img/icon.ico")
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
    subj.resizable(0,0)
    #subj.iconbitmap("Img/icon.ico")
    subj.configure(bg = "grey14")
    s = StringVar()
    sentry = Entry(subj, textvariable = s)
    Label(subj,text="Materia?",bg="grey14",fg="white").pack()
    sentry.pack()
    Button(subj,text="Ok",command=subloadmedia,bg="grey19",fg="white").pack()

def voto():
    global s
    global err
    e = entry.get()
    try:
        float(e)
        print(e)
        if float(e) < 0 or float(e) > 10:
            Label(text="Voto invalido",bg="grey14",fg="white").grid(row=5,column=0)
        else:
            votes = open("Subj/"+s, "a+")
            votes.write(e+"\n")
            votes.close()
    except:
        err = Label(text="Voto invalido",bg="grey14",fg="white")
        err.grid(row=5,column=0)

def media():
    global s
    global voti
    global md
    global err
    try:
        votes = open("Subj/"+s, "r")
        voti = []
        for line in votes:
            currentPlace = line[:-1]
            voti.append(currentPlace)
        print(voti)
        md = 0
        for i in voti:
            md = md + float(i)
        md = round(md/len(voti),1)
        print(md)
        mediascreen()
    except:
        err = Label(text="Materia invalida",bg="grey14",fg="white")
        err.grid(row=5,column=0)

#schermata principale
screen = Tk()
screen.title("      ")
screen.configure(bg = "grey14")
screen.resizable(0,0)
#screen.iconbitmap("Img/icon.ico")
screen.geometry("176x500")
e = StringVar()
entry = Entry(textvariable = e, width=20)
title = Label(text = "Registro \n by federicodc05", font = ("Agency FB", 20), bg = "grey14", fg = "white")
text1 = Label(text = "Inserisci il voto", bg = "grey14", fg = "white")
Ok = Button(text = "Ok", bg = "grey19", fg = "white", command = subget)
Media = Button(text = "Fai la media", bg = "grey19", fg ="white", command = subgetmedia)
Graph = Button(text = "Mostra in un grafico", bg = "grey19", fg = "white", command = subgetgraph)
canvas = Canvas(width=176,height=331,highlightthickness=0,bg="grey14")

#posizionamento elementi
title.grid(row=0,column=0,columnspan=2)
text1.grid(row=1,column=0)
entry.grid(row=2,column=0)
Ok.grid(row=2,column=1)
Media.grid(row=3,column=0,columnspan=2)
Graph.grid(row=4,column=0,columnspan=2)
canvas.grid(row=6,column=0,columnspan=2) #canvas WIP

#centro canvas 88 165

#canvas
logo1 = canvas.create_oval(48,125,128,205,fill="blue")
logo2 = canvas.create_oval(53,130,123,200,fill="lightblue")
logotext = canvas.create_text(88,165,text="Fede DC",fill="dark goldenrod",font=("Comic Sans MS",11,'bold','italic'))
copyrighttext = canvas.create_text(120,321,text="©2020 federicodc05",fill="white")

screen.mainloop()
