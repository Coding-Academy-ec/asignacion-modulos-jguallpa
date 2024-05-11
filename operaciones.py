def suma(a, b):
    sumas = a + b 
    return sumas # Return de la suma

def resta(a, b):
    restas = a -b
    return restas # Return de la resta

def multiplicacion(a, b):
    multiplicar= a * b 
    return multiplicar

def division(a, b):
    if b != 0:
        dividir= a/b
        return dividir # Return de la división
    else:
        return "Error: división por cero"  # Return de error
