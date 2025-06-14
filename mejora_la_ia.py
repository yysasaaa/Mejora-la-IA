# -*- coding: utf-8 -*-

import random

def crear_tablero():
  """Crea un tablero de 3x3 vacío."""
  tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
  return tablero

def imprimir_tablero(tablero):
  """Imprime el estado actual del tablero."""
  print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
  print("-----")
  print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
  print("-----")
  print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")

def movimiento_jugador(tablero, jugador):
  """Maneja el movimiento del jugador humano."""
  while True:
    try:
      fila = int(input("Elige fila (0, 1, 2): "))
      columna = int(input("Elige columna (0, 1, 2): "))

      if 0 <= fila <= 2 and 0 <= columna <= 2:
        if tablero[fila][columna] == " ":
          tablero[fila][columna] = jugador
          break
        else:
          print("¡Casilla ocupada!")
      else:
        print("¡Entrada inválida! Elige filas y columnas entre 0 y 2.")
    except ValueError:
      print("¡Entrada inválida! Por favor, introduce un número válido.")

def hay_ganador(tablero):
  """Verifica si hay un ganador en el tablero actual."""
  # Verificar filas y columnas
  for i in range(3):
    if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
      return True
    if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
      return True

  # Verificar diagonales
  if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
    return True
  if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
    return True

  return False

def tablero_lleno(tablero):
  """Verifica si el tablero está lleno."""
  for fila in tablero:
    if " " in fila:
      return False
  return True

def movimiento_ia(tablero):
  """Realiza un movimiento más inteligente para la IA (bloquea al jugador o gana si es posible)."""
  ia_simbolo = "O"
  jugador_simbolo = "X"

  # 1. Verificar si la IA puede ganar en el siguiente movimiento
  for i in range(3):
    for j in range(3):
      if tablero[i][j] == " ":
        tablero[i][j] = ia_simbolo
        if hay_ganador(tablero):
          return
        tablero[i][j] = " " # Deshacer el movimiento simulado

  # 2. Verificar si el jugador puede ganar en el siguiente movimiento y bloquearlo
  for i in range(3):
    for j in range(3):
      if tablero[i][j] == " ":
        tablero[i][j] = jugador_simbolo
        if hay_ganador(tablero):
          tablero[i][j] = ia_simbolo # Bloquear al jugador
          return
        tablero[i][j] = " " # Deshacer el movimiento simulado

  # 3. Si no hay movimientos ganadores o bloqueantes, realizar un movimiento aleatorio
  casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
  if casillas_vacias:
    fila, columna = random.choice(casillas_vacias)
    tablero[fila][columna] = ia_simbolo


def juego_completo(puntuacion):
  """Ejecuta una partida completa del juego del Gato."""
  tablero = crear_tablero()
  jugador_actual = "X"

  while True:
    imprimir_tablero(tablero)
    print(f"Turno de {jugador_actual}")

    if jugador_actual == "X":
      movimiento_jugador(tablero, jugador_actual)
    else:
      movimiento_ia(tablero)

    if hay_ganador(tablero):
      imprimir_tablero(tablero)
      print(f"¡{jugador_actual} ha ganado!")
      puntuacion[jugador_actual] += 1
      break

    if tablero_lleno(tablero) and not hay_ganador(tablero):
      imprimir_tablero(tablero)
      print("¡Empate!")
      break

    if(jugador_actual=="O"):
      jugador_actual="X"
    else:
      jugador_actual = "O"

# Inicializar puntuación
puntuacion = {"X": 0, "O": 0}

# Bucle principal para jugar varias partidas
while True:
  juego_completo(puntuacion)
  print(f"\nPuntuación actual: Jugador X: {puntuacion['X']}, Jugador O: {puntuacion['O']}")
  jugar_de_nuevo = input("¿Quieres jugar otra partida? (s/n): ").lower()
  if jugar_de_nuevo != 's':
    break

print("¡Gracias por jugar!")
