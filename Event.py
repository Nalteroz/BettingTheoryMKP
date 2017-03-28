#!/usr/bin/python

from random import randint
from random import random
from math import fabs
from Item import Item

class Event():
	Knapsack = []
	nOfDimentions = 0
	DimentionsMaxCapacity = 0
	Inventory = []
	nOfItens = 0
	ItensMaxWeight = 0
	ItensMaxProfit = 0

	def __init__(self, FileName=None, nOfDimentions=10, MaxDimensionCapacity=100, nOfItens=30, MaxItenWeight=10, MaxProfit = 50):
		if FileName is None :
			self.Knapsack = [0] * nOfDimentions
			self.nOfDimentions = nOfDimentions
			self.Inventory = [0] * nOfItens
			self.nOfItens = nOfItens
			self.DimentionsMaxCapacity = MaxDimensionCapacity
			self.ItensMaxWeight = MaxItenWeight
			self.ItensMaxProfit = MaxProfit
		for i in range(nOfDimentions):
			self.Knapsack[i] = randint(0, MaxDimensionCapacity)
		for i in range(nOfItens):
			self.Inventory[i] = Item(i, randint(0, MaxItenWeight), randint(0, MaxProfit))      

	def __str__(self):
		out = "Knapsack:\n"
		out += "\t[ "
		for i in self.Knapsack: out += str(i) + " "
		out += "]\nInventory:\n"
		out += "\t[ "
		for i in self.Inventory: out += "("+str(i.Weight)+" "+str(i.Profit)+")"
		out += " ]"
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
			if(self.CalculeWeight(SolutionVector)+self.Inventory[i].Weight <= self.Knapsack[DimentionIndex] and i not in SolutionVector):
				return i
		return None

	def GetInitialSolution(self):
		Index = -1
		Weight = 0
		Solution = [0] * self.nOfDimentions
		Fit = False
		Dimention = 0
		for i in range(self.nOfDimentions):
			Selection = []
			Fit = False
			while not Fit:
				Weight = 0
				while (self.Knapsack[i] - Weight) >= self.ItensMaxWeight:
					Index = randint(0, len(self.Inventory) - 1)
					#while Index in Solution:
					#    Index = randint(0, len(self.Inventory) - 1)
					Selection.append(Index)
					Weight += self.Inventory[Index].Weight
					if(Weight > self.Knapsack[i]):
						Selection.pop()
					else:
						Fit = True
			Solution[i] = Selection
			
		while Dimention < self.nOfDimentions:
			SomeElseFit = self.isSomeElseFit(Dimention, Solution[Dimention])
			if(SomeElseFit):
				Solution[Dimention].append(SomeElseFit)
			else: Dimention+=1
		return Solution
				
			

