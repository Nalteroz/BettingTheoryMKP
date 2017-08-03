#!/usr/bin/python

from random import randint
from random import random
from math import fabs
from Item import Item

class Event():
	nOfItens = 0
	nOfConstraints = 0
	Optimal = 0
	ItensPicked = []
	Knapsack = []
	Inventory = []
	ItemMaxWeight = []

	def __init__(self, nOfItens, nOfConstraints, Optimal, Inventory, Knapsack):
		self.nOfItens = nOfItens
		self.ItensPicked = [0] * nOfItens
		self.nOfConstraints = nOfConstraints
		self.Optimal = Optimal
		self.Knapsack = Knapsack
		self.Inventory = Inventory
		self.ItemMaxWeight = self.GetMaxWeights()


		'''
		else:
			self.Knapsack = [0] * nOfDimentions
			self.nOfDimentions = nOfDimentions
			self.Inventory = [0] * nOfItens
			self.nOfItens = nOfItens
			#self.ItensPickList = [Bounderie] * nOfItens
			self.DimentionsMaxCapacity = MaxDimensionCapacity
			self.ItensMaxWeight = MaxItenWeight
			self.ItensMaxProfit = MaxProfit
			for i in range(nOfDimentions):
				self.Knapsack[i] = randint(0, MaxDimensionCapacity)
			for i in range(nOfItens):
				self.Inventory[i] = Item(i, randint(1, MaxItenWeight), randint(0, MaxProfit))
		'''

	def GetMaxWeights(self):
		Weights = [0] * self.nOfConstraints
		tIndex = 0
		for Constraint in range(self.nOfConstraints):
			tIndex= 0
			for ItemIndex in range(self.nOfItens):
				if(self.Inventory[ItemIndex].Weight[Constraint] > self.Inventory[tIndex].Weight[Constraint]):
					Weights[Constraint] = self.Inventory[ItemIndex].Weight[Constraint]
					tIndex = ItemIndex
		return Weights


	def __str__(self):
		tw = 0
		out = "N of Constraints: " + str(self.nOfConstraints)
		out += "\nN of Itens: " + str(self.nOfItens)
		out += "\nOptimal: " + str(self.Optimal)
		out += "\nKnapsack:\n"
		out += "\t[ "
		for i in self.Knapsack:
			out += str(i) + " "
			tw+=i
		out += "] \nTotal Weight Suported: " + str(tw)
		out += "\nInventory:\n"
		out += "\n["
		for i in self.Inventory: out += str(i)
		out += "]\n"
		out += "\nMax Weights:\n"
		out += "\n["
		for i in self.ItemMaxWeight: out += str(i) + " "
		out += "]\n"
		return out

	def CalculeWeight(self, IndexList, Constraint):
		Weight = 0
		for ItemIndex in IndexList:
			Weight += self.Inventory[ItemIndex].Weight[Constraint]
		return Weight

	def CalculeProfit(self, IndexList):
		Profit = 0
		for ItemIndex in IndexList:
			Profit += self.Inventory[ItemIndex].Profit
		return Profit

	def isSomeElseFit(self, Constraint, SolutionVector):
		for i in range(self.nOfItens):
			if(self.CalculeWeight(SolutionVector, Constraint)+self.Inventory[i].Weight[Constraint] <= self.Knapsack[Constraint] ):
				return i
		return -1

	def CheckIfIsIn(self, Index, Solution):
		for i in range(len(Solution)):
			if Index in Solution[i]:
				return True
		return False

	def RandIndexList(self):
		RandomList = [-1] * self.nOfItens
		PickList = [1] * self.nOfItens
		CheckList = []
		for idx in range(self.nOfItens):
			ItemIndex = randint(0, self.nOfItens - 1)
			RandomList[idx] = ItemIndex
			PickList[ItemIndex] = 0




	def GetInitialSolution(self):
		Index = -1
		Weight = 0
		Weights = [0] * self.nOfConstraints
		Profits = [0] * self.nOfConstraints
		Solution = [0] * self.nOfConstraints
		for i in range(self.nOfConstraints):
			Solution[i] = [0] * self.nOfItens
		TotalWeight = 0
		TotalProfit = 0
		Fit = False
		Constraint = 0
		ItensPicked = [0] * self.nOfItens
		ItensLeft = self.nOfItens
		MaxMisses = 10

		for Constraint in range(self.nOfConstraints):
			Selection = [0] * self.nOfItens
			Fit = False
			while not Fit:
				Weight = 0
				Miss = 0
				while (self.Knapsack[Constraint] - Weight) >= self.ItensMaxWeights[Constraint] or ItensLeft > 0:
					if Miss < MaxMisses:
						Index = randint(0, self.nOfItens - 1)
						while ItensPicked[Index]:
							Index = randint(0, self.nOfItens - 1)
						Selection.append(Index)
						Weight += self.Inventory[Index].Weight[Constraint]
				if(Weight > self.Knapsack[Constraint]):
					Selection.pop()
				else:
						Fit = True
			Solution[Constraint] = Selection

		while Constraint < self.nOfConstraints:
			SomeElseFit = self.isSomeElseFit(Constraint, Solution[Dimention])
			if(SomeElseFit>=0):
				Solution[Constraint].append(SomeElseFit)
			else: Constraint+=1

		for Constraint in range(self.nOfConstraints):
			Weights[Constraint] = self.CalculeWeight(Solution[Constraint])
			TotalWeight += Weights[Constraint]
			Profits[Constraint] = self.CalculeProfit(Solution[Constraint])
			TotalProfit += Profits[Constraint]

		return {"Solution": Solution, "Profits": Profits,
				"Weights": Weights, "TotalWeight": TotalWeight, "TotalProfit": TotalProfit}



