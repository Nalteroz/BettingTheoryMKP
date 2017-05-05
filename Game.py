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
		if(self.BestSolution):
			out +="BestSolution: \n"
			for i  in len(self.BestSolution):
				out += "["
				for j in len(self.BestSolution[0]): out += str(self.BestSolution[i][j]) + " "
				out += "]"
		out+="\n"
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
		if(self.DebugMode): print("\nGame Start:")
		for Turn in range(self.Turns):
			print("\tTurn " + str(Turn))
			if(self.DebugMode): print("\nGenerationg mask:")
			self.GenerateMask()
			if(self.DebugMode): print("\nMask:")
			if(self.DebugMode): print(str(self.Mask))
			if(self.DebugMode):bp()
			if(self.DebugMode): print("\nCalculing players weight:")
			for Player in self.Players:
				Player.CalculeMyWeights(self.Mask)
				print(str(Player))
				if(self.DebugMode):bp()
			if(self.DebugMode): print("\nCalculing house weight:")
			self.House.CalculeWeights(self.Players)
			print(str(self.House))
			if(self.DebugMode):bp()
			if(self.DebugMode): print("\nCalculing players bets:")
			for Player in self.Players:
				Player.MakeBets(self.House)
				print(str(Player))
				if(self.DebugMode):bp()
			if(self.DebugMode): print("\nTrying better solution:")
			TempSolution = self.Mask.TryBetterSolution(Solution)
			if(self.DebugMode): print("\nBetter solution:")
			if(self.DebugMode): print(self.TempSolution)
			if(self.DebugMode):bp()
			if(self.DebugMode): print("\nPaying players Awards:")
			self.House.PayAwards(self.Mask.Size, TempSolution["BestIndexes"], self.Players)
			if(self.DebugMode):bp()
			if(TempSolution["TotalProfit"] > Solution["TotalProfit"]):
				if(self.DebugMode): print("\nBetter solution finded, changing solution")
				Solution = TempSolution
			else:
				if(self.DebugMode): print("\nBetter solution missed")
				Miss +=1
				if(self.DebugMode): print("\nMisses: " + str(Miss))
			for Player in self.Players:
				if(Player.isBroken()): 
					print("\nPlayer " + Player.Name + " is broken")
					Player.NewPlayer()
			if(Miss > self.MaxMissConvergence):
				if(self.DebugMode): print("\nMax misses hited, breaking game")
				break

		print("\nFinal solution:")
		print(str(self.Event))
		print("")
		print(Solution)


		
