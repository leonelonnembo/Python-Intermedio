def buscar_palabra(palabra_buscada, *args):
    resultado = f"La palabra '{palabra_buscada}' está en la lista." if palabra_buscada in args else f"La palabra '{palabra_buscada}' NO está en la lista."
    print(resultado)

# Ejemplo de uso:
buscar_palabra("manzana", "pera", "banana", "manzana")