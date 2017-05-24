#!/usr/bin/python

class Item():
	Index = 0
	Profit = 0
	Weight = []

	def __init__(self, Index, Profit, nOfConstraits):
		self.Index = Index
		self.Profit = Profit
		self.Weight = [0] * nOfConstraits

	def __str__(self):
		out = "Item Index: " + str(self.Index) + ", Profit: " + str(self.Profit)
		out += "\n\tWeights: ["
		for i in range(len(self.Weight)): out+= str(self.Weight[i]) + " "
		out += "]\n" 
		return out
