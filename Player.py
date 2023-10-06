class Player:

    def __init__(self):
        self.__name = None  # Stores the player's name
        self.__symbol = None  # Stores either an "X" or an "O"

    def setName(self, name):
        self.__name = name

    def setSymbol(self, symbol):
        self.__symbol = symbol

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol
