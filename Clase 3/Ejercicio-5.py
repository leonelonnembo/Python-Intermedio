def funcion_con_minimo_dos_args(*args):
    print("Todo bien, tenés suficientes argumentos.") if len(args) >= 2 else print("Error: se necesitan al menos dos argumentos.")

# Ejemplos de uso:
funcion_con_minimo_dos_args(1, 2)    # OK
funcion_con_minimo_dos_args(1)       # Error