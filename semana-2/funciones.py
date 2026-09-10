def saludar(nombre):
    return f"Hola,{nombre}"

def calcular_experiencia(experiencia):
    return experiencia * 12

def determinar_nivel(experiencia):
    if experiencia < 2:
        return "Junior"
    elif experiencia <= 5:
        return "Semi Senior"
    else:
        return "Senior"