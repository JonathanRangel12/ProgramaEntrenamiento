
def validar(cadena):
    listBoo=[]
    lisName = cadena.split()
    for i in lisName:
        i = i.isalpha()
        listBoo.append(i)
    return listBoo, lisName

def printNombre():
    nombre = input('Introduzca su nombre: )\n')
    listBool, listName = validar(nombre)
    if False in listBool or len(listName) <= 2:
        print('Por favor no introduzca numeros, coloque su nombre')
        printNombre()
    else:
        var = listName[-2:]
        print(' '.join([str(v) for v in var]))



def mostrarMenu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leerOpcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutarOpcion(opcion, opciones):
    opciones[opcion][1]()


def generarMenu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrarMenu(opciones)
        opcion = leerOpcion(opciones)
        ejecutarOpcion(opcion, opciones)
        print()


def menuPrincipal():
    opciones = {
        '1': ('Ingresar datos de usuario', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('Salir', salir)
    }

    generarMenu(opciones, '4')


def accion1():
    printNombre()
    

def accion2():
    print('Has elegido la opción 2')


def accion3():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menuPrincipal()


