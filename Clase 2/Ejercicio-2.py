"""
Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

"""
try:
    numero = 5
    cadena = "hola"
    resultado = numero + cadena
    print("Resultado:", resultado)
except TypeError:
    print("Error: No se puede sumar un número con una cadena.")
