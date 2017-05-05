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
		out += "\n\tBankroll: " + str(self.Bankroll)
		out += "\n\tMinimal Bet: " + str(self.MinimalBet)
		out += "\n\t\Max Bet: " + str(self.MaxBet)
		return out

	def CalculeWeights(self, PlayersOnGame):
		if(self.DebugMode): print("Calculing weights:")
		BigWeight = []
		AcumulateWeight = 0
		nOfWeights = len(PlayersOnGame[0].Weights[0])
		if(self.DebugMode): print("\tWeights per dimention: " + str(nOfWeights))
		self.Weights = [0] * self.Event.nOfDimentions
		if(self.DebugMode): print("\tCalculing")
		for Dimention in range(self.Event.nOfDimentions):
			if(self.DebugMode): print("\t\tDimention " + str(Dimention))
			self.Weights[Dimention] = [0] * nOfWeights
			AcumulateWeight = 0.0
			for Index in range(nOfWeights):
				if(self.DebugMode): print("\t\t\tIndex " + str(Index))
				CurrentWeight = 0.0
				for Player in PlayersOnGame:
					CurrentWeight += Player.Weights[Dimention][Index]
				if(self.DebugMode): print("\t\t\tWeight: " + str(CurrentWeight))
				self.Weights[Dimention][Index] = CurrentWeight
				AcumulateWeight += CurrentWeight
				if(self.DebugMode): print("Acumulated weight: " + str(AcumulateWeight))
			if(self.DebugMode): print("\t\tDimention big weight " + str(AcumulateWeight))
			BigWeight.append(AcumulateWeight)
		for Dimention in range(self.Event.nOfDimentions):
			for Index in range(nOfWeights):
				self.Weights[Dimention][Index] /= BigWeight[Dimention]
		if(self.DebugMode): print("Final Weights: ")
		if(self.DebugMode): print(self.Weights)

	def RecieveBet(self, Bet):
		if(self.DebugMode): print("\tBet recieved.")
		self.Bankroll += Bet
	
	def PayAwards(self, MaskSize, WinnerIndexes, Players):
		if(self.DebugMode): print("Payng awards")
		Award = 0
		for Player in Players:
			if(self.DebugMode): print("\tPayng to " + Player.Name)
			for Dimention in range(self.Event.nOfDimentions):
				if(self.DebugMode): print("\t\tDimention " + str(Dimention))
				for Index in range(MaskSize):
					if(self.DebugMode): print("\t\t\tMask index " + str(Index))
					if(Index == WinnerIndexes[Dimention]):
						Award = (1.0 / self.Weights[Dimention][Index*2 + 1]) * Player.Bets[Dimention][Index*2 + 1]
						if(self.DebugMode): print("\t\t\tHe bet : " + str(Player.Bets[Dimention][Index*2 + 1]))
					else:
						Award = (1.0 / self.Weights[Dimention][Index*2]) * Player.Bets[Dimention][Index*2]
						if(self.DebugMode): print("\t\t\tHe bet : " + str(Player.Bets[Dimention][Index*2]))
					if(Award > 0):
						if(self.DebugMode): print("\t\t\tHe recived award: " + str(Award))
						Player.RecieveAward(Award)
						self.Bankroll -=Award
