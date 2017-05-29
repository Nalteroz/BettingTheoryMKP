#!/usr/bin/python

from random import randint
from random import random
from math import fabs
from Item import Item

class Event():
	nOfItens = 0
	nOfConstraints = 0
	Optimal = 0
	ItensPickList = []
	Knapsack = []
	Inventory = []

	def __init__(self, nOfItens, nOfConstraints, Optimal, Inventory, Knapsack):
		self.nOfItens = nOfItens
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

	def CalculeWeight(self, IndexesList, Constraint):
		Weight = 0
		for ItemIndex in IndexesList:
			Weight += self.Inventory[ItemIndex].Weight[Constraint]
		return Weight

	def CalculeProfit(self, IndexesList):
		Profit = 0
		for ItemIndex in IndexesList:
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

	#def RandomItem(self, Bounded):

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
		ItensLeft = self.nOfItens

		for Constraint in range(self.nOfConstraints):
			Selection = [0] * self.nOfItens
			Fit = False
			while not Fit:
				Weight = 0
				while (self.Knapsack[Constraint] - Weight) >= self.ItensMaxWeights[Constraint]:
					Index = randint(0, self.nOfItens - 1)
					#while self.CheckIfIsIn(Index, Solution):
						#Index = randint(0, self.nOfItens - 1)
					Selection.append(Index)
					Weight += self.Inventory[Index].Weight
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



