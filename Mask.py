#!/usr/bin/python

from random import randint

class Mask():
    Indexes = []
    MaxIndex = 0

    def __init__(self, Size, MaxIndex):
        self.MaxIndex = MaxIndex
        self.Indexes = [0] * Size
        for i in range(Size):
            Index = randint(0, self.MaxIndex)
            while Index in self.Indexes:
                Index = randint(0, self.MaxIndex)
            self.Indexes[i] = Index

    def Transformation(self, Event, Solution, Index):
        pass

    def GetBetterMask(self, Event, Solution):
        pass

    def CalculeWeight(self, Index, Tendings):
        pass
