#!/usr/bin/python

class House():
    MinimalBet = 1
    MaxBet = 200
    Bankroll = 10000.0
    Weights = []

    def __init__(self, minimalBet=1, maxBet=200, bankroll = 10000.0):
        self.MinimalBet = minimalBet
        self.MaxBet = maxBet

    def CalculeWeights(self, PlayersOnGame):
        BigWeight = 0
        
        nOfWeights = len(PlayersOnGame[0].Weights)
        self.Weights = [0] * nOfWeights

        for i in range(nOfWeights):
            CurrentWeight = 0
            for player in PlayersOnGame:
                CurrentWeight += player.Weights[i]
            self.Weights[i] = CurrentWeight
            BigWeight += CurrentWeight

        for i in range(nOfWeights):
            self.Weights /= BigWeight

    def RecieveBet(self, Bet):
        self.Bankroll += Bet

    def PayAward(self, ResultIndex, Player):
        Award = self.Weights[ResultIndex] * Player.Bets[ResultIndex]
        self.Bankroll -=Award
        return Award
