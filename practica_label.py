from tkinter import*
root=Tk()

myframe=Frame(root,width=500,height=400)
myframe.pack()
myLabel=Label(myframe,text="xxxyyy",fg="blue",font=("comic sans ms",14)).place(x=50,y=50)


miImagen=PhotoImage(file="auto.png")
Label(myframe,image=miImagen).place(x=125,y=75)








root.mainloop()