from cb import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, limite_extraccion=500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se depositaron ${monto}. Saldo actual: ${self._saldo}")
        else:
            print("El monto debe ser mayor que cero.")

    def extraer(self, monto):
        if monto <= self._saldo and monto <= self._limite_extraccion:
            self._saldo -= monto
            print(f"Se extrajeron ${monto}. Saldo actual: ${self._saldo}")
        elif monto > self._limite_extraccion:
            print("No puede extraer más que el límite permitido.")
        else:
            print("Saldo insuficiente.")
