#!/usr/bin/python

from random import randint
from math import fabs

class Event():
    Knapsack = []
    DimentionsMaxCapacity = 0
    Inventory = []
    ItensMaxWeight = 0
    

    def __init__(self, FileName=None, nOfDimentions=10, MaxDimensionCapacity=100, nOfItens=30, MaxItenWeight=15):
        if FileName is None :
            self.Knapsack = [0] * nOfDimentions
            self.Inventory = [0] * nOfItens
            self.DimentionsMaxCapacity = MaxDimensionCapacity
            self.ItensMaxWeight = MaxItenWeight
            for i in range(0, nOfDimentions):
                self.Knapsack[i] = randint(0, MaxDimensionCapacity)
            for i in range(0, nOfItens):
                self.Inventory[i] = randint(0, MaxItenWeight)
        
    def __str__(self):
        out = "Knapsack:\n"
        out += "\t[ "
        for i in self.Knapsack: out += str(i) + " "
        out += "]\n Inventory:\n"
        out += "\t[ "
        for i in self.Inventory: out += str(i) + " "
        out += "]"
        return out

    def __len__(self):
        v.append(len(self.Knapsack))
        v.append(len(self.Inventory))
        return v

    def SelectionWeight(self, Selection): 
        Weight = 0
        for ItemIndex in Selection:
            Weight += self.Inventory[ItemIndex]
        return Weight
##Parei aqui!
    def GetInitialSolution(self):
        Intex = 0
        Weight = 0
        Solution = []
        Fit = False
        for i in range(0, len(self.Knapsack)):
            Selection = []
            Weight = 0
            while not Fit:
                print(self.Knapsack[i] - Weight)
                while self.Knapsack[i] - Weight >= self.ItensMaxWeight:
                    Index = randint(0, len(self.Inventory) - 1)
                    Selection.append(Index)
                    Weight += self.Inventory[Index]
                if(Weight > self.Knapsack[i]): Selection.pop()
                else:
                    Fit = True
                
            Solution.append(Selection)

        return Solution
                
            
                
                
