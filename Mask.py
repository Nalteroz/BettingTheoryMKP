#!/usr/bin/python

from random import randint

class Mask():
	Indexes = []
	Size = 0
	MaxIndex = 0
	Event = None
	DebugMode = True

	def __init__(self, Event, Players):
		self.Size = len(Players)
		self.Event = Event
		self.Indexes = [0] * self.Event.nOfDimentions
		self.MaxIndex = self.Event.nOfItens - 1
		for Dimention in range(self.Event.nOfDimentions):
			IndexVector = []
			for Player in Players:
				IndexVector.append(Player.Favorites[Dimention])	
			self.Indexes[Dimention] = IndexVector

	def __str__(self):
		out = "\tSize per dimention: " + str(self.Size)
		return out

	def Transformation(self, Solution, Dimention, Index):
		ItensIndex = []
		ItensIndex.extend(Solution[Dimention])        
		TempIndex = -1
		SwapIndex = -1
		BestIndex = -1
		TempProfit = 0
		TempWeight = 0
		BestWeight = 0
		BestProfit = self.Event.CalculeProfit(ItensIndex)
		for i in range(len(ItensIndex)):
			TempIndex = ItensIndex[i]
			ItensIndex[i] = Index
			TempProfit = self.Event.CalculeProfit(ItensIndex)
			TempWeight = self.Event.CalculeWeight(ItensIndex)
			if((TempProfit > BestProfit and TempWeight <= self.Event.Knapsack[Dimention]) or (TempProfit >= BestProfit and TempWeight < BestWeight)):
				SwapIndex = i
				BestProfit = TempProfit
				BestWeight = TempWeight
			ItensIndex[i] = TempIndex
		if(SwapIndex > -1):
			ItensIndex[SwapIndex] = Index
			return {"BetterSolution": ItensIndex, "BetterProfit": BestProfit, "BetterWeight": BestWeight}
		else:
			return None	
		
	def TryBetterSolution(self, Solution):
		if(self.DebugMode): print("Trying Better Solution:")
		nOfDimentions = self.Event.nOfDimentions
		BestSolution = []
		BestSolution.extend(Solution)
		BestProfits = [0] * nOfDimentions
		BestTempSolution = None
		BestIndexes = [0] * nOfDimentions
		if(self.DebugMode): print("Initial solution:")
		if(self.DebugMode): print(BestSolution)
		for Dimention in range(nOfDimentions):
			BestProfits[Dimention] = self.Event.CalculeProfit(Solution[Dimention])
		if(self.DebugMode): print("Initial best profit:")
		if(self.DebugMode): print(BestProfits)
		if(self.DebugMode): print("Start Temptation")
		for Dimention in range(nOfDimentions):
			if(self.DebugMode): print("\tDimention " + str(Dimention))
			if(self.DebugMode): print("\tThe dimention max weight is:" + str(self.Event.Knapsack[Dimention]))
			for Index in range(self.Size):
				if(self.DebugMode): print("\t\tIndex " + str(Index))
				BestTempSolution = self.Transformation(BestSolution, Dimention, self.Indexes[Dimention][Index])
				if(self.DebugMode): print("\t\t\tTemporary best solution is: ")
				if(self.DebugMode): print(BestTempSolution)
				if(BestTempSolution):
					if(self.DebugMode): print("\t\t\t\tSubstituing")
					BestSolution[Dimention] = BestTempSolution["BetterSolution"]
					BestProfits[Dimention] = BestTempSolution["BetterProfit"]
					BestIndexes[Dimention] = Index
		
		return {"BestSolution": BestSolution, "BestIndexes": BestIndexes, "BestProfits": BestProfits}
