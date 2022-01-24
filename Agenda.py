from genericpath import exists
import os

CONTACTOS = 'Contactos/'   #carpeta de contactos (se escribe en mayuscula cuando es una constante)
EXTENSION = '.txt'

def app():                 #funcion que ejecuta la app
    crear_directorio()    #crear la carpeta de contactos o revisar si existe 
    mostrar_menu()        #mostrar las opciones del menu para que el usuario elija

    preguntar = True
    while preguntar:      #loop que funciona para que el usuario elija la opcion que desea
        
        print()
        opcion = int(input('Seleccione la opciones que desea: \n'))
        print()

        if opcion == 1:
            print('Seleccionó: Agregar contacto')
            preguntar = False
            agregar_contacto()
        elif opcion == 2:
            print('Seleccionó: Editar contacto')
            preguntar = False
            editar_contacto()
        elif opcion == 3:
            print('Seleccionó: Ver contactos')
            preguntar == False
            mostrar_contactos()
        elif opcion == 4:
            print('Seleccionó: Buscar contacto')
            preguntar = False
            buscar_contacto()
        elif opcion == 5:
            print('Seleccionó: Eliminar contacto')
            preguntar = False
            eliminar_contacto()
        else:
            print('Seleccionó: Opción no válida, intente de nuevo')


def crear_directorio():
    if not os.path.exists(CONTACTOS):  #comprueba si existe el directorio
        os.makedirs(CONTACTOS)         #crea el directorio si es que no existe


def mostrar_menu():
    print()
    print('Seleccione del Menú lo que desea hacer presionando el número correspondiente:')
    print()
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')


class Informacion_contacto: #se comienza a crear un objeto para los datos
    
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def agregar_contacto():
    
    #el usuario ingresara los datos (aqui se ingresa el nombre)
    print('Escribe los datos para agregar un nuevo contacto \n')
    nombre_contacto = input('Nombre del contacto: ')   
    
    #se comprobará que no se repitan los contactos (si el nombre se repite no podrá agendar)
    existe = os.path.isfile(CONTACTOS + nombre_contacto + EXTENSION)

    #si no existe el archivo(contacto) entrará aqui y lo creará
    if not existe:
        
        #se ingresan los demás datos para crear el archivo
        telefono_contacto = input('Número del contacto: ')
        categoria_contacto = input('Categoria del contatco: ') 
        
        with open(CONTACTOS + nombre_contacto + EXTENSION, 'w') as archivo:
            
            #crea un objeto para manejar los datos
            informacion_contacto = Informacion_contacto(nombre_contacto, telefono_contacto, categoria_contacto)            
            
            #crea los datos del contacto en el archivo       
            archivo.write('Nombre: ' + informacion_contacto.nombre)
            archivo.write('\nNumero: ' + informacion_contacto.telefono)
            archivo.write('\nCategoria: ' + informacion_contacto.categoria)
            print('\n ¡Registro exitoso! \n')
            

    #si el contacto ya existía mostrará este mensaje
    else:
        print('\n ¡Ese contacto ya existe, por favor intenta con otro nombre para poder agendar! \n')        

    #reinicia la app
    app()


def editar_contacto():
    print('\nPara editar el contacto por favor le pedimos que haga lo siguiente: \n')
    
    #ingresar el nombre y comprobar si existe el contacto a editar
    nombre_anterior = input('Nombre del contacto que desea editar: ')
    existe = os.path.isfile(CONTACTOS + nombre_anterior + EXTENSION)
    
    if existe:
        
        #abriendo el archivo
        with open(CONTACTOS + nombre_anterior + EXTENSION, 'w') as archivo:
            
            #ingresa los nuevos datos
            nombre_contacto = input('\nPor favor agregar el nuevo nombre: ')
            telefono_contacto = input('Por favor agregar el nuevo número: ')
            categoria_contacto = input('por favor agregar la nueva categoria: ') 
            
            #crea un objeto para manejar los datos
            informacion_contacto = Informacion_contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            #escribir los nuevos datos
            archivo.write('Nombre: ' + informacion_contacto.nombre)
            archivo.write('\nNumero: ' + informacion_contacto.telefono)
            archivo.write('\nCategoria: ' + informacion_contacto.categoria)
            print('\n ¡Edición exitosa! \n')
            
            
        #cambia el nombre del archivo
        os.rename(CONTACTOS + nombre_anterior + EXTENSION, CONTACTOS + nombre_contacto + EXTENSION)
    
    else:
        print('\n **** Este contacto no existe, por favor seleccione la opción 1 para crear un nuevo contacto **** \n')
    
    app()


def mostrar_contactos():
    #para mostrar la lista de contactos
    print('')
    archivos = os.listdir(CONTACTOS)

    #verifica que solo muestre los archivos con terminación .txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivos in archivos_txt:
        with open(CONTACTOS + archivos) as contactos:
            for linea in contactos:
                #imprime los contenidos
                print(linea.rstrip())
            #imprime un separador entre contacto
            print('\n')
    
    app()


def buscar_contacto():
    nombre = input('\nEscriba el nombre del contacto que desea buscar: ')

    #crea el try para dar un mensaje de error "personalizado" en caso de que suceda. En este caso por si se cae la base de datos
    try:
        with open(CONTACTOS + nombre + EXTENSION) as archivo:
            print('\nInformación del contacto:')
            for linea in archivo:
                print(linea.rstrip())
            print('\n')
    except IOError:
        print('\n Uf, no se encontró ningún archivo :(')
        
    
    app()


def eliminar_contacto():
    nombre = input('\nEscriba el nombre del contacto que desea eliminar: ')

    try:
        os.remove(CONTACTOS + nombre + EXTENSION)
        print('\nEl contacto fue eliminado con éxito :)')
    except IOError:
        print('\nEste contacto no se encontró :(\n')

    app()    


app()
