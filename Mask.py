#!/usr/bin/python

from random import randint

class Mask():
    Indexes = []
    MaxIndex = 0

    def __init__(self, Size, nOfDimentions, MaxIndex):
        
        self.MaxIndex = MaxIndex
        self.Indexes = [0] * nOfDimentions
        for Dimention in range(nOfDimentions):
            IndexVector = []
            for i in range(Size):
                Index = randint(0, self.MaxIndex)
                while Index in self.Indexes:
                    Index = randint(0, self.MaxIndex)
                IndexVector.append(Index)
            self.Indexes[Dimention] = IndexVector

    def Transformation(self, Event, Solution, Index):
        pass

    def TryBetterSolution(self, Event, Solution, Dimention):
        BestSolution = Solution
        TempSolution = None
        BestIndex = -1
        BestWeight = 0
        BestProfit = 0

        for Index in range(len(Indexes)):
            TempSolution = self.Transformation(Event, Solution, Index)

    def CalculeWeight(self, Index, Tendings):
        pass
