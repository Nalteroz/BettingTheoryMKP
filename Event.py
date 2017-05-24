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


	def __str__(self):
		tw = 0
		out = "N of Constraints: " + str(self.nOfDimentions)
		out += "\nN of Itens: " + str(self.nOfItens)
		out += "\nKnapsack:\n"
		out += "\t[ "
		for i in self.Knapsack:
			out += str(i) + " "
			tw+=i
		out += "] \nTotal Weight Suported: " + str(tw)
		out += "\nInventory:\n"
		out += "\n "
		for i in self.Inventory: out += str(i)
		out += " ]\n"
		return out

	def EventLen(self):
		return {"Dimentions": self.nOfDimentions, "nOfItens": self.nOfItens}

	def CalculeWeight(self, IndexesList):
		Weight = 0
		for ItemIndex in IndexesList:
			Weight += self.Inventory[ItemIndex].Weight
		return Weight

	def CalculeProfit(self, Indexes):
		Profit = 0
		for ItemIndex in Indexes:
			Profit += self.Inventory[ItemIndex].Profit
		return Profit

	def isSomeElseFit(self, DimentionIndex, SolutionVector):
		for i in range(self.nOfItens):
			if(self.CalculeWeight(SolutionVector)+self.Inventory[i].Weight <= self.Knapsack[DimentionIndex] ):
				return i
		return -1

	def CheckIfIsIn(self, Index, Solution):
		print(Solution)
		for i in range(len(Solution)):
			if Index in Solution[i]:
				return True
		return False

	#def RandomItem(self, Bounded):


	def GetInitialSolution(self):
		Index = -1
		Weight = 0
		Weights = [0] * self.nOfDimentions
		Profits = [0] * self.nOfDimentions
		Solution = [0] * self.nOfDimentions
		for i in range(self.nOfDimentions): Solution[i] = []
		TotalWeight = 0
		TotalProfit = 0
		Fit = False
		Dimention = 0
		ItensLeft = self.nOfItens

		for Dimention in range(self.nOfDimentions):
			Selection = []
			Fit = False
			while not Fit:
				Weight = 0
				while (self.Knapsack[Dimention] - Weight) >= self.ItensMaxWeight:
					Index = randint(0, self.nOfItens - 1)
					#while self.CheckIfIsIn(Index, Solution):
						#Index = randint(0, self.nOfItens - 1)
					Selection.append(Index)
					Weight += self.Inventory[Index].Weight
				if(Weight > self.Knapsack[Dimention]):
					Selection.pop()
				else:
						Fit = True
			Solution[Dimention] = Selection

		while Dimention < self.nOfDimentions:
			SomeElseFit = self.isSomeElseFit(Dimention, Solution[Dimention])
			if(SomeElseFit>=0):
				Solution[Dimention].append(SomeElseFit)
			else: Dimention+=1

		for Dimention in range(self.nOfDimentions):
			Weights[Dimention] = self.CalculeWeight(Solution[Dimention])
			TotalWeight += Weights[Dimention]
			Profits[Dimention] = self.CalculeProfit(Solution[Dimention])
			TotalProfit += Profits[Dimention]

		return {"Solution": Solution, "Profits": Profits,
				"Weights": Weights, "TotalWeight": TotalWeight, "TotalProfit": TotalProfit}



