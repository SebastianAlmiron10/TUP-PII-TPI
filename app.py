# Trabajo Práctico I - Programación

from libro import *
import os



print("Bienvenido!")
respuesta = ''


def gestionar_prestamo(codigo_busqueda):
    
    encontrado = False
    for codigo in lista_libros:
        if codigo_busqueda == codigo['cod']:
            encontrado = True
            
            titulo_x = codigo['titulo']
            autor_x = codigo['autor']
            cant_x = codigo['cant_ej_ad']
            
            if cant_x > 0:
                print(f"Titulo: {titulo_x}, Autor: {autor_x}, cantides disponibles: {cant_x}")
                confirmado = int(input('confirmar prestamo (1. si 2. no): '))
                if confirmado == 1:
                    codigo['cant_ej_ad'] -= 1
                    codigo['cant_ej_pr'] += 1
            else:
                print('no hay unidades disponibles')      
        if not encontrado:
            print('ERROR') 





        

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            codigo_busqueda = input('ingresar codigo de libro: ')
            gestionar_prestamo(codigo_busqueda)
            print()
        elif int(opt) == 2:
            #completar
            print()
        elif int(opt) == 3:
            nuevo_libro()
            print()
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            #completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")