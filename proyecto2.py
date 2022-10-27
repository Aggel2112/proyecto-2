from tkinter import *
from wsgiref.validate import validator
# definimos los comandos que aran que aumente y disminuya de uno en uno el contador 

def incrementar():
    valor = int(label_valor["text"])
    label_valor["text"] = f"{valor + 1} "

def disminuir():
    valor = int(label_valor["text"])
    label_valor["text"] = f"{valor - 1}" 

ventana = Tk()
ventana.title("CONTADOR")
ventana.geometry("250x150")
ventana.resizable(0,0)
ventana.rowconfigure(0, minsize=50, weight=1)
ventana.columnconfigure([0, 1, 2], minsize=50, weight=1)

boton_decre = Button(ventana, text="DISMINUIR", activebackground="red", command= disminuir)
boton_decre.grid(row=0, column=0, sticky="nsew")

boton_incre = Button(ventana, text="AUMENTAR",activebackground="green", command= incrementar)
boton_incre.grid(row=0, column=2, sticky="nsew")

label_valor = Label(ventana, text=0, fg="black", font=("arial", 35))
label_valor.grid(row=0, column=1)

if  label_valor["text"] > int (0):
    label_valor.config(background="green")

elif label_valor["text"] < int (0)  :
    label_valor.config(background="white")

ventana.mainloop()
