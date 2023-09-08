import libro as l
import os
from cod_generator import generar

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados(libros):
    bandera = False
    for libro in libros:
        if libro['cant_ej_pr'] > 0:
            titulo_x = libro['titulo']
            autor_x = libro['autor']
            cant_x = libro['cant_ej_pr']
            codigo = libro['cod']    
            bandera = True
            print(f"Titulo: {titulo_x} - Autor: {autor_x} - Ejemplares Prestados: {cant_x} - Codigo: {codigo}")
    
    if not(bandera):
        print("No hay Ejemplares Prestados")

        
    
    return None

def registrar_nuevo_libro():
    
    titulo_x = str(input("Ingrese el nombre del libro: "))
    autor_x = str(input("Ingrese el autor del libro: "))
    cant_li = input("Ingrese las cantidades de los libros a registrar: ")
    codigo = generar()
    libro_nuevo = {'cod': codigo, 'cant_ej_ad': cant_li, 'cant_ej_pr': 0, "titulo": titulo_x, "autor": autor_x}
    print(libro_nuevo)
    libros.append(libro_nuevo)
    
    return None


def eliminar_ejemplar_libro(libros, codigo_busqueda):
    encontrado = False
    
    for codigo in libros:
        if codigo_busqueda == codigo['cod']:
            encontrado = True
            cant_x = codigo['cant_ej_ad']
            num = False
            if cant_x > 0:
                while not num:                   
                    confirmado = input('Confirmar Eliminacion (1. si 2. no): ')
                    if confirmado.isnumeric():
                        num = True
                        if int(confirmado) == 1:
                            codigo['cant_ej_ad'] -= 1
                            print("Se Realizo la Eliminacion con Exito")
                    else: 
                        print("Ingrese una opción numérica")
            else:
                print('No hay Unidades')      
    if not encontrado:
        print('ERROR') 
    return None


def prestar_ejemplar_libro():
    encontrado = False
    codigo_busqueda = input('Ingresar codigo de libro: ')
    for codigo in libros:
        if codigo_busqueda == codigo['cod']:
            encontrado = True
            num = False
            titulo_x = codigo['titulo']
            autor_x = codigo['autor']
            cant_x = codigo['cant_ej_ad']
            
            if cant_x > 0:
                while not num:
                    print(f"Titulo: {titulo_x}, Autor: {autor_x}, cantides disponibles: {cant_x}")
                    confirmado = input('confirmar prestamo (1. si 2. no): ')
                    if confirmado.isnumeric():
                        num = True
                        if int(confirmado) == 1:
                            codigo['cant_ej_ad'] -= 1
                            codigo['cant_ej_pr'] += 1
                            print("Se Realizo el prestamo con Exito")
                    else: 
                        print("Ingrese una opción numérica")
            else:
                print('no hay unidades disponibles')      
    if not encontrado:
        print('ERROR') 
    return None


def devolver_ejemplar_libro(libros, codigo_busqueda):
    encontrado = False
    num = False
    for codigo in libros:
        if codigo_busqueda == codigo['cod']:
            encontrado = True
            cant_x = codigo['cant_ej_pr']
            
            if cant_x > 0:
                while not num:
                    confirmado = input('confirmar devolucion (1. si 2. no): ')
                    if confirmado.isnumeric():
                        num = True
                        if int(confirmado) == 1:
                            codigo['cant_ej_ad'] += 1
                            codigo['cant_ej_pr'] -= 1
                            print("Se Realizo la Devolucion con Exito")
                    else: 
                        print("Ingrese una opción numérica")
            else:
                print('No hay unidades para devolver')      
    if not encontrado:
        print('ERROR') 
    return None