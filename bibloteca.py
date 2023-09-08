import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados(lista_libros):
    bandera = False
    for libro in lista_libros:
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
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro(lista_libros, codigo_busqueda):
    encontrado = False
    for codigo in lista_libros:
        if codigo_busqueda == codigo['cod']:
            encontrado = True
            cant_x = codigo['cant_ej_ad']
            
            if cant_x > 0:
                confirmado = int(input('Confirmar Eliminacion (1. si 2. no): '))
                if confirmado == 1:
                    codigo['cant_ej_ad'] -= 1
                    print("Se Realizo la Eliminacion con Exito")
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
    return None

def devolver_ejemplar_libro(lista_libros, codigo_busqueda):
    encontrado = False
    for codigo in lista_libros:
        if codigo_busqueda == codigo['cod']:
            encontrado = True
            cant_x = codigo['cant_ej_pr']
            
            if cant_x > 0:
                confirmado = int(input('confirmar devolucion (1. si 2. no): '))
                if confirmado == 1:
                    codigo['cant_ej_ad'] += 1
                    codigo['cant_ej_pr'] -= 1
                    print("Se Realizo la Devolocion con Exito")
            else:
                print('No hay unidades para devolver')      
        if not encontrado:
            print('ERROR') 
    return None

def nuevo_libro():
    #completar
    return None