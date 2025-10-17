from cb import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0,limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def depositar(self, monto):
        self._saldo+=monto
        print(f"Depósito realizado. El saldo nuevo es {self._saldo}")

    def extraer(self, monto):
        if monto > self._limite_extraccion:
            print("Usted esta excediendo el límite de extracción")
        elif monto > self._saldo:
            print("Usted no posee saldo suficiente para realizar la operación")
        else:
            self._saldo-=monto
            print(f"Extracción realizada. El saldo nuevo es {self._saldo}")
