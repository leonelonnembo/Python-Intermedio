try:
    a = int(input("Ingresá el primer número: "))
    b = int(input("Ingresá el segundo número: "))
    resultado = a / b
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")




"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""
