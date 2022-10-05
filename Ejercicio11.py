# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.

cantAhorrosInit = float(input("Introduce una cantidad de dinero depositada en la cuenta de ahorros: "))
interes = 1.04
cantAhorrosAño1 = cantAhorrosInit * interes
print("Cantidad de ahorros tras el primer año: " + str(round(cantAhorrosAño1, 2)))
cantAhorrosAño2 = cantAhorrosAño1 * interes
print("Cantidad de ahorros tras el segundo año: " + str(round(cantAhorrosAño2, 2)))
cantAhorrosAño3 = cantAhorrosAño2 * interes
print("Cantidad de ahorros tras el tercer año: " + str(round(cantAhorrosAño3, 2)))

