from tkinter import *
from usuarios import usuario

def createVen():
    
    root = Tk()
    root.title('Programa de Entrenamiento')

    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width = 400 , height= 400)

    titulo = Label(mainFrame, text = " Inicio de session ", font = ("Times New Roman", 12))
    titulo.grid(column = 0,  row = 0, padx= 5, pady = 5, columnspan = 2)

    #Usuario y contraseña
    userLabel = Label(mainFrame, text = "Nombre: ")
    userLabel.grid(column= 0 , row = 1)

    passLabel = Label(mainFrame, text = "Contraseña: ")
    passLabel.grid(column= 0 , row = 2)

    #Entrada de datos
    nombreUser = StringVar()
    nombreUser.set('')
    nombreEntry = Entry(mainFrame, textvariable = nombreUser)
    nombreEntry.grid(column = 1, row = 1)

    passUser = StringVar()
    passUser.set('')
    passEntry = Entry(mainFrame, textvariable = passUser, show = '*')
    passEntry.grid(column = 1, row = 2)

    #Boton
    iniciarButton = Button(mainFrame, text = 'Iniciar', command = iniciar)
    iniciarButton.grid(column = 1, row = 3, ipadx = 2, padx = 5, pady = 8)

    resgisButton = Button(mainFrame, text = 'Registro', command = registro)
    resgisButton.grid(column = 2, row = 3, ipadx = 2, padx = 5, pady = 8)
    
    root.mainloop()

def iniciar():
    user1.conectar

def registro():
    pass

if __name__ == "__main__":
    
    # user1 = usuario(input('Ingrese su nombre: '), input('Ingrese contraseña: '))
    user1 = usuario("Jhonny","123")
    
    createVen()
 

