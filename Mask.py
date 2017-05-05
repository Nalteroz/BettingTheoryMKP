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

	def Transformation(self, InitialSolution, Dimention, Index):
		MySolution = InitialSolution.copy()
		IniSolution = TempSolution['Solution']
		TempIndex = -1
		SwapIndex = -1
		BestIndex = -1
		TempProfit = 0
		TempWeight = 0
		BestWeight = 0

		for idx in range(len(IniSolution[Dimention])):
			TempIndex = IniSolution[Dimention][idx]
			IniSolution[Dimention][idx] = Index
			TempProfit = self.Event.CalculeProfit(IniSolution[Dimention])
			TempWeight = self.Event.CalculeWeight(IniSolution[Dimention])
			if((TempProfit > TempSolution['Profits'][Dimention] and TempWeight <= self.Event.Knapsack[Dimention]) or (TempProfit >= TempSolution['Profits'][Dimention] and TempWeight < TempSolution['Weights'][Dimention])):
				SwapIndex = idx
				BestProfit = TempProfit
				BestWeight = TempWeight
			ItensIndex[i] = TempIndex
		if(SwapIndex > -1):
			ItensIndex[SwapIndex] = Index
			return {"Solution": ItensIndex, "Profit": BestProfit, "Weight": BestWeight}
		else:
			return None	
		
	def TryBetterSolution(self, Solution):
		nOfDimentions = self.Event.nOfDimentions
		BestSolution = Solution.copy()
		BestTempSolution = None
		BestIndexes = [0] * nOfDimentions
		TotalWeight = 0
		TotalProfit = 0

		for Dimention in range(nOfDimentions):
			for Index in range(self.Size):
				BestTempSolution = self.Transformation(BestSolution, Dimention, self.Indexes[Dimention][Index])
				if(BestTempSolution):
					BestSolution[Dimention] = BestTempSolution["Solution"]
					BestProfits[Dimention] = BestTempSolution["Profit"]
					BestWeights[Dimention] = BestTempSolution["Weight"]
					BestIndexes[Dimention] = Index
		for Dimention in range(nOfDimentions):
			TotalWeight += BestWeights[Dimention]
			TotalProfit += BestProfits[Dimention]


		return {"Solution": BestSolution, "BestIndexes": BestIndexes, "Profits": BestProfits, "Weights": BestWeights, "TotalWeight": TotalWeight, "TotalProfit": TotalProfit}
