def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as error:
        print(f"Error: {error}")
        return None



    