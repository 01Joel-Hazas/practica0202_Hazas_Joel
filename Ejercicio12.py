# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca
# y el coste final total.

precioPan = 3.49
descuento = 60
cantPan = int(input("Introduce el número de barras vendidas que no son del dia: "))
costeFinal = cantPan * ( precioPan - (precioPan * (descuento/100)))
print("El coste de una barra normal es " + str(precioPan) + "€")
print("El descuento sobre una barra que no es del día es " + str(descuento) + "%")
print("El coste final a pagar es " + str(round(costeFinal, 2)) + "€")
