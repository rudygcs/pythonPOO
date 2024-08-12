# EJEMPLO DE HERENCIA

# Definición de la clase base (superclase)
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Definición de una subclase (derivada)
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # Llamamos al constructor de la clase base usando super()
        super().__init__(marca, modelo)
        self.puertas = puertas

    def obtener_informacion(self):
        # Sobrescribimos el método obtener_informacion de la clase base
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Puertas: {self.puertas}"

# Creación de instancias de las subclases
mi_vehiculo = Vehiculo("Ford", "Focus")
mi_automovil = Automovil("Toyota", "Camry", 4)

# Llamada a los métodos de las subclases
print(mi_vehiculo.obtener_informacion())  # Imprime "Marca: Ford, Modelo: Focus"
print(mi_automovil.obtener_informacion())  # Imprime "Marca: Toyota, Modelo: Camry, Puertas: 4"