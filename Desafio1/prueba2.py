# How many Sundays fell on the first of the month during the twentieth century (1 Jan
# 1901 to 31 Dec 2000)?

#Función que determina si un año es bisiesto o no
# Recibe como parámetro el año
def determineYearLeap(year):
  leap = False
  if year % 4 == 0:
    leap = True
  elif year % 100 != 0:
    leap = False
  elif year % 400 == 0:
    leap = True
  return leap

# función que cuenta el número de domingos
def countingSundays():
    # Iniciamos la variable en 2 porque el 1 enero de 1901 fue martes
    days = 2
    sunday_count = 0

    # Arreglo con la longitud en días de cada mes
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Se itera sobre los años
    for year in range(1901,2001):

	# Se itera sobre los meses
        for month in range(12):
            days += months[month]
            # Compara si el año es bisiesto y el mes tiene 28 días 
            # para sumarle un día
            if determineYearLeap(year) and months[month] == 28:
                days += 1
            # Verifica si corresponde al día domingo y suma al contador
            if days % 7 == 0:
                sunday_count += 1

    print( "Sundays:", sunday_count)

countingSundays()
