#!/usr/bin/python

from Event import Event

InputType = 0
MyEvent = None

def GetInput(InputType=0):
    try:
        if(InputType == 0):
            return int(input("\tInt value: "))
        if(InputType == 1):
            v = input("\tAnswer(s|n): ")
            if(v=="s"): return True
            if(v=="n"): return False
            else: return bool(input("\tAnswer(s|n): "))
    except ValueError:
        print("This is no a valid value! Try again.")
        return GetInput(InputType)

""" 
print("Number of dimentions")
nOfDimentions = GetInput(0)
#print(nOfDimentions)

print("Max dimention capacity")
dMaxCapacity = GetInput(0)
#print(dMaxCapacity)

print("Number of itens")
nOfItens = GetInput(0)
#print(nOfItens)

print("Max item weight")
itemMaxWeight = GetInput(0)
#print(itemMaxWeight)
"""

MyEvent = Event()
print(str(MyEvent))
InitialSolution = MyEvent.GetInitialSolution()
print("Solutions: ")
print(InitialSolution)
for i in range(len(MyEvent.Knapsack)):
    print(MyEvent.SelectionWeight(InitialSolution[i]))




