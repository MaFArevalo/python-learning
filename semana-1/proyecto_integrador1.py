programadores = [
    {"nombre": "Florencia", "lenguaje": "Python", "experiencia": 2},
    {"nombre": "Gastón", "lenguaje": "Java", "experiencia": 3},
    {"nombre": "Afua", "lenguaje": "JavaScript", "experiencia": 8}
]
def buscar_programador(nombre):
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    for programador in programadores:
        if programador["nombre"] == nombre:
            return programador 
    raise ValueError(f"No se encontró un programador con ese nombre: {nombre}")
try:
    print(buscar_programador("Carlos"))
except ValueError as error:
    print(error)
try:
    print(buscar_programador("Florencia"))
except ValueError as error:
    print(error)
try:
    print(buscar_programador(""))  
except ValueError as error:
    print(error)    


while True:
    print("=== GESTOR DE PROGRAMADORES ===")
    print("1. Buscar programador")
    print("2. Salir")

    opcion = input("Elegí una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del programador: ")
        try:
            programador = buscar_programador(nombre)
            print(f"Nombre: {programador['nombre']}, Lenguaje: {programador['lenguaje']}, Experiencia: {programador['experiencia']} años")
        except ValueError as error:
            print(error)
    elif opcion == "2":
        print("Programa finalizado.") 
        break
    else:
        print("Opción inválida.")     
        
