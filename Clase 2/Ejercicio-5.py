try:
    a = int(input("Ingresá el primer número: "))
    b = int(input("Ingresá el segundo número: "))
    resultado = a / b
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Uno de los valores ingresados no es un número válido.")


"""
 Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

"""