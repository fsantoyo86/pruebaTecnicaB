# Puntería
# En 20 ocasiones, cada jugador lanzó una jabalina a un campo abierto.
# El objetivo era medir la puntería, por lo que se registraron las 
# coordenadas en las que cayó la jabalina en cada intento.
# ¿De qué forma se te ocurre visualizar esta información?

import pandas as pd
import matplotlib.pyplot as plt

# Determina el promedio de una lista dada
def average(list):
  sum = 0
  for i in list:
   sum = sum + i
  prom = sum / len(list)
  return prom

# El enfoque a resolver es sacar el punto promedio de las latitudes y longitudes
# para graficarlo y para un determinado radio alrededor del punto ver el número
# de tiros que caen dentro.

# Enfoques adicionales podrían contar con el descartar outliers para que el promedio 
# no se vea tan afectado

def prueba3():
  file = pd.read_csv("./position_of_players.csv")
  print(file.head(100))

  player1 = file.loc[file['No'] == "Player 1"]
  player2 = file.loc[file['No'] == "Player 2"]
  player3 = file.loc[file['No'] == "Player 3"]
  player4 = file.loc[file['No'] == "Player 4"]
  player5 = file.loc[file['No'] == "Player 5"]

  latitudeAVG1 = []
  longitudAVG1 = []
  latitudeAVG2 = []
  longitudAVG2 = []
  latitudeAVG3 = []
  longitudAVG3 = []
  latitudeAVG4 = []
  longitudAVG4 = []
  latitudeAVG5 = []
  longitudAVG5 = []

  # Se crean los puntos promedio tanto de longitud como latitude
  latitudeAVG1.append(average(player1['Latitude']))
  longitudAVG1.append(average(player1['Longitud']))
  latitudeAVG2.append(average(player2['Latitude']))
  longitudAVG2.append(average(player2['Longitud']))
  latitudeAVG3.append(average(player3['Latitude']))
  longitudAVG3.append(average(player3['Longitud']))
  latitudeAVG4.append(average(player4['Latitude']))
  longitudAVG4.append(average(player4['Longitud']))
  latitudeAVG5.append(average(player5['Latitude']))
  longitudAVG5.append(average(player5['Longitud']))

  # Se crean las graficas para cada uno de los jugadores junto con la
  # vecindad para contar el número de puntos dentro de
  
  figure, axis = plt.subplots(2,3)
  axis[0, 0].set_xlim(left=24.8, right=25)
  axis[0, 0].set_ylim(bottom=121.4, top=121.6)
  axis[0, 0].scatter(player1['Latitude'], player1['Longitud'], label = "Player 1")
  axis[0, 0].set_title("Player 1")
  axis[0, 1].set_xlim(left=24.8, right=25)
  axis[0, 1].set_ylim(bottom=121.4, top=121.6)
  axis[0, 1].scatter(player2['Latitude'], player2['Longitud'], label = "Player 2", color='r')
  axis[0, 1].set_title("Player 2")
  axis[0, 2].set_xlim(left=24.8, right=25)
  axis[0, 2].set_ylim(bottom=121.4, top=121.6)
  axis[0, 2].scatter(player3['Latitude'], player3['Longitud'], label = "Player 3", color='green')
  axis[0, 2].set_title("Player 3")
  axis[1, 0].set_xlim(left=24.8, right=25)
  axis[1, 0].set_ylim(bottom=121.4, top=121.6)
  axis[1, 0].scatter(player4['Latitude'], player4['Longitud'], label = "Player 4", color='pink')
  axis[1, 0].set_title("Player 4")
  axis[1, 1].set_xlim(left=24.8, right=25)
  axis[1, 1].set_ylim(bottom=121.4, top=121.6)
  axis[1, 1].scatter(player5['Latitude'], player5['Longitud'], label = "Player 5", color='purple')
  axis[1, 1].set_title("Player 5")
  axis[0, 0].scatter(latitudeAVG1, longitudAVG1, label = "Averages1", color='yellow')
  circle1 = plt.Circle((latitudeAVG1[0], longitudAVG1[0]), radius=0.025, color='yellow', fill=False, clip_on=False)
  axis[0, 0].add_patch(circle1)
  axis[0, 1].scatter(latitudeAVG2, longitudAVG2, label = "Averages2", color='yellow')
  circle2 = plt.Circle((latitudeAVG2[0], longitudAVG2[0]), radius=0.025, color='yellow', fill=False, clip_on=False)
  axis[0, 1].add_patch(circle2)
  axis[0, 2].scatter(latitudeAVG3, longitudAVG3, label = "Averages3", color='yellow')
  circle3 = plt.Circle((latitudeAVG3[0], longitudAVG3[0]), radius=0.025, color='yellow', fill=False, clip_on=False)
  axis[0, 2].add_patch(circle3)
  axis[1, 0].scatter(latitudeAVG4, longitudAVG4, label = "Averages4", color='yellow')
  circle4 = plt.Circle((latitudeAVG4[0], longitudAVG4[0]), radius=0.025, color='yellow', fill=False, clip_on=False)
  axis[1, 0].add_patch(circle4)
  axis[1, 1].scatter(latitudeAVG5, longitudAVG5, label = "Averages5", color='yellow')
  circle5 = plt.Circle((latitudeAVG5[0], longitudAVG5[0]), radius=0.025, color='yellow', fill=False, clip_on=False)
  axis[1, 1].add_patch(circle5)

  plt.xlim([23, 25])
  plt.ylim([120, 122])

  plt.show()

prueba3()

