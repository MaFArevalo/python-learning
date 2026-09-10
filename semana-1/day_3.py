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
    
    },
    { "nombre": "lucia",
            "edad": 36,
            "lenguaje": "python",
            "experiencia": 8}
]

def evaluar_experiencia(programador):
    if programador ["experiencia"] >= 3:
        return f"{programador['nombre']}: es un programador con experiencia"
    else:
        return f"{programador['nombre']}: es un programador junior"

def evaluar_programadores(programadores):

    for programador in programadores:
        print(evaluar_experiencia(programador))

evaluar_programadores(programadores)

def calcular_experiencia_total (programadores):
    total = 0
    for programador in programadores:
        total += programador["experiencia"]
    return total
print(f"El total de experiencia acumulada es: {calcular_experiencia_total(programadores)} años")


def calcular_python (programadores):
   programadores_python = 0
   for programador in programadores:
       if programador["lenguaje"] == "python":
           programadores_python += 1
   return programadores_python

print(f"El total de programadores que usan python es: {calcular_python(programadores)}")

def buscar_expertos(programadores):
    for programador in programadores:
        if programador["experiencia"] >= 5:
            print(f"{programador['nombre']} es un experto en {programador['lenguaje']}")
buscar_expertos(programadores)

def calcular_promedio_experiencia(programadores):
    total_exp = calcular_experiencia_total(programadores)
    promedio = total_exp / len(programadores)
    return promedio

print(f"el promedio es: {calcular_promedio_experiencia(programadores)} años")
      