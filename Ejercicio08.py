# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
# la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

numEntero1 = int(input("Introduce un número entero positivo: "))
numEntero2 = int(input("Introduce otro número entero positivo: "))

def cociente(numEntero1:int, numEntero2:int):
    coeficiente = numEntero1 // numEntero2
    return coeficiente;

def resto(numEntero1:int , numEntero2:int):
    resto = numEntero1 % numEntero2
    return resto

print ("El cociente de " + str(numEntero1) + " entre " + str(numEntero2) +" nos da " + str(cociente(numEntero1, numEntero2)))
print ("El resto de " + str(numEntero1) + " entre " + str(numEntero2) +" nos da " + str(resto(numEntero1,numEntero2)))
