from tkinter import *
from tkinter import ttk


sudok_root = Tk()
sudok_root.geometry("253x285")
sudok_root.title("S U D O K U")
def _exit():
   sudok_root.destroy()

def quad(X,Y):
   for a in range(0,3):
      for i in range (0,3):
         txtNum = Entry(width=3)
         txtNum.place(x=X+(i*25),y=Y+(a*25))

quad(10,10) #Cuadrante 1,1
quad(90,10) #Cuadrante 1,2
quad(170,10) #Cuadrante 1,3
quad(10,90) #cuadrante 2,1
quad(10,170) #Cuadrante 3,1
quad(90,90) #Cuadrante 2,2
quad(90,170) #Cuadrante 3,2
quad(170,90) #Cuadrante 2,3
quad(170,170) #Cuadrante 3,3

btnSalir = Button(sudok_root, text ="SALIR", command=_exit)
btnSalir.pack(side=BOTTOM)



sudok_root.mainloop()
