#!/usr/bin/python

class House():
	MinimalBet = 1
	MaxBet = 200
	Bankroll = 10000.0
	Weights = []
	Event = None
	DebugMode = True

	def __init__(self, Event, MinimalBet=1, MaxBet=200, Bankroll = 100000.0):
		self.MinimalBet = MinimalBet
		self.MaxBet = MaxBet
		self.Bankroll = Bankroll
		self.Event = Event

	def __str__(self):
		out = "House:\n"
		out += "\n Bankroll: " + str(self.Bankroll)
		out += "\n Minimal Bet: " + str(self.MinimalBet)
		out += "\n Max Bet: " + str(self.MaxBet)
		if(self.Weights):
			out += "\n Weights: \n"
			for i in range(len(self.Weights)):
				out += "Dimention " + str(i) + ": \n["
				for j in range(len(self.Weights[0])):
					out += " " + str(self.Weights[i][j]) + ","
				out += "]\n"
		out+="\n"
		return out

	def CalculeWeights(self, PlayersOnGame):
		BigWeight = []
		AcumulateWeight = 0
		nOfWeights = len(PlayersOnGame[0].Weights[0])
		self.Weights = [0] * self.Event.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			self.Weights[Dimention] = [0] * nOfWeights
			AcumulateWeight = 0.0
			for Index in range(nOfWeights):
				CurrentWeight = 0.0
				for Player in PlayersOnGame:
					CurrentWeight += Player.Weights[Dimention][Index]
				self.Weights[Dimention][Index] = CurrentWeight
				AcumulateWeight += CurrentWeight
			BigWeight.append(AcumulateWeight)
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
						Award = (1.0 / self.Weights[Dimention][Index*2 + 1]) * Player.Bets[Dimention][Index*2 + 1]
					else:
						Award = (1.0 / self.Weights[Dimention][Index*2]) * Player.Bets[Dimention][Index*2]
					if(Award > 0):
						Player.RecieveAward(Award)
						self.Bankroll -=Award
