# archivo: cuenta_ahorro.py
from cb import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = 0.001

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito exitoso de ${monto}. Saldo actual: ${self._saldo}")
        else:
            print("El monto debe ser mayor a cero.")

    def extraer(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Extracción exitosa de ${monto}. Saldo actual: ${self._saldo}")
        else:
            print("Saldo insuficiente.")

    def calcular_interes(self):
        interes = self._saldo * self._tasa_interes
        print(f"El interés generado sobre el saldo actual es: ${interes:.2f}")
        return interes
