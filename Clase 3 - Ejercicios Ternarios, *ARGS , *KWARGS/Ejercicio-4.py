def promedio(*args):
    return sum(args)/len(args) if len(args) > 0 else "No se puede calcular el promedio sin datos."

# Ejemplo de uso:
print(promedio(5, 10, 15))  # Promedio: 10.0