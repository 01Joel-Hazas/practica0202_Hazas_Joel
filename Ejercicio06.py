#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla
# la suma de todos los enteros desde 1 hasta . La suma de los  primeros enteros positivos puede ser calculada de la
# siguiente forma: suma = n * (n + 1)/2

numEntero = int(input("Introduce un número entero positivo: "))

def suma(numEntero:int):
    suma = numEntero * (numEntero + 1) / 2
    return suma

print ("la suma de todos los enteros desde 1 hasta "  + str(numEntero) +" " + "es " + str(suma(numEntero)))


