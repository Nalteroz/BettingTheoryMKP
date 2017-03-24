#!/usr/bin/python

from random import randint

class Mask():
	Indexes = []
	Size = 0
	MaxIndex = 0
	Event = None

	def __init__(self, Event, Players):
		self.Event = Event
		self.Indexes = [0] * self.Event.nOfDimentions
		self.MaxIndex = self.Event.nOfItens -1
		self.Size = len(Players)
    	for Dimention in range(self.Event.nOfDimentions):
			IndexVector = []
			for Player in Players:
				IndexVector.append(Player.Favourites[Dimention])
			
			self.Indexes[Dimention] = IndexVector


	def Transformation(self, SolutionArray, Dimention, Index):
		ItensIndex = []
		ItensIndex.extend(SolutionArray)        
		TempIndex = -1
		SwapIndex = -1
		BestIndex = -1
		TempProfit = 0
		TempWeight = 0
		BestProfit = self.Event.CalculeProfit(SolutionArray)
		for i in range(len(ItensIndex)):
			TempIndex = ItensIndex[i]
			ItensIndex[i] = Index
			TempProfit = self.Event.CalculeProfit(ItensIndex)
			TempWeight = self.Event.CalculeWeight(ItensIndex)
			if(TempProfit > BestProfit and TempWeight <= self.Event.Knapsack[Dimention]):
				SwapIndex = i
				BestProfit = TempProfit
			ItensIndex[i] = TempIndex
		if(SwapIndex > -1):
			ItensIndex[SwapIndex] = Index
			return {"BetterSolution": ItensIndex, "BetterProfit": BestProfit}
		else:
			return None	
		

	def TryBetterSolution(self, Solution):
		nOfDimentions = self.Event.nOfDimentions
		BestSolution.extend(Solution)
		BestProfits = [0] * nOfDimentions
		BestTempSolution = []
		TempProfit = 0
		BestIndexes = [0] * nOfDimentions
		
		for Dimention in range(nOfDimentions):
			BestProfits[Dimention] = self.Event.CalculeProfit(Solution[Dimention])
			for Dimention in range(nOfDimentions):
				for Index in range(self.Size):
					BestTempSolution = self.Transformation(BestSolution[Dimention], Dimention, Index)
					if(BestTempSolution):
						BestSolution[Dimention] = BestTempSolution["BetterSolution"]
						BestProfits[Dimention] = BestTempSolution["BetterProfit"]
						BestIndex[Dimention] = Index
		
		return {"BestSolution": BestSolution, "BestIndexes": BestIndexes, "BestProfits": BestProfits}
