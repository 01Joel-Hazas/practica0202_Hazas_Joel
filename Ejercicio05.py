# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

numHoras = int(input("Introduce el número de horas trabajadas: "))
costeHora = int(input("Introduce el coste por hora: "))
paga = numHoras * costeHora
print("¡La paga correspondiente es" + " " + str(paga) + " !")