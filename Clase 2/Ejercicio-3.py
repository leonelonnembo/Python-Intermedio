try:
    mi_diccionario = {"nombre": "Juan", "edad": 30}
    print(mi_diccionario["profesion"])
except KeyError:
    print("Error: Esa clave no existe en el diccionario.")


"""
Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra un mensaje de error al usuario.
"""
