# Genero de videojuego favorito
# Determina el promedio de partidas ganadas por jugador para 3 tipos diferentes de videojuego
import pandas as pd


#Función que determina el promedio de puntuación para un tipo de videojuego de un jugador particular
def findAverage(list):
  sum = 0
  for ele in list:
    if (int(ele) > 10):
      sum = sum + 1

  prom = sum / len(list)
  return prom * 100

#Función que calcula los promedios de los jugadores, lee el archivo csv utilizando pandas
def successCampaign():
  file = pd.read_csv("./scores_by_game_and_player.csv")

  # lista que contiene los jugadores que participaron
  players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

  # listas donde se hace la limpieza del archivo csv para cada tipo de juego
  FPSlist = []
  ActionList = []
  RPGList = []

  #listas donde se almacenan los procentajes por jugador para cada tipo de juego
  porcentajeFPS = []
  porcentajeAction = []
  porcentajeRPG = []

  #Se hace el filtrado de las columnas por Player ID y tipo de juego
  for pl in players:
    FPSlist.append(file.loc[(file['Player ID'] == pl) & (file['Adventure ID'] == "FPS")])
    ActionList.append(file.loc[(file['Player ID'] == pl) & (file['Adventure ID'] == "ACTION")])
    RPGList.append(file.loc[(file['Player ID'] == pl) & (file['Adventure ID'] == "RPG")])

  # Se determinan los promiedios pasando La columna Score de cada lista
  for i in range(5):
    porcentajeFPS.append(findAverage(FPSlist[i]['Score']))
    porcentajeAction.append(findAverage(ActionList[i]['Score']))
    porcentajeRPG.append(findAverage(RPGList[i]['Score']))

    print("Player ",i+1," FPS: ", porcentajeFPS[i], "%, Action: ", porcentajeAction[i], "%, RPG: ", porcentajeRPG[i],"%")

successCampaign()
