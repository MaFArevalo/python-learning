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
def mostrar_programador(programador):
    return f"Nombre:{programador['nombre']} \n lenguaje: {programador['lenguaje']}\n experiencia: {programador['experiencia']}"

for programador in programadores:
    print(mostrar_programador(programador))