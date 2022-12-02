from tkinter import *
from usuarios import usuario

def principal():
    
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

def registro():     
    root = Tk()
    root.title('Resitro de datos')

    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width = 400 , height= 400)

    titulo = Label(mainFrame, text = " Registro ", font = ("Times New Roman", 12))
    titulo.grid(column = 0,  row = 0, padx= 5, pady = 5, columnspan = 2)

    #Usuario y contraseña
    userLabel = Label(mainFrame, text = "Nombre: ")
    userLabel.grid(column= 0 , row = 1)
    
    passLabel = Label(mainFrame, text = "Contraseña: ")
    passLabel.grid(column= 0 , row = 2)
    
    userLabel = Label(mainFrame, text = "Peso ")
    userLabel.grid(column= 0 , row = 3)
    
    passLabel = Label(mainFrame, text = "Altura: ")
    passLabel.grid(column= 0 , row = 4)

    #Entrada de datos
    nombreUser = StringVar()
    nombreUser.set('')
    nombreEntry = Entry(mainFrame, textvariable = nombreUser)
    nombreEntry.grid(column = 1, row = 1)

    passUser = StringVar()
    passUser.set('')
    passEntry = Entry(mainFrame, textvariable = passUser, show = '*')
    passEntry.grid(column = 1, row = 2)
    
    pesoUser = StringVar()
    pesoUser.set('')
    pesoEntry = Entry(mainFrame, textvariable = pesoUser)
    pesoEntry.grid(column = 1, row = 3)

    alturaUser = StringVar()
    alturaUser.set('')
    alturaEntry = Entry(mainFrame, textvariable = alturaUser)
    alturaEntry.grid(column = 1, row = 4)

    #Boton
    resgisButton = Button(mainFrame, text = 'Registro', command = validarRegistro)
    resgisButton.grid(column = 1, row = 5, ipadx = 2, padx = 5, pady = 8)
    
    root.mainloop()


def iniciar():
    print("Conectar")
    
def validarRegistro():
    print("Validar")
    
    

principal()