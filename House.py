#!/usr/bin/python

class House():
	MinimalBet = 1
	MaxBet = 200
	Bankroll = 10000.0
	Weights = []
	Event = None

	def __init__(self, Event, MinimalBet=1, MaxBet=200, Bankroll = 10000.0):
		self.MinimalBet = MinimalBet
		self.MaxBet = MaxBet
		self.Bankroll = Bankroll
		self.Event = Event

	def CalculeWeights(self, PlayersOnGame):
		BigWeight = []
		nOfWeights = len(PlayersOnGame[0].Weights[0])
		self.Weights = [0] * self.Event.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			self.Weights[Dimention] = [0] * nOfWeights
			for Index in range(nOfWeights):
				CurrentWeight = 0
				for Player in PlayersOnGame:
					CurrentWeight += Player.Weights[Dimention][Index]
				self.Weights[Dimention][Index] = CurrentWeight
				BigWeight.append(CurrentWeight)

		for Dimention in range(self.Event.nOfDimentions):
			for Index in range(nOfWeights):
				self.Weights[Dimention][Index] /= BigWeight[Dimention]

	def RecieveBet(self, Bet):
		self.Bankroll += Bet
	
	def PayAwards(self, MaskSize, WinnerIndexes, Players):
		Award = 0
		for Player in Players:
			for Dimention in range(self.Event.nOfDimentions):
				for Index in range(MaskSize):
					if(Index == WinnerIndexes[Dimention]):
						Award = self.Weights[Dimention][Index*2 + 1] * Player.Bets[Dimention][Index*2 + 1]
					else:
						Award = self.Weights[Dimention][Index*2] * Player.Bets[Dimention][Index*2]
					if(Award > 0):
						Player.RecieveAward(Award)
						self.Bankroll -=Award
