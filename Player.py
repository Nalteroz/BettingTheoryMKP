
from random import random
from Names import randomName


class Player():
	Name = "Fulano"
	Tendings = []
	Favorites = []
	Bets = []
	Bankroll = 1000.0
	Weights = []
	Event = None
	DebugMode = True

	def __init__(self, Event, bankroll=1000.0):
		self.Bankroll = bankroll
		self.Name = randomName()
		self.Event = Event
		self.Tendings = [0] * self.Event.nOfDimentions
		self.Favorites = [0] * self.Event.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			self.Tendings[Dimention] = [0] * self.Event.nOfItens
			Favorite = -1
			for Index in range(self.Event.nOfItens):
				self.Tendings[Dimention][Index] = random()
				if(Favorite <0 or self.Tendings[Dimention][Index] > self.Tendings[Dimention][Favorite]):
					Favorite = Index
			self.Favorites[Dimention] = Favorite

	def __str__(self):
		out = "Player name:\n" + str(self.Name) 
		out += "\nBankroll: " + str(self.Bankroll)
		out += "\nTendings Lens: \n"
		for i in range(len(self.Tendings)): out += " " + str(len(self.Tendings[i]))
		out += "\nFavorites: \n"
		for i in range(len(self.Favorites)): out += " " + str(self.Favorites[i])
		out+= "\n"
		return out

	def CalculeMyWeights(self, Mask):
		if(self.DebugMode): print("Calculing weights of " + self.Name)
		self.Weights = [0] * self.Event.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			self.Weights[Dimention] = [1] * (Mask.Size * 2)
			for Index in range(Mask.Size):
				ItemIndex = Mask.Indexes[Dimention][Index]
				self.Weights[Dimention][Index * 2] *= (1 - self.Tendings[Dimention][ItemIndex])
				self.Weights[Dimention][(Index * 2) + 1] *= self.Tendings[Dimention][ItemIndex]
		if(self.DebugMode): print("Weights:")
		if(self.DebugMode): print(self.Weights)

	def MakeBets(self, House):
		if(self.DebugMode): print("Calculing Bets of " + self.Name)
		BetsPerDimention = len(self.Weights[0])
		self.Bets = [0] * self.Event.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			if(self.DebugMode): print("\tDimention " + str(Dimention))
			if(self.DebugMode): print("\tBets per dimention = " + str(BetsPerDimention))
			self.Bets[Dimention] = [0] * BetsPerDimention
			for Index in range(BetsPerDimention):
				if(self.DebugMode): print("\t\tIndex " + str(Index))
				Bet = 0
				if(self.DebugMode): print("\t\tMy Weight: " + str(self.Weights[Dimention][Index]))
				if(self.DebugMode): print("\t\tHouse Weight: " + str(House.Weights[Dimention][Index]))
				if(House.Weights[Dimention][Index] >= self.Weights[Dimention][Index]):
					if(self.DebugMode): print("\t\tHouse weight is better.")
					p = House.MinimalBet / self.Weights[Dimention][Index]
					if(self.DebugMode): print("\t\tP:" + str(p))
					Bet = (p * House.Weights[Dimention][Index])
					if(self.DebugMode): print("\t\t\tBet value: " + str(Bet))
					Bet = min(self.Bankroll, max(Bet, House.MinimalBet))
					if(self.DebugMode): print("\t\t\tMin bet value: " + str(Bet))
					self.Bets[Dimention][Index] = Bet
					self.Bankroll -= Bet
					House.RecieveBet(Bet)
		if(self.DebugMode): print(self.Bets)

	def isWinner(self, Dimention, BetIndex):
		if(self.Bets[Dimention][BetIndex] > 0): return True
		return False

	def isBroken(self):
		if(self.Bankroll > 0): return False
		return True

	def RecieveAward(self, Montant):
		self.Bankroll += Montant

	def NewPlayer(self):
		if(self.DebugMode): print(self.Name + "Will be a new player.")
		return Player(self.Event)
	

#player = Player(3, 51241)
#print(player.Name)
#print(player.Tendings)
#print(player.Bankroll)
