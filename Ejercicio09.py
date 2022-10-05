# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión.

cantidad = float(input("¿Que cantidad deseas invertir? "))
interes = float(input("Introduce el interés porcentual anual: "))
años = int(input("¿En cuantos años?"))

def calculoCapital(cantidad:float , interes:float , años:int):
    capitalObtenido = cantidad * (interes/100)*años
    return capitalObtenido;
print ("El capital obtenido de la inversion de " + str(cantidad) + " es " + str(calculoCapital(cantidad, interes , años)))
