from tkinter import *
raiz=Tk()


raiz.title("titulom jojojo")

raiz.iconbitmap("sena.ico")
raiz.geometry("400x400")
raiz.config(bg="#666")


myFrame=Frame()
myFrame.pack()
myFrame.config(bg="#222")
raiz.geometry("400x300")
myFrame.config(width=300,height=70)
myFrame.pack(side=LEFT,anchor="n")
myFrame.pack(fill="x",expand=True)

myFrame.config(bd=30)
myFrame.config(relief="groove")
myFrame.config(cursor="hand1")






raiz.mainloop()