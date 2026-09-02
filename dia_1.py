nombre = "Florencia"
edad = 30
ciudad = "Cordoba"
lenguaje = "JavaScript"



print("Mi nombre es", nombre, "Tengo", edad, "años" "y vivo en", ciudad, "Estoy aprendiendo", lenguaje)
edad_en_5_anios = edad + 10

print("En 10 años tendré", edad_en_5_anios, "años")
a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b  
division = a / b
print(suma, resta, multiplicacion, division)

nombre = input("¿Cómo te llamás? ")
edad = int(input("¿cuantos años tenés? "))

if edad >= 18:
    print("Hola", nombre, "podes ingresar")
    
else:
    print("Hola", nombre, "no podes ingresar")
if edad >= 65:
    print("tenes con descuento")
if edad == 18:
    print("¡acabas de cumplir la mayoria de edad!")
