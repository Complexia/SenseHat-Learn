from electronicDie import Die

import csv
from time import sleep

from classes import Engine
from classes import Player

def main():
    engine = Engine()
    engine.addPlayer(Player(1))
    engine.addPlayer(Player(2))

    hasPlayerBeenPrompted = False

    die = Die()
    while True:
        if not hasPlayerBeenPrompted:
            engine.gameStart()
            hasPlayerBeenPrompted = True
        if die.detectShake():
            sleep(1)
            break

    engine.gameInstructions()
    hasPlayerBeenPrompted = False

    while True:
        if not hasPlayerBeenPrompted:
            engine.promptRoll()
            sleep(3)
            hasPlayerBeenPrompted = True
        if die.detectShake():
            number = die.roll(engine.getCurrentPlayer())
            engine.playerScores(number)
            hasPlayerBeenPrompted = False
            sleep(3)
            engine.nextPlayerTurn()
        if engine.hasPlayerWon():
            engine.gameOver()
            break
main()