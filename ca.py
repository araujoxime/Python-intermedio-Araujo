from cb import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, tasa_interes=0.001):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = tasa_interes
    
    def depositar(self, monto):
        self._saldo+=monto
        print(f"Depósito realizado. El saldo nuevo es {self._saldo}")

    def extraer(self, monto):
        if monto <= self._saldo: 
            self._saldo-=monto
            print(f"Extracción realizada. El saldo nuevo es {self._saldo}")
        else:
            print("Usted no posee saldo suficiente para realizar la operación")
    
    def calcular_interes(self):
        return self._saldo*self._tasa_interes
       
    def obtener_saldo(self):
        interes=self.calcular_interes()
        return self._saldo + interes