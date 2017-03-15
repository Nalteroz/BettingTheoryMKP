#!/usr/bin/python

from random import randint
from random import random
from math import fabs
from Item import Item

class Event():
    Knapsack = []
    DimentionsMaxCapacity = 0
    Inventory = []
    ItensMaxWeight = 0
    ItensMaxProfit = 0
    

    def __init__(self, FileName=None, nOfDimentions=10, MaxDimensionCapacity=100,
                 nOfItens=30, MaxItenWeight=15, MaxProfit = 10):
        if FileName is None :
            self.Knapsack = [0] * nOfDimentions
            self.Inventory = [0] * nOfItens
            self.DimentionsMaxCapacity = MaxDimensionCapacity
            self.ItensMaxWeight = MaxItenWeight
            self.ItensMaxProfit = MaxProfit
            for i in range(0, nOfDimentions):
                self.Knapsack[i] = randint(0, MaxDimensionCapacity)
            for i in range(0, nOfItens):
                self.Inventory[i] = Item(i, randint(0, MaxItenWeight), randint(0, MaxProfit))        
    def __str__(self):
        out = "Knapsack:\n"
        out += "\t[ "
        for i in self.Knapsack: out += str(i) + " "
        out += "]\nInventory:\n"
        out += "\t[ "
        for i in self.Inventory: out += "["+str(i.Weight)+" "+str(i.Profit)+"]"
        out += " ]"
        return out

    def EventLen(self):
        v = []
        v.append(len(self.Knapsack))
        v.append(len(self.Inventory))
        return v

    def CalculeItensWeight(self, Indexes): 
        Weight = 0
        for ItemIndex in Indexes:
            Weight += self.Inventory[ItemIndex].Weight
        return Weight
    
    def CalculeItensProfit(self, Indexes): 
        Profit = 0
        for ItemIndex in Indexes:
            Weight += self.Inventory[ItemIndex].Profit
        return Profit
    
    def isSomeElseFit(self, DimentionIndex, SolutionVector):
        for i in range(len(self.Inventory)):
            if(self.CalculeItensWeight(SolutionVector)+self.Inventory[i].Weight
               <= self.Knapsack[DimentionIndex]
               and i not in SolutionVector):
                return i
        return None
                
    def GetInitialSolution(self):
        Index = -1
        Weight = 0
        Solution = []
        Fit = False
        Dimention = 0
        for i in range(len(self.Knapsack)):
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
                if(Weight > self.Knapsack[i]): Selection.pop()
                else:
                    Fit = True
            Solution.append(Selection)
        while Dimention < len(self.Knapsack):
            ItemIndex = self.isSomeElseFit(Dimention, Solution[Dimention])
            if(ItemIndex):
                Solution[Dimention].append(ItemIndex)
            else: Dimention+=1
        return Solution
                
            

