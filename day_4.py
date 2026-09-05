programadores = [
    {
        "nombre": "florencia",
        "edad": 30,
        "lenguaje": "python",
        "experiencia": 2
    },
    {
        "nombre": "gaston",
        "edad": 25,
        "lenguaje": "java",
        "experiencia": 3
    },
    {
        "nombre": "afua",
        "edad": 36,
        "lenguaje": "javascript",
        "experiencia": 8
    }
]

for programador in programadores: 
    programador["experiencia"] += 1
    print(f"{programador['nombre']}: {programador['experiencia']}")

for programador in programadores:
    programador["nivel"] = "junior" if programador["experiencia"] < 3 else "senior"
    print(f"{programador['nombre']}, {programador['nivel']}")

lenguajes = ["python", "javascript", "java", "python", "c++"]
lenguajes_python = [lenguajes for lenguajes in lenguajes if lenguajes == "python"]
print(f"{lenguajes_python}")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_mayores = [numero for numero in numeros if numero > 5]
print(f"{numeros_mayores}")

edades = [20, 25, 30, 35]
edades_futuras = [edad +5 for edad in edades]
print(f"{edades_futuras}")

programadores = [
    {"nombre": "Florencia", "lenguaje": "Python"},
    {"nombre": "Gastón", "lenguaje": "Java"},
    {"nombre": "Afua", "lenguaje": "JavaScript"},
    {"nombre": "Lucía", "lenguaje": "Python"}
]
nombres_python =[programador["nombre"] for programador in programadores if programador["lenguaje"] == "Python"]
print(f"{nombres_python}")