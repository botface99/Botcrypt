#Botfcae Encryption Decryption python program
from tkinter import *
from tkinter import messagebox
top=Tk()
top.title("Botcrypt")
top.geometry("300x240")
top.configure()
filen=StringVar()
keyn=StringVar()

def encrypt():
    filer=filen.get()
    key=keyn.get()
    bot=open(filer,"r")
    content=bot.read()
    v=int(key)
    s=" "
    result=""
    for i in range(0,len(content)):
        if " " in content[i]:
            result=result + s 
        else:
            result=result + chr(ord(content[i])-v)
    bot.close()
    bot=open(filer,"w")
    bot.write(result)
    bot.close()
    messagebox.showinfo("Botcrypt","You are succesfully Encrypted your text file")

def decrypt():
    filer=filen.get()
    key=keyn.get()
    bot=open(filer,"r")
    content=bot.read()
    v=int(key)
    s=" "
    result=""
    for i in range(0,len(content)):
        if " " in content[i]:
            result=result + s 
        else:
            result=result + chr(ord(content[i])+v)
    bot.close()
    bot=open(filer,"w")
    bot.write(result)
    bot.close()
    messagebox.showinfo("Botcrypt","You are succesfully Decrypted your text file")
    #tkinter GUI
h1=Label(top,text="BOTCRYPT",foreground="grey",justify="center",font=("Consolas",14,"bold"))
h1.place(x=5,y=5)
h1.pack()
t1=Label(top,text="Text file Name:",fg="grey",font=("Calibri",10,"bold"))
t1.pack(side=LEFT)
t1.place(x=10,y=55)

t2=Entry(top,bd=1.4,textvariable=filen,background="lightgray")
t2.pack(side=RIGHT)
t2.place(x=105,y=55)

k1=Label(top,text="Key:",fg="grey",font=("Calibri",10,"bold"))
k1.pack(side=LEFT)
k1.place(x=10,y=90)

k2=Entry(top,bd=1.4,textvariable=keyn,background="lightgray")
k2.pack(side=LEFT)
k2.place(x=105,y=90)

E=Button(top,text="Encrypt",bg="grey",fg="skyblue",width="16",height="1",command=encrypt)
D=Button(top,text="Decrypt",bg="grey",fg="skyblue",width="16",height="1",command=decrypt)
E.pack(side=LEFT)
E.place(x=10,y=170)
D.pack(side=RIGHT)
D.place(x=150,y=170)

foot=Label(top,text="made by botface",fg="gray",font=("Candara",8))
foot.place()
foot.pack(side=BOTTOM)
top.mainloop()
