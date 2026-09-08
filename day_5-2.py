programadores = [
    {"nombre": "Florencia", "lenguaje": "Python"},
    {"nombre": "Gastón", "lenguaje": "Java"},
    {"nombre": "Afua", "lenguaje": "JavaScript"}
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