#!/usr/bin/python
import os
from Event import Event
from Item import Item
from pdb import set_trace as bp

class FileTreater():

	FilePath = "Default"

	def __init__(self, FilePath):
		self.FilePath = FilePath
		#self.fileNameOut = os.path.splitext(fileName)[0] + "Results.txt"
		#self.fileRef = fileName + "Result"

	def LoadEvents(self): 

		Events = []
		nOfItens = 0
		nOfConstraints = 0
		Optimal = 0
		Inventory = []
		Knapsack = []
		CurrentData = []

		with open(self.FilePath, 'r') as FileOpen:
			#Getting number of events in the frist line of the file
			nOfEvents = int(FileOpen.readline())
			Events = [0] * nOfEvents
			for EventIndex in range(nOfEvents):
				CurrentLine = FileOpen.readline()
				LineData = CurrentLine.split()
				#Ignore white lines
				while (len(LineData) == 0):
					CurrentLine = FileOpen.readline()
					LineData = CurrentLine.split()
				#Getting the informetion of the current event
				nOfItens = int(LineData[0])
				nOfConstraints = int(LineData[1])
				Optimal = float(LineData[2])
				Inventory = [0] * nOfItens
				Knapsack = [0] * nOfConstraints
				#Recovery itens profit data
				CurrentData = []
				while len(CurrentData) < nOfItens:
					CurrentLine = FileOpen.readline()
					LineData = CurrentLine.split()
					CurrentData.extend(LineData)
				#Applying itens profits
				for index in range(nOfItens):
					Inventory[index] = Item(index, float(CurrentData[index]), nOfConstraints)
				#Getting itens weight per constraint
				for Constraint in range(nOfConstraints):
					CurrentData = []
					while len(CurrentData) < nOfItens:
						CurrentLine = FileOpen.readline()
						LineData = CurrentLine.split()
						CurrentData.extend(LineData)
						print(CurrentData)
					for index in range(nOfItens):
						Inventory[index].Weight[Constraint] = float(CurrentData[index])
						print(Inventory[index])
				#Getting constraints capacity
				CurrentData = []
				while len(CurrentData) < nOfConstraints:
					CurrentLine = FileOpen.readline()
					LineData = CurrentLine.split()
					CurrentData.extend(LineData)
				#Applying capacities on knapsack
				for Constraint in range(nOfConstraints):
					Knapsack[Constraint] = float(CurrentData[Constraint])
				#Creating Event
				Events[EventIndex] = Event(nOfItens, nOfConstraints, Optimal, Inventory, Knapsack)
				
		return Events

