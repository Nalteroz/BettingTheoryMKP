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
		out = "Mask size per dimention: " + str(self.Size) 
		out += "\nIndexes: \n["
		for i in range(len(self.Indexes)):
			out += "["
			for j in range(len(self.Indexes[0])):
				out += str(self.Indexes[i][j]) + " "
			out += "]"
		out+="\n"
		return out

	def Transformation(self, SolutionArray, Dimention, Index):
		TempSolution = SolutionArray
		TempIndex = -1
		SwapIndex = -1
		BestIndex = -1
		TempProfit = 0
		TempWeight = 0
		BestWeight = self.Event.CalculeProfit(SolutionArray)
		BestProfit = self.Event.CalculeWeight(SolutionArray)

		for idx in range(len(SolutionArray)):
			TempIndex = TempSolution[idx]
			TempSolution[idx] = Index
			TempProfit = self.Event.CalculeProfit(TempSolution)
			TempWeight = self.Event.CalculeWeight(TempSolution)

			if((TempProfit > BestProfit and TempWeight <= self.Event.Knapsack[Dimention]) or
			 (TempProfit >= BestProfit and TempWeight < BestWeight)):
				SwapIndex = idx
				BestProfit = TempProfit
				BestWeight = TempWeight
			TempSolution[idx] = TempIndex

		if(SwapIndex > -1):
			TempSolution[SwapIndex] = Index
			return {'Solution': TempSolution, 'Weight': BestWeight, 'Profit': BestProfit}
		else:
			return None	
		
	def TryBetterSolution(self, Solution):
		nOfDimentions = self.Event.nOfDimentions
		BestSolution = Solution.copy()
		BestTempSolution = None
		BestMaskIndexes = [-1] * nOfDimentions
		TotalWeight = 0
		TotalProfit = 0

		for Dimention in range(nOfDimentions):
			for Index in range(self.Size):
				BestTempSolution = self.Transformation(BestSolution['Solution'][Dimention], Dimention, self.Indexes[Dimention][Index])
				if(BestTempSolution):
					BestSolution['Solution'][Dimention] = BestTempSolution["Solution"]
					BestSolution['Profits'][Dimention] = BestTempSolution["Profit"]
					BestSolution['Weights'][Dimention] = BestTempSolution["Weight"]
					BestMaskIndexes[Dimention] = Index
		for Dimention in range(nOfDimentions):
			TotalWeight += BestSolution['Weights'][Dimention]
			TotalProfit += BestSolution['Profits'][Dimention]

		BestSolution['BestIndexes'] = BestMaskIndexes
		BestSolution['TotalWeight'] = TotalWeight
		BestSolution['TotalProfit'] = TotalProfit

		return BestSolution
