from datetime import datetime
from sense_hat import SenseHat

import csv

class Player:
    def __init__(self, id : int):
        self.__id = id
        self.__score = 0

    def getId(self):
        return self.__id

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def resetScore(self):
        self.__score = 0

class Engine:
    def __init__(self, target = 30):
        sense = SenseHat()
        self.__players = []
        self.__messageHandler = MessageHandler(sense)
        self.__timeSensor = TimeSensor(sense)
        self.__target = target

    def addPlayer(self, player):
        if not self.__maxPlayers():
            self.__players.append(player)
            if self.__maxPlayers():
                self.__currentPlayer = self.getPlayerById(1)

    def getCurrentPlayer(self):
        return self.__currentPlayer

    def getPlayerById(self, id : int):
        return self.__players[id - 1]

    def gameStart(self):
        self.__messageHandler.promptGameStart()

    def gameInstructions(self):
        self.__messageHandler.displayInstructions()
        self.__timeSensor.setStartingTime()

    def promptRoll(self):
        self.__messageHandler.promptRoll(self.__currentPlayer.getId())

    def nextPlayerTurn(self):
        self.__currentPlayer = self.__getOtherPlayer(self.__currentPlayer.getId())

    def playerScores(self, score):
        self.__currentPlayer.increaseScore(score)
        self.__messageHandler.rolledDie(self.__currentPlayer.getId(), score)

    def hasPlayerWon(self):
        return self.getPlayerById(1).getScore() > self.__target or self.getPlayerById(2).getScore() > self.__target

    def gameOver(self):
        self.__timeSensor.setEndingTime()
        gameDuration = self.__timeSensor.calculateDuration() 
        with open('results.csv', mode='w') as csv_file:
            results_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow(['id', 'score', 'time'])
            for player in self.__players:
                results_writer.writerow([player.getId(), player.getScore(), str((gameDuration)).split('.')[0]])
        self.__messageHandler.finalResults(self.__players)

    def promptGameReset(self):
        self.__messageHandler.promptGameReset()

    def resetGame(self):
        for player in self.__players:
            player.resetScore()

    def __getOtherPlayer(self, id):
        for player in self.__players:
            if player.getId() != id:
                return player

    def __maxPlayers(self):
        return len(self.__players) == 2

class TimeSensor:
    def __init__(self, sense):
        self.__sense = sense

    def setStartingTime(self):
        self.__startingTime = datetime.now()

    def setEndingTime(self):
        self.__endingTime = datetime.now()

    def calculateDuration(self):
        return self.__endingTime - self.__startingTime

    def resetTimeBounds(self):
        self.__startingTime = None
        self.__endingTime = None

class MessageHandler:
    def __init__(self, sense):
        self.__sense = sense

    def promptGameStart(self):
        message = 'Please shake the Pi to start'
        print(message)
        self.__sense.show_message(message, scroll_speed = 0.05)

    def displayInstructions(self):
        message = 'This is a 2 player game, player 1 automatically goes first. The LED screen will indicate whose turn it is to roll: player 1 (red), player 2 (blue). To roll the die, gently shake the Pi.'
        print(message)
        self.__sense.show_message(message, scroll_speed = 0.05)

    def promptRoll(self, id):
        message = 'Player {}\'s turn'.format(id)
        print(message)
        if id == 1:
            self.__sense.clear((255, 0, 0))
        else:
            self.__sense.clear((0, 0, 255))

    def rolledDie(self, id, number):
        message = 'Player {} rolled a {}'.format(id, number)
        print(message)
        # self.__sense.show_message(message)

    def finalResults(self, players):
        message = 'Final scores, Player 1: {}, Player 2: {}!'.format(players[0].getScore(), players[1].getScore())
        print(message)
        self.__sense.show_message(message, scroll_speed = 0.05)

    def promptGameReset(self):
        message = 'Please shake the Pi to restart'
        print(message)
        self.__sense.show_message(message)