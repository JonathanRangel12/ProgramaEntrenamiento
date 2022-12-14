
class usuario():
    
    nUsuario = 0
    
    def __init__(self, nombre, passw):
        self.nombre = nombre
        self.passw = passw
        
        self.conectado = False
        self.intento = 3
        
        usuario.nUsuario += 1
        
    def conectar(self, password = None):
        if password == None:
            pas = input('Ingrese contraseña ')
        else:
            pas = password
                       
        if pas == self.passw:
            print('Conectado.')
            self.conectado = True
        else:
            self.intento -= 1
            if self.intento > 0:
                print('Constraseña incorrecta')
                if self.intento != 1:
                    print('Te quedan: ', self.intento ,'intentos')
                else:
                    print('Te queda: ', self.intento ,'intento')
                self.conectar()
            else:
                print('Maximo de intentos posibles')
                
    def desconectar(self):
        if self.conectado:
                print('Session cerrada')
                self.conectado = False
        else:
                print('No se iniciado session')
        
    def __str__(self):
        if self.conectado:
                conect = 'Conectado'
        else:
                conect = 'Desconectado'            
        return f'{self.nombre} --- Estado: {conect}'
        
        
## user1 = usuario(input('Ingrese su nombre: '), input('Ingrese contraseña: '))
## print(user1)
## user1.conectar()
