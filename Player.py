
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

	def __init__(self, Event, bankroll=10.0):
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
		out += "\nTendings:\n"
		for i in range(len(self.Tendings)):
			out += "Dimention " + str(i) + ": \n\t["
			for j in range(len(self.Tendings[0])):
				out += " " + str(self.Tendings[i][j]) + ","
			out += "]\n"
		if(self.Weights):
			out += "\nWeights:\n\n"
			for i in range(len(self.Weights)):
				out += "Dimention " + str(i) + ": \n\t["
				for j in range(len(self.Weights[0])):
					out += " " + str(self.Weights[i][j]) + ","
				out += "]\n"
		out += "\nFavorites: \n"
		out += "["
		for i in range(len(self.Favorites)): out += str(self.Favorites[i]) + " "
		out += "]"
		if(self.Bets):
			out+= "\nBets:\n"
			for i in range(len(self.Bets)):
				out += "["
				for j in range(len(self.Bets[0])):
					out += str(self.Bets[i][j]) + " "
				out += "]"
		out+="\n"
		return out

	def CalculeMyWeights(self, Mask):
		self.Weights = [0] * self.Event.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			self.Weights[Dimention] = [1] * (Mask.Size * 2)
			for Index in range(Mask.Size):
				ItemIndex = Mask.Indexes[Dimention][Index]
				self.Weights[Dimention][Index * 2] *= (1 - self.Tendings[Dimention][ItemIndex])
				self.Weights[Dimention][(Index * 2) + 1] *= self.Tendings[Dimention][ItemIndex]

	def MakeBets(self, House):
		BetsPerDimention = len(self.Weights[0])
		self.Bets = [0] * self.Event.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			self.Bets[Dimention] = [0] * BetsPerDimention
			for Index in range(BetsPerDimention):
				Bet = 0
				if(House.Weights[Dimention][Index] >= self.Weights[Dimention][Index]):
					p = House.MinimalBet / self.Weights[Dimention][Index]
					Bet = (p * House.Weights[Dimention][Index])
					Bet = min(self.Bankroll, max(Bet, House.MinimalBet))
					self.Bets[Dimention][Index] = Bet
					self.Bankroll -= Bet
					House.RecieveBet(Bet)

	def isWinner(self, Dimention, BetIndex):
		if(self.Bets[Dimention][BetIndex] > 0): return True
		return False

	def isBroken(self):
		if(self.Bankroll > 0): 
			return False
		return True

	def RecieveAward(self, Montant):
		self.Bankroll += Montant

	def NewPlayer(self):
		return Player(self.Event)
	

#player = Player(3, 51241)
#print(player.Name)
#print(player.Tendings)
#print(player.Bankroll)
