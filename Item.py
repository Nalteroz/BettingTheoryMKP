#!/usr/bin/python

class Item():
    Index = -1
    Weight = 0
    Importance = 0

    def __init__(self, Index, Weight = 10, Value = 0.5):
        self.Index = Index
        self.Weight = Weight
        self.Value = Value

    def __len__(self):
        return Weight * Value
