#!/usr/bin/python

from House import House
from Event import Event
from Player import Player
from Mask import Mask

class Game():
	Turns = 5
	Event = None
	House = None
	Players = []
	nOfPlayers = 0
	BestSolution = None
	TempSolution = None
	Solution = []
	MaxMissConvergence = 0
	#FileName = ""	
	
	def __init__(Turns = 1000, nOfPlayers = 20, MaxMissConvergence = 1000):
		self.Event = Event()
		self.House = House(self.Event)
		self.Turns = Turns
		self.MaxMissConvergence = MaxMissConvergence
		self.Players = [0] * nOfPlayers
		self.nOfPlayers = nOfPlayers
		for i in range(self.nOfPlayers):
			self.Players[i] = Player(self.Event)

	def GenerateMask():
		self.Mask = Mask(self.Event, self.Players)

	def Play():
		Miss = 0
		self.Solution = self.Event.GetInitialSolution()
		for Turn in range(self.Turns):
			self.GenerateMask()
			for Player in self.Players:
				Player.CalculeMyWeight(self.Mask)
			self.House.CalculeWeights(self.Players)
			for Player in self.Players:
				Player.MakeBets(self.House)
			self.TempSolution = self.Mask.TryBetterSolution(self.Solution)
			self.House.PayAwards(self.Mask.Size, self.TempSolution["BestIndexes"], Players)
			if(BestSolution is not None or TempSolution["BestProfit"] > BestSolution["BestProfit"]):
				BestSolution = TempSolution
			else:
				Miss +=1
			for Player in self.Players:
				if(Player.isBroken()): Player.NewPlayer()




		
