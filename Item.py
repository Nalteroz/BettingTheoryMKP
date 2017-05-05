#!/usr/bin/python

class Item():
	Index = -1
	Weight = 0
	Profit = 0

	def __init__(self, Index, Weight = 10, Profit = 1):
		self.Index = Index
		self.Weight = Weight
		self.Profit = Profit
	def __len__(self):
		return Weight * Value
	def __str__(self):
		out = "(" + str(self.Weight) + ", " + str(self.Profit) + ")"
		return out
