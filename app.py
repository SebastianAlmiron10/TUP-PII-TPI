# Trabajo Práctico I - Programación
from bibloteca import *
import os



print("Bienvenido!")
respuesta = ''      

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            prestar_ejemplar_libro()
            print()
        elif int(opt) == 2:
            codigo_busqueda = input('ingresar codigo de libro: ')
            devolver_ejemplar_libro(libros, codigo_busqueda)
        elif int(opt) == 3:
            registrar_nuevo_libro()
            print()
        elif int(opt) == 4:
            codigo_busqueda = input('ingresar codigo de libro: ')
            eliminar_ejemplar_libro(libros, codigo_busqueda)
            print()
        elif int(opt) == 5:
            ejemplares_prestados(libros)
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")