
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
				if(Favorite <0 or self.Tendings[Dimention][Index] > Tendings[Dimention][Favorite]):
					Favorite = Index
			Favorites[Dimention] = Favorite

	def CalculeMyWeights(self, Mask):
		self.Weights = [0] * self.Event.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			self.Weights[Dimention] = [1] * (Mask.Size * 2)
			for Index in range(Mask.Size):
				self.Weights[Dimention][Index * 2] *= (1 - self.Tendings[Dimention][Mask.Indexes[Dimention][Index]])
				self.Weights[Dimention][(Index * 2) + 1] *= self.Tendings[Dimention][Mask.Indexes[Dimention][Index]]

	def MakeBets(self, House):
		BetsPerDimention = len(self.Weights[0])
		Bets = [0] * self.nOfDimentions
		for Dimention in range(self.Event.nOfDimentions):
			for Index in range(BetsPerDimention):
				Bet = 0
				if(House.Weights[Dimention][Index] > self.Weights[Dimention][Index]):
					p = 1.0/self.Weights[Dimention][Index]
					Bet = ((p*House.Weights[Dimention][Index] - 1)/(House.Weights[Dimention][Index] - 1))*self.Bankroll
					Bet = min(self.Bankroll, max(Bet, House.MinimalBet))
					self.Bets[Dimention][Index] = Bet
					self.Bankroll -= Bet
					House.RecieveBet(Bet)

	def isWinner(self, Dimention, BetIndex):
		if(self.Bets[Dimention][BetIndex] > 0): return True
		return False

	def isBroken(self):
		if(self.Bankroll > 0): return False
		return True

	def RecieveAward(self, Montant):
		self.Bankroll += Montant

	def NewPlayer(self):
		return Player(self.Event)
	

#player = Player(3, 51241)
#print(player.Name)
#print(player.Tendings)
#print(player.Bankroll)
