with open("datos.txt", "r") as archivo:
    contenido = archivo.readlines()

for cosas in enumerate(contenido, start=1):  
    print(f"{cosas[0]} - {cosas[1].strip()}")

with open ("perfil.txt", "w") as archivo:
    archivo.write("Nombre: Florencia\n")
    archivo.write("Lenguaje: Python\n")
    archivo.write("objetivo: ia engineer\n")

with open ("perfil.txt", "a") as archivo:
    archivo.write("experiencia: 2 años\n")
with open("perfil.txt", "r") as archivo:
    contenido = archivo.readlines()
    for perfil in enumerate(contenido, start=1):
        print(f"{perfil[0]} - {perfil[1].strip()}")
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")

try: 
     numero = int(input("Ingresá un número: "))
except ValueError:
    print("Por favor, ingresa un número válido.")
else:
    print(f"El número ingresado es: {numero}")
finally:
    print("Fin del programa.")
    