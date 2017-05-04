#!/usr/bin/python

from House import House
from Event import Event
from Player import Player
from Mask import Mask
from pdb import set_trace as bp

class Game():
	Turns = 5
	Event = None
	House = None
	Players = []
	nOfPlayers = 0
	BestSolution = None
	TempSolution = None
	MaxMissConvergence = 0
	DebugMode = True
	#FileName = ""	
	
	def __init__(self, Turns = 10, nOfPlayers = 1, MaxMissConvergence = 1000):
		self.Event = Event()
		self.House = House(self.Event)
		self.Turns = Turns
		self.MaxMissConvergence = MaxMissConvergence
		self.Players = [0] * nOfPlayers
		self.nOfPlayers = nOfPlayers
		for i in range(self.nOfPlayers):
			self.Players[i] = Player(self.Event)

	def GenerateMask(self):
		self.Mask = Mask(self.Event, self.Players)

	def __str__(self):
		out = "Turns: " + str(self.Turns)
		out += "\nN of Players: " + str(self.nOfPlayers)
		out += "\nPlayers:\n"
		for Player in self.Players: out += str(Player) +"\n"
		return out 

	def Play(self):
		Miss = 0
		BestSolution = {}
		TempSolution = {}
		Solution = {}
		if(self.DebugMode): print(str(self))
		if(self.DebugMode):bp()
		if(self.DebugMode): print(str(self.Event))
		if(self.DebugMode):bp()
		Solution = self.Event.GetInitialSolution()
		if(self.DebugMode): print("Game Start:")
		for Turn in range(self.Turns):
			print("\tTurn " + str(Turn))
			if(self.DebugMode): print("\tGenerationg mask:")
			self.GenerateMask()
			if(self.DebugMode): print("\tMask:")
			if(self.DebugMode): print(str(self.Mask))
			if(self.DebugMode):bp()
			if(self.DebugMode): print("\tCalculing players weight:")
			for Player in self.Players:
				Player.CalculeMyWeights(self.Mask)
				if(self.DebugMode):bp()
			if(self.DebugMode):bp()
			if(self.DebugMode): print("\tCalculing house weight:")
			self.House.CalculeWeights(self.Players)
			if(self.DebugMode):bp()
			if(self.DebugMode): print("\tCalculing players bets:")
			for Player in self.Players:
				Player.MakeBets(self.House)
				if(self.DebugMode):bp()
			if(self.DebugMode):bp()
			if(self.DebugMode): print("\tTrying better solution:")
			TempSolution = self.Mask.TryBetterSolution(Solution)
			if(self.DebugMode): print("\tBetter solution:")
			if(self.DebugMode): print(self.TempSolution)
			if(self.DebugMode):bp()
			if(self.DebugMode): print("\tPaying players Awards:")
			self.House.PayAwards(self.Mask.Size, TempSolution["BestIndexes"], self.Players)
			if(self.DebugMode):bp()
			if(TempSolution["TotalProfit"] > Solution["TotalProfit"]):
				if(self.DebugMode): print("\tBetter solution finded, changing solution")
				Solution = TempSolution
			else:
				if(self.DebugMode): print("\tBetter solution missed")
				Miss +=1
				if(self.DebugMode): print("\tMisses: " + str(Miss))
			for Player in self.Players:
				if(Player.isBroken()): 
					print("Player " + Player.Name + " is broken")
					Player.NewPlayer()
			if(Miss > self.MaxMissConvergence):
				if(self.DebugMode): print("Max misses hited, breaking game")
				break

		print("\nFinal solution:")
		print(str(self.Event))
		print("")
		print(Solution)


		
