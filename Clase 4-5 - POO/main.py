
from cuenta_ahorro import CuentaAhorro
from cuenta_corriente import CuentaCorriente

print("Cuenta Ahorro:")
cuenta1 = CuentaAhorro("María", 12345678, "1990/05/10", 10000)
cuenta1.depositar(1000)
cuenta1.extraer(500)
cuenta1.calcular_interes()
print(f"Edad del titular: {cuenta1.obtener_edad()} años\n")

print("Cuenta Corriente:")
cuenta2 = CuentaCorriente("Pedro", 87654321, "1985/03/15", 2000)
cuenta2.depositar(300)
cuenta2.extraer(400)
print(f"Edad del titular: {cuenta2.obtener_edad()} años")
