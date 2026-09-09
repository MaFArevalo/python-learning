import json


programadores = [
    {"nombre": "Florencia", "lenguaje": "Python", "experiencia": 2},
    {"nombre": "Gastón", "lenguaje": "Java", "experiencia": 3},
    {"nombre": "Afua", "lenguaje": "JavaScript", "experiencia": 8}
]


def mostrar_programadores():
    if not programadores:
        raise ValueError("No se encontró ningún programador.")

    return "\n\n".join(
        f"Nombre: {programador['nombre']}\n"
        f"Lenguaje: {programador['lenguaje']}\n"
        f"Experiencia: {programador['experiencia']} años"
        for programador in programadores
    )


def agregar_programador():
    while True:
        nombre = input("Ingrese el nombre del programador: ").strip()
        if not nombre:
            print("Error: el nombre no puede estar vacío.")
        elif any(caracter.isdigit() for caracter in nombre):
            print("Error: el nombre no puede contener números.")
        else:
            break
    while True:
        lenguaje = input("Ingrese el lenguaje de programación: ").strip()
        if not lenguaje:
            print("Error: el lenguaje no puede estar vacío.")
        elif any(caracter.isdigit() for caracter in lenguaje):
            print("Error: el lenguaje no puede contener números.")
        else:
            break

    while True:
        try:
            experiencia = int(input("Ingrese los años de experiencia: "))
            if experiencia < 0:
                print("la experiencia no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Error: la experiencia debe ser un número entero.")

    nuevo_programador = {
        "nombre": nombre,
        "lenguaje": lenguaje,
        "experiencia": experiencia
    }
    programadores.append(nuevo_programador)
    print("Programador agregado correctamente.")


def guardar_programadores():
    with open("programadores.json", "w", encoding="utf-8") as archivo:
        json.dump(programadores, archivo, ensure_ascii=False)
    print("Programadores guardados correctamente.")


def buscar_programador(nombre):
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    for programador in programadores:
        if programador["nombre"] == nombre:
            return (
                f"Nombre: {programador['nombre']}\n"
                f"Lenguaje: {programador['lenguaje']}\n"
                f"Experiencia: {programador['experiencia']} años"
            )
    raise ValueError(f"No se encontró un programador con ese nombre: {nombre}")


def cargar_programadores():
    with open("programadores.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)


try:
    programadores = cargar_programadores()
except FileNotFoundError:
    print("No existe el archivo. Se usará la lista inicial.")


while True:
    print("=== GESTOR DE PROGRAMADORES ===")
    print("1. Mostrar todos los programadores")
    print("2. Buscar programador")
    print("3. Agregar programador")
    print("4. Guardar programador")
    print("5. Salir.")

    opcion = input("Elegí una opción: ")
    if opcion == "1":
        try:
            print(mostrar_programadores())
        except ValueError as error:
            print(error)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del programador: ")
        try:
            print(buscar_programador(nombre))
        except ValueError as error:
            print(error)
    elif opcion == "3":
        agregar_programador()
    elif opcion == "4":
        guardar_programadores()
    elif opcion == "5":
        print("Programa finalizado")
        break
    else:
        print("Opción inválida.")





