# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5,
# 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000

# Función que recibe el número limite (n) y los dos parametros multiplos (mul1, mul2)
# Se
def findSumMultiples(n, mul1, mul2):
  sum = 0
  # Ciclo que itera sobre los números menores que el limite, revisa si van siendo
  # multiplos de los parametros mul1 y mul2 y los va sumando en la variable sum
  for i in range(n):
    # Se verifica que sean multiplos de los parametros dados
    if i % mul1 == 0 or i % mul2 == 0:
      sum = sum + i
  print("Suma: ", sum)

findSumMultiples(1000, 3, 5)
