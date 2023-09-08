# Crear un diccionario para cada libro


libro1 = {'cod': 'asd', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}
from cod_generator import generar
def nuevo_libro():
    tit = input("Ingrese el nombre del libro")
    aut = input("Ingrese el autor del libro")
    
    cant_li = input("Ingrese las cantidades de los libros a registrar")
    codigo = generar()
    libro_nuevo = {'cod': codigo, 'cant_ej_ad': cant_li, 'cant_ej_pr': 0, "titulo": tit, "autor": aut}
    print(libro_nuevo)
    lista_libros.append(libro_nuevo)
    
    return None



lista_libros = []
lista_libros.append(libro1)
lista_libros.append(libro2)
lista_libros.append(libro3)