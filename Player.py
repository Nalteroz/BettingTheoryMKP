#!/usr/bin/python

from random import random
from names import randomName


class Player():
    Name = "Fulano"
    Tendings = []
    Bets = []
    Bankroll = 1000.0
    Weights = []

    def __init__(self, SizeOfTendings, bankroll=100.0):
        if(SizeOfTendings<=0):
            print("Erro on instantiate player! Size of tendings has incorrect value.")
            return
        self.Bankroll = bankroll
        self.Name = randomName()
        self.Tendings = [0] * SizeOfTendings
        for i in range(SizeOfTendings):
            self.Tendings[i] = random()

    def CalculeWeight(self, mask):
        pass

    def MakeBets(self, house):
        pass

    def isWinner(self, BetIndex):
        if(self.Bets[BetIndex] > 0): return True
        return False

    def isBroken(self):
        if(self.Bankroll > 0): return False
        return True

    def GetAward(self, house, BetIndex):
        pass

    def NewPlayer(self):
        return Player(len(self.Tendings))
    

#player = Player(3, 51241)
#print(player.Name)
#print(player.Tendings)
#print(player.Bankroll)
