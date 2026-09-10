from funciones import saludar
saludar("Flor")


import funciones

mensaje = funciones.saludar("Flor")
meses = funciones.calcular_experiencia(6)
nivel = funciones.determinar_nivel(5)

print(mensaje)
print(f"Los meses de experiencia del programador son: {meses}")
print(f"El programador es: {nivel}")

import funciones as fn

mensaje = fn.saludar("Flor")
meses = fn.calcular_experiencia(6)
nivel = fn.determinar_nivel(5)

import calculadora as calc
sumas = calc.sumar(10,5)
restas = calc.restar(20,8)
multiplicaciones = calc.multiplicar(6,4)
divisiones = calc.dividir(3,0)

print(f"resultado {sumas}")
print(f"resultado {restas}")
print(f"resultado {multiplicaciones}")
print(f"resultado {divisiones}")
