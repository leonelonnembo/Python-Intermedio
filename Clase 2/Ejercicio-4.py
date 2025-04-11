"""
Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.
"""

try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe, lo creamos ahora.")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Archivo creado automáticamente.")
        print("Archivo creado con éxito.")
