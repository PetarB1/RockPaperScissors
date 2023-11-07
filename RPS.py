from tkinter import *
import random
def izbor(w):
    pkm = {'Kamen':0,'Papir':1,'Makaze':2}
    return pkm[w]
def random_izbor():
    return random.choice(['Kamen','Papir','Makaze'])
def rezultat(korisnik_i,comp_i):
    global korisnik,comp
    igrac=izbor(korisnik_i)
    komp=izbor(comp_i)
    if igrac==komp:
        print("")
    elif (igrac-komp)%3==1:
        korisnik+=1
    else:
        comp+=1
    text1=Text(f2, height=12, width=30)
    text1.grid(column=0, row=0)
    text1.insert(END," Tvoj izbor: {} \n Kompjuterov izbor : {} \n Tvoj rezultat : {}\n Kompjuterov rezultat : {} ".format(korisnik_i,comp_i,korisnik,comp))
def kamen1():
    global korisnik_i,comp_i
    korisnik_i='Kamen'
    comp_i=random_izbor()
    rezultat(korisnik_i,comp_i)
def papir1():
    global korisnik_i,comp_i
    korisnik_i='Papir'
    comp_i=random_izbor()
    rezultat(korisnik_i,comp_i)
def makaze1():
    global korisnik_i,comp_i
    korisnik_i='Makaze'
    comp_i=random_izbor()
    rezultat(korisnik_i,comp_i)
def brojack():
    global m,r,x
    if x==0:
        if m!=r:
            kamen1()
            m+=1
            if m==r:
                kamen.destroy()
                papir.destroy()
                makaze.destroy()
                dugme2.destroy()
                label2.destroy()
        x+=1
    else:
        print("")
def brojacp():
    global m,r,x
    if x==0:
        if m!=r:
            papir1()
            m+=1
            if m==r:
                kamen.destroy()
                papir.destroy()
                makaze.destroy()
                dugme2.destroy()
                label2.destroy()
        x+=1
    else:
        print("")
def brojacm():
    global m,r,x
    if x==0:
        if m!=r:
            makaze1()
            m+=1
            if m==r:
                kamen.destroy()
                papir.destroy()
                makaze.destroy()
                dugme2.destroy()
                label2.destroy()
        x+=1
    else:
        print("")
def runde():
    global r
    r=int(runde1.get())
    label3.destroy()
    dugme.destroy()
    runde1.destroy()
def igraj():
    global x
    x=0
win=Tk()
win.title("Kamen-Papir-Makaze")
win.geometry("600x500")
korisnik_i=""
comp_i=""
m=0
korisnik=0
comp=0
f1=Frame(win)
f1.pack()
label1=Label(f1,text="Kamen-Papir-Makaze",font=23,fg="blue")
label1.pack(side=TOP,pady=30)
label2=Label(f1,text="Tvoje opcije su:")
label2.pack(pady=15)
kamen = Button(f1,text="Kamen",bg="light blue",command=brojack)
kamen.pack(side=LEFT,padx=10,pady=10)
papir = Button(f1,text="Papir",command=brojacp)
papir.pack(side=LEFT,padx=10,pady=10)
makaze = Button(f1,text="Makaze",bg="red",command=brojacm)
makaze.pack(side=LEFT,padx=10,pady=10)
f2=Frame(win)
f2.pack()
f3=Frame(win)
f3.pack()
label=Label(f3,text="")
label3=Label(f3,text=("Prije pocetka unesite zeljeni broj rundi i pritisnite 'OK':,\n Nakon svakog odigranog poteza pritisnite 'Igraj ponovo'"))
label3.pack(side=TOP)
runde1=Entry(f3)
runde1.pack(expand=True)
dugme=Button(f3,text="OK",command=runde)
dugme.pack(expand=True)
f4=Frame(win)
f4.pack()
x=0
dugme2=Button(f4,text="Igraj ponovo",command=igraj)
dugme2.grid()
mainloop()