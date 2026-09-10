cosas = ["python", "java", "c++", "ia", "css"]
cosas.append("sql")
cosas.append("html")
print("Estoy estudiando " + str(len(cosas)) + " tecnologias")

print(f"Estoy estudiando {len(cosas)} tecnologias")
for numero, cosa in enumerate(cosas, start=1):  
    if cosa == "ia":
        print(f"{numero} - la ia es mi objetivo") 
    else: print(f"{numero} - quiero aprender: {cosa}")


    programador = [
        {
            "nombre": "florencia",
            "edad": 30,
            "lenguaje": "python",
            "experiencia": 2
        } 
        ] 
    print(programador[0]["nombre"], programador[0]["edad"])
    programadores = [ {
    
            "nombre": "florencia",
            "edad": 30,
            "lenguaje": "python",
            "experiencia": 2,
    },{
            "nombre": "gaston",
            "edad": 25,
            "lenguaje": "java",
            "experiencia": 3
       } ]

    for programador in programadores: 
        print(f'{programador["nombre"]} usa: {programador["lenguaje"]} y tiene {programador["experiencia"]} años de experiencia')
        if programador["lenguaje"] == "python":
            print (f'{programador["nombre"]} esta estudiando python para especializarse en IA')

    for programador in programadores:
        if programador ["experiencia"] > 2:
            print(f'{programador["nombre"]} tiene mas de 2 años de experiencia')
        else:
            print(f'{programador["nombre"]} tiene menos de 2 años de experiencia')

    for programador in programadores:
        if programador ["lenguaje"] == "python":
            print(f'{programador["nombre"]} usa python')

    for programador in programadores:
        if programador ["lenguaje"] == "python":
            print(f'{programador["nombre"]} usa python y tiene {programador["experiencia"]} años de experiencia')

def saludar(nombre, lenguaje):
    print(f"Hola, me llamo {nombre} y estoy aprendiendo {lenguaje}!")
    saludar("Florencia", "Python")

def calcular_experiencia(años, proyectos):
    return años * proyectos

resultados = calcular_experiencia(2, 5)
print(f"{resultados} años de experiencia acumulada")

def mostrar_programador(programador):
    return f"{programador['nombre']} usa {programador['lenguaje']} y tiene {programador['experiencia']} años de experiencia"

for programador in programadores:
    print(mostrar_programador(programador))