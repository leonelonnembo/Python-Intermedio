from cuenta_ahorro import CuentaAhorro

cuenta = CuentaAhorro("María", 44444444, "1995/05/10", 10000)

cuenta.depositar(500)
cuenta.extraer(1000)
cuenta.extraer(1000)
cuenta.extraer(1000)
cuenta.extraer(1000)
cuenta.calcular_interes()  # Debería mostrar interés acumulado hasta el momento
