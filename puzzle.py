#!/usr/bin/env python

import sys
from random import randint

class TilePuzzle:
	def __init__(self,size):
		self.size=size
		self.puzzle=[]
		self.zero=(0,0)
		self.moves=["U","D","L","R"]
		count=1
		for x in range(0,size):
			self.puzzle.append([])
			for y in range(0,size):
				self.puzzle[x].append([])
		for x in range(0,size):
			for y in range(0,size):
				self.puzzle[x][y]=count
				count+=1
		self.puzzle[size-1][size-1]=0
		self.zero=(size-1,size-1)

	def readPuzzle(self,string):
		a=string.split(" ")
		count=0
		for x in range(0,self.size):
			for y in range(0,self.size):
				if int(a[count])==0:
					self.zero=(x,y)
				self.puzzle[x][y]=int(a[count])
				count+=1

	def checkPuzzle(self):
		count=1
		for x in range(0,self.size):
			for y in range(0,self.size):
				if self.puzzle[x][y]!=(count%(self.size*self.size)):

					return False
				count+=1
		return True


	#def swap(self,(x1,y1),(x2,y2)):
	def swap(self,o1,o2):
		x1=o1[0]
		y1=o1[1]
		x2=o2[0]
		y2=o2[1]
		temp=self.puzzle[x1][y1]
		self.puzzle[x1][y1]=self.puzzle[x2][y2]
		self.puzzle[x2][y2]=temp

	def up(self):
		if (self.zero[0]!=0):
			self.swap((self.zero[0]-1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]-1,self.zero[1])
	def down(self):
		if (self.zero[0]!=self.size-1):
			self.swap((self.zero[0]+1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]+1,self.zero[1])

	def left(self):
		if (self.zero[1]!=0):
			self.swap((self.zero[0],self.zero[1]-1),self.zero)
			self.zero=(self.zero[0],self.zero[1]-1)


	def right(self):
		if (self.zero[1]!=self.size-1):
			self.swap((self.zero[0],self.zero[1]+1),self.zero)
			self.zero=(self.zero[0],self.zero[1]+1)

	def printPuzzle(self):
		for x in range(0,self.size):
			for y in range(0,self.size):
				print(self.puzzle[x][y],end=" ")
			#print

	def doMove(self,move):
		if move=="U":
			self.up()
		if move=="D":
			self.down()
		if move=="L":
			self.left()
		if move=="R":
			self.right()

	def permute(self,numPerm):
		for i in range(0,numPerm):
			self.doMove(self.moves[randint(0,3)])

	def parseMoveSequence(self,string):
		for m in string:
			self.doMove(m)



#t=tilePuzzle(int(sys.argv[1]))
#t.permute(int(sys.argv[2]))
#t.printPuzzle()
