class Programador:
    def __init__(self, nombre, lenguaje, experiencia):
        self.nombre = nombre
        self.lenguaje = lenguaje
        self.experiencia = experiencia
    def aumentar_experiencia(self):
        self.experiencia += 1 
    def cambiar_lenguaje(self, nuevo_lenguaje):
        self.lenguaje = nuevo_lenguaje
    def presentarse(self):
        return f"Hola, soy {self.nombre} y programo en {self.lenguaje}."


flor = Programador("Flor", "Python", 1)
lucia = Programador("lucia", "Java", 5)
print(flor.presentarse(), lucia.presentarse())

flor.cambiar_lenguaje("JavaScript")
print(flor.lenguaje)
flor.aumentar_experiencia()
print(flor.experiencia)

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"
    def vender(self):
        self.stock -= 1

notebook = Producto("Notebook", 800000, 5)
yerba = Producto("Yerba", 300, 5)

notebook.vender()
print(notebook.stock)
print(notebook.mostrar_info())
print(yerba.mostrar_info())



