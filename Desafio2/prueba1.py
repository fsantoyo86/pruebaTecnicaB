# Durante 30 días se registró el tiempo en minutos que tardó cada jugador en llegar 
# a un score determinado. ¿Cómo harías una gráfica para observar 
# su desempeño a lo largo de los 30 días?

import pandas as pd
import matplotlib.pyplot as plt

# Función que realiza la grafica del tiempo que tardó cada jugador en llegar a un score
def prueba1():
  # Se lee el archivo csv con la librería pandas
  file = pd.read_csv("./tiempos_para_llegar_al_mejor_score.csv")

  # Se muestra la estrututa del csv imprimiento los primeros 20 resultados
  print(file.head(20))

  # Se filtra para cada jugador por medio del Player ID
  player1 = file.loc[file['Player ID'] == "Player 1"]
  player2 = file.loc[file['Player ID'] == "Player 2"]
  player3 = file.loc[file['Player ID'] == "Player 3"]
  player4 = file.loc[file['Player ID'] == "Player 4"]
  player5 = file.loc[file['Player ID'] == "Player 5"]

  # Se grafica mediante matplotlib para cada jugador los minutos contra  el dia
  plt.plot(player1['Day'], player1['Minutes to get that score'], label = "Player 1")
  plt.plot(player2['Day'], player2['Minutes to get that score'], label = "Player 2")
  plt.plot(player3['Day'], player3['Minutes to get that score'], label = "Player 3")
  plt.plot(player4['Day'], player4['Minutes to get that score'], label = "Player 4")
  plt.plot(player5['Day'], player5['Minutes to get that score'], label = "Player 5")
  plt.xlabel('Days')
  plt.ylabel('Time (minutes)')

  plt.title('Number of minutes per day')
  plt.legend()
  plt.show()

prueba1()

