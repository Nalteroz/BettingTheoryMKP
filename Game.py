#!/usr/bin/python

import House from House
import Event from Event
import Player from Player
import Mask from Mask

class Game():
	Turns = 5
	Event = None
	House = None
	Players = []
	nOfPlayers = 0
	Solution = []
	MaskSize = 0
	#FileName = ""	
	
	def __init__(Turns = 1000, nOfPlayers = 20, MaskSize = 3, MaxMissConvergence = 1000):
		self.Event = Event()
		self.House = House(self.Event)
		self.MaskSize = MaskSize
		self.Turns = Turns
		self.Players = [0] * nOfPlayers
		self.nOfPlayers = nOfPlayers
		
		for i in range(self.nOfPlayers):
			self.Players[i] = Player(self.Event)

	def GenerateMask():
		self.Mask = Mask(self.MaskSize, self.Event.nOfDimentions, self.Event.nOfItens - 1)

	def Play():

		self.Solution = self.Event.GetInitialSolution()

		for Turn in range(self.Turns):
			self.GenerateMask()
			for Player in self.Players:
				Player.CalculeMyWeight(self.Mask)
			self.House.CalculeWeights(self.Players)
			for Player in self.Players:
				Player.MakeBets(self.House)
			self.Mask.TryBetterSolution(self.Solution)
			




		
